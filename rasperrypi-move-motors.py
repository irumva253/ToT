from gpiozero import Motor, PWMOutputDevice
import time

# Motor setup
motor1 = Motor(forward=24, backward=23)
motor2 = Motor(forward=27, backward=22)
enablePin1 = PWMOutputDevice(25)
enablePin2 = PWMOutputDevice(17)

def setup():
    enablePin1.value = 0.5  # Set initial speed for motor1
    enablePin2.value = 0.5  # Set initial speed for motor2

def loop():
    motor1.backward()
    motor2.forward()
    # Here you can add more motor control logic if needed

if _name_ == "_main_":
    setup()
    
    while True:
        loop()
        time.sleep(0.1)  # Add a short delay to prevent overwhelming the CPU