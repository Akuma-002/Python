from machine import Pin, PWM
from time import sleep

# Servo setup
servo_pin_fr = Pin(13)  # Change to your GPIO pin
servo_fr = PWM(servo_pin_fr, freq=50)  # 50Hz PWM frequency
servo_pin_fl = Pin(15)  # Change to your GPIO pin
servo_fl = PWM(servo_pin_fl, freq=50)
servo_pin_br = Pin(14)  # Change to your GPIO pin
servo_br = PWM(servo_pin_br, freq=50)  # 50Hz PWM frequency
servo_pin_bl = Pin(18)  # Change to your GPIO pin
servo_bl = PWM(servo_pin_bl, freq=50)  # 50Hz PWM frequency
# Function to set servo angle (0 - 180 degrees)
def set_angleFR(angle):
    min_duty = 26   # ~0.5ms pulse for 0°
    max_duty = 128  # ~2.5ms pulse for 180°
    duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
    servo_fr.duty(duty)

def set_angleFL(angle):
    min_duty = 26   # ~0.5ms pulse for 0°
    max_duty = 128  # ~2.5ms pulse for 180°
    duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
    servo_fl.duty(duty)


def set_angleBR(angle):
    min_duty = 26   # ~0.5ms pulse for 0°
    max_duty = 128  # ~2.5ms pulse for 180°
    duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
    servo_br.duty(duty)


def set_angleBL(angle):
    min_duty = 26   # ~0.5ms pulse for 0°
    max_duty = 128  # ~2.5ms pulse for 180°
    duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
    servo_bl.duty(duty)

# Start at 90° initially
set_angleFR(90)
set_angleFL(90)
set_angleBR(90)
set_angleBL(90)
sleep(1)  # Hold for a moment before starting motion

try:
    while True:
        # Move 90° -> 180°
        for angle in range(90, -1, -5):  # Smaller step for smooth motion
            set_angleFR(angle)
            set_angleBL(180 - angle)
            set_angleFL(90 + angle)
            set_angleBR(90 - angle)
            sleep(0.02)  # Short delay for smooth motion
        
        # Move 180° -> 90°
        for angle in range(0, 91, -5):
            set_angleFR(angle)
            set_angleBL(180 - angle)
            set_angleFL(90 + angle)
            set_angleBR(90 - angle)
            sleep(0.02)  # Short delay for smooth motion

except KeyboardInterrupt:
    print("Stopped by user.")
    servo_fr.deinit()
    servo_fl.deinit()
    servo_br.deinit()
    servo_bl.deinit()# Cleanup
    

