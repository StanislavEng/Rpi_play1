import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
work = 11
GPIO.setup(work,GPIO.OUT)
myPWM = GPIO.PWM(work,1000)
myPWM.start(0)
while(1):
    bright = input("What % brightness do you want in the LED?")
    if bright == "exit":
        break
    else:
        myPWM.ChangeDutyCycle(bright)
    
#   bright = input("How bright do you want the LED?\nEnter value between 1-6")
#   myPWM.ChangeDutyCycle(math.log(2**bright))
    
myPWM.stop()
GPIO.cleanup()
