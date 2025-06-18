import network
import socket
import time
from machine import Pin, I2C
from mpu6050 import MPU6050

# ---- I2C Setup ----
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# ---- Scan I2C Devices ----
devices = i2c.scan()
if 0x68 not in devices:
    print("MPU6050 not detected. Check wiring and power.")
    raise SystemExit()

# ---- MPU6050 Setup ----
mpu = MPU6050(i2c)

# ---- Tilt Threshold ----
TILT_THRESHOLD = 0.7

# ---- Motor Pins Setup ----
r_f = Pin(15, Pin.OUT)
r_b = Pin(18, Pin.OUT)
l_f = Pin(4, Pin.OUT)
l_b = Pin(5, Pin.OUT)

def all_off():
    r_f.value(1)
    r_b.value(1)
    l_f.value(1)
    l_b.value(1)

# ---- Initial State ----
all_off()

# ---- Main Loop ----
def main():
    while True:
        try:
            accel = mpu.get_accel()
            x = accel['x']
            y = accel['y']

            # Default to STOP
            direction = "Level"
            all_off()

            if abs(x) < TILT_THRESHOLD and abs(y) < TILT_THRESHOLD:
                direction = "Level"
                all_off()

            elif y > TILT_THRESHOLD:
                direction = "FORWARD"
                r_f.value(0); r_b.value(1)
                l_f.value(0); l_b.value(1)

            elif y < -TILT_THRESHOLD:
                direction = "BACKWARD"
                r_f.value(1); r_b.value(0)
                l_f.value(1); l_b.value(0)

            elif x > TILT_THRESHOLD:
                direction = "RIGHT"
                r_f.value(1); r_b.value(0)
                l_f.value(0); l_b.value(1)

            elif x < -TILT_THRESHOLD:
                direction = "LEFT"
                r_f.value(0); r_b.value(1)
                l_f.value(1); l_b.value(0)

            print(f"X: {x:.2f}g, Y: {y:.2f}g → {direction}")
            time.sleep(0.1)

        except OSError as e:
            print("MPU6050 read error:", e)
            all_off()
            time.sleep(0.5)

# ---- Start ----
main()

