from RPi import GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

while True:
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(26, GPIO.LOW)
    time.sleep(1)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(26, GPIO.HIGH)
    time.sleep(1)
