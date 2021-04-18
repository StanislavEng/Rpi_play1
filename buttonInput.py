import RPi.GPIO as GPIO
from time import sleep

b1 = 11 # button 1
b2 = 16 # button 2

GPIO.setmode(GPIO.BOARD)
buttons = [b1, b2]
for pin in buttons:
    GPIO.setup(pin, GPIO.IN,pull_up_down=GPIO.PUD_UP)
    print("The iter is ", pin)
try:
    while 1:
        if GPIO.input(b1) == 0:
            print("Button one was pressed")
            sleep(.1)
        if GPIO.input(b2) == 0:
            print("Button two was pressed")
            sleep(.1)
except KeyboardInterrupt:        
    GPIO.cleanup()