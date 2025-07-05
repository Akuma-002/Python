import network
import socket
from machine import UART
import _thread
import utime

# --- GPS Setup ---
gps = UART(2, baudrate=9600, rx=16, tx=17)

# --- Check if GPS is connected ---
print("Checking GPS connection...")
gps_detected = False
start_time = utime.ticks_ms()

while utime.ticks_diff(utime.ticks_ms(), start_time) < 5000:
    if gps.any():
        line = gps.readline()
        if line and (b'$GPGGA' in line or b'$GPRMC' in line):
            gps_detected = True
            print("GPS module detected.")
            break
    utime.sleep_ms(100)

if not gps_detected:
    print("GPS not detected. Check wiring and antenna.")
    raise SystemExit

# --- Shared variables ---
latest_lat = None
latest_lon = None
gps_running = True

# --- Robust GPS parser ---
def parse_lat_lon(nmea):
    try:
        line = nmea.decode().strip()
        if line.startswith('$GPGGA'):
            parts = line.split(',')
            if len(parts) >= 6 and parts[2] and parts[3] and parts[4] and parts[5]:
                lat, lat_dir = parts[2], parts[3]
                lon, lon_dir = parts[4], parts[5]
            else:
                return None, None
        elif line.startswith('$GPRMC'):
            parts = line.split(',')
            if len(parts) >= 7 and parts[3] and parts[4] and parts[5] and parts[6]:
                lat, lat_dir = parts[3], parts[4]
                lon, lon_dir = parts[5], parts[6]
            else:
                return None, None
        else:
            return None, None

        # Parse latitude
        lat_deg = float(lat[:2])
        lat_min = float(lat[2:])
        latitude = lat_deg + (lat_min / 60)
        if lat_dir == 'S':
            latitude = -latitude

        # Parse longitude
        lon_deg = float(lon[:3])
        lon_min = float(lon[3:])
        longitude = lon_deg + (lon_min / 60)
        if lon_dir == 'W':
            longitude = -longitude

        return latitude, longitude

    except Exception as e:
        print("Parsing error:", e)
        return None, None

# --- GPS Reader Thread ---
def gps_reader():
    global latest_lat, latest_lon
    while gps_running:
        if gps.any():
            nmea = gps.readline()
            if nmea:
                lat, lon = parse_lat_lon(nmea)
                if lat and lon:
                    latest_lat = lat
                    latest_lon = lon
                    print("Latitude:", lat)
                    print("Longitude:", lon)
                    print("-----------------------")
        utime.sleep_ms(200)

# --- Wi-Fi AP Setup ---
ssid = "ESP"
password = "12345678"

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)
print("Access Point started. Connect to SSID:", ssid)
print("IP address:", ap.ifconfig()[0])

# --- Start GPS thread immediately ---
_thread.start_new_thread(gps_reader, ())

# --- Wait for Wi-Fi client ---
print("Waiting for a client to connect...")
while ap.status('stations') == []:
    utime.sleep(1)
print("Client connected. Starting server...")

# --- HTML Page ---
html = """<!DOCTYPE html>
<html>
<head>
  <title>ESP32 GPS Address</title>
  <script>
    function getLocationAndAddress() {
      fetch('/location')
        .then(response => response.json())
        .then(data => {
          document.getElementById('coords').innerText =
            'Latitude: ' + data.lat + '\\nLongitude: ' + data.lon;
          if (data.lat !== "N/A" && data.lon !== "N/A") {
            // Use OpenStreetMap Nominatim API for reverse geocoding
            fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${data.lat}&lon=${data.lon}`)
              .then(resp => resp.json())
              .then(addrData => {
                document.getElementById('address').innerText =
                  addrData.display_name || "Address not found";
              })
              .catch(() => {
                document.getElementById('address').innerText = "Error fetching address";
              });
          } else {
            document.getElementById('address').innerText = "No valid coordinates yet.";
          }
        })
        .catch(err => {
          document.getElementById('coords').innerText = 'Error: ' + err;
          document.getElementById('address').innerText = '';
        });
    }
  </script>
</head>
<body>
    <div class="mainBox">
        <h2>ESP32 GPS Location & Address</h2>
        <button onclick="getLocationAndAddress()">Get Address</button>
        <pre id="coords"></pre>
        <pre id="address" style="color:blue"></pre>
    </div>
    
</body>
<style>
    body{
        padding: 100px;
        background-color: aqua;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .mainBox{
        border: 2px solid white;
        height: 200px;
        width: 400px;
        border-radius: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        background-color:lightblue;
    }
</style>
</html>
"""

# --- Web Server ---
def serve():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print("Web server running at http://%s/" % ap.ifconfig()[0])

    while True:
        cl, addr = s.accept()
        req = cl.recv(1024)
        req_str = req.decode()
        if 'GET /location' in req_str:
            if latest_lat is not None and latest_lon is not None:
                response = '{{"lat": {:.6f}, "lon": {:.6f}}}'.format(latest_lat, latest_lon)
            else:
                response = '{"lat": "N/A", "lon": "N/A"}'
            cl.send('HTTP/1.0 200 OK\r\nContent-Type: application/json\r\n\r\n')
            cl.send(response)
        else:
            cl.send('HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n')
            cl.send(html)
        cl.close()

# --- Start Server ---
serve()

