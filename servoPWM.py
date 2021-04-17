import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
servo = 11
GPIO.setup(servo,GPIO.OUT)
myservo = GPIO.PWM(servo, 50)
myservo.start(7.5)

try:
    while True:
        leAngle = input("What Angle do you want to get to (Between 0 and 180)\n")
# works but best in py3 
#         if leAngle == 'done':
#             print("\n")
#             myservo.stop()
#             GPIO.cleanup()
#             exit()
# converts variable from string to input because
# in py3 it's default string, in py2 its default int
#        leAngle = int(leAngle)
# keeping the py2 version for now because my except covers exiting and
# the py2 math seems more accurate for the servo
        if leAngle >= 0 and leAngle <= 180:
            leDC = (leAngle*1./18.)+2
            myservo.ChangeDutyCycle(leDC)
        else:
            print("That was not a valid answer")
except KeyboardInterrupt:
    print("\n")
    myservo.stop()
    GPIO.cleanup()
    exit()