import RPi.GPIO as GPIO
import time

servo = 11
Hz = 50
start = 0
end = 180

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo, GPIO.OUT)
mypwm = GPIO.PWM(servo,Hz)
mypwm.start(7.5)

for i in range(start,end):
    dc = i*9.5/180. + 2.5
    mypwm.ChangeDutyCycle(dc)
    time.sleep(0.05)
for i in range(end,start,-1):
    dc = i*9.5/180. + 2.5
    mypwm.ChangeDutyCycle(dc)
    time.sleep(0.05)
mypwm.ChangeDutyCycle(7.5)
mypwm.stop()
GPIO.cleanup()