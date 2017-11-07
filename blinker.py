from RPi import GPIO
import time

# LED configuration (BCM numbering)
led1 = 20
led2 = 26

# Number of seconds between blinks
t = 1

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

# Blinker loop
while True:
    GPIO.output(led1, GPIO.HIGH)
    GPIO.output(led2, GPIO.LOW)
    time.sleep(t)
    GPIO.output(led1, GPIO.LOW)
    GPIO.output(led2, GPIO.HIGH)
    time.sleep(t)
