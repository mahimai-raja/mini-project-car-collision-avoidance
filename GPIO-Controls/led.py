import RPi.GPIO as GPIO
import time

Buzzer = 12
BuzzerPin = pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(BuzzerPin, GPIO.OUT)
GPIO.output(BuzzerPin, GPIO.HIGH)
time.sleep(5)

GPIO.output(BuzzerPin, GPIO.LOW)
GPIO.cleanup()



import RPi.GPIO as GPIO 
from time import sleep 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

try :
    while True: 
        GPIO.output(8, GPIO.HIGH) 
        sleep(1) 
        GPIO.output(8, GPIO.LOW) 
        sleep(1) 
except KeyboardInterrupt:
    GPIO.output(8,GPIO.LOW)
    GPIO.cleanup()