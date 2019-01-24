import RPi.GPIO as GPIO
import Adafruit_LSM303
lsm303 = Adafruit_LSM303.LSM303()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17, GPIO.LOW)

while True:
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    if accel_y > 50:
        GPIO.output(17, GPIO.HIGH) 
    else:
        GPIO.output(17, GPIO.LOW)
        
GPIO.output(17, GPIO.LOW)
