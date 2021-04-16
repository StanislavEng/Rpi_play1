import RPi.GPIO as GPIO
import time

comp = 16

red = 11
blue = 12
yellow = 15
green = 13

rl = 0
bl = 0
yl = 0
gl = 0
#####
rm = 0
bm = 0
ym = 0
gm = 0


GPIO.setmode(GPIO.BOARD)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
GPIO.setup(yellow,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)

while True:
	blink_to = input("What number do you want to count to in binary? ")
	if int(blink_to) < comp:
		break
	else:
		print("Not an option")

for i in range(0,blink_to+1):
    if i == 1:
        GPIO.output(red,1)
    if i == 2:
        GPIO.output(red,0)
        GPIO.output(blue,1)
    if i == 3:
        GPIO.output(red,1)
    if i == 4:
        GPIO.output(red,0)
        GPIO.output(blue,0)
        GPIO.output(yellow,1)
    if i == 5:
        GPIO.output(red,1)
    if i == 6:
        GPIO.output(red,0)
        GPIO.output(blue,1)
    if i == 7:
        GPIO.output(red,1)
    if i == 8:
        GPIO.output(red,0)
        GPIO.output(blue,0)
        GPIO.output(yellow,0)
        GPIO.output(green,1)
    if i == 9:
        GPIO.output(red,1)
    if i == 10:
        GPIO.output(red,0)
        GPIO.output(blue,1)
    if i == 11:
        GPIO.output(red,1)
    if i == 12:
        GPIO.output(red,0)
        GPIO.output(blue,0)
        GPIO.output(yellow,1)
    if i == 13:
        GPIO.output(red,1)
    if i == 14:
        GPIO.output(red,0)
        GPIO.output(blue,1)
    if i == 15:
        GPIO.output(red,1)
    time.sleep(1)
time.sleep(15)
GPIO.output(red,0)
GPIO.output(blue,0)
GPIO.output(yellow,0)
GPIO.output(green,0)
GPIO.cleanup()
    

