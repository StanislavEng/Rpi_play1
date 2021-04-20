import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

b1 = 11 # button 1
b2 = 16 # button 2
blue = 12 # blue LED
yellow = 15 # yellow LED

LED = [blue,yellow]
button = [b1, b2]
for pin in button: # set up buttons as input
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for pin in LED: # set up LED as output
    GPIO.setup(pin,GPIO.OUT)

pwm1 = GPIO.PWM(blue,1000)
pwm2 = GPIO.PWM(yellow,1000)
pwm1.start(0)
pwm2.start(0)
bright = 1
try:
    while True:
        if GPIO.input(b1) == 0:
            bright = bright/1.25
            if bright < 1:
                bright = 1
                print("You are at min brightness")
            pwm1.ChangeDutyCycle(bright)
            pwm2.ChangeDutyCycle(bright)
            print "Your brightness is : ", bright
            sleep(.25)
        if GPIO.input(b2) == 0:
            bright = bright*1.25
            if bright>100:
                bright = 100
                print ("You are at full brightness")
            pwm1.ChangeDutyCycle(bright)
            pwm2.ChangeDutyCycle(bright)
            print "Your brightness is : ", bright
            sleep(.25)

        
except KeyboardInterrupt:
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()