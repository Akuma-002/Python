from machine import I2C, Pin
import time
from mpu6050 import MPU6050

# Initialize I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# MPU6050 instance
mpu = MPU6050(i2c)

TILT_THRESHOLD = 0.3  # Adjust for your setup

while True:
    accel = mpu.get_accel()
    x = accel['x']
    y = accel['y']

    direction = "Level"

    if x > TILT_THRESHOLD:
        direction = "Tilted RIGHT"
    elif x < -TILT_THRESHOLD:
        direction = "Tilted LEFT"
    elif y > TILT_THRESHOLD:
        direction = "Tilted FORWARD"
    elif y < -TILT_THRESHOLD:
        direction = "Tilted BACKWARD"

    print(f"X: {x:.2f}g, Y: {y:.2f}g → {direction}")
    time.sleep(0.5)
