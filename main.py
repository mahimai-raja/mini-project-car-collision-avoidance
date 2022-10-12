import RPi.GPIO as GPIO
import time
import pyfiglet

ledPin = 7


ENA = 33
IN1 = 35
IN2 = 37

def setup():
    GPIO.setwarnings(False) 
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)
    # initialize EnA, In1 and In2
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)

    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    time.sleep(1)

def Ledon():
    GPIO.output(ledPin, GPIO.HIGH) 
    time.sleep(5)
    

def Ledoff():
    GPIO.output(ledPin, GPIO.LOW) 
    time.sleep(1)


def main():
    while True:
        GPIO.setmode(GPIO.BOARD)

        # Forward
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        # time.sleep(20)
        x = input('Enter the x value')

        if x != 'person':
            pass
        else:
            print(pyfiglet.figlet_format('H U M A N'))
            GPIO.output(ENA, GPIO.LOW)
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.LOW)
            Ledon()
            print('we have detected a human in the vision and \nfor safety purpose we have slow stopped the vehicle')
            Ledoff()
            GPIO.cleanup()
            setup()
        

if __name__ == '__main__':
    setup()
    try:
        main()
        
    except KeyboardInterrupt:
        GPIO.output(ENA, GPIO.LOW)
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        Ledoff()
        GPIO.cleanup()
        ('Interuptted by keyboard')