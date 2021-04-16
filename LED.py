import RPi.GPIO as GPIO
import time

green = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(green,GPIO.OUT)

blink_num = input("How many times do you want to blink?")
#while True:
for i in (0,blink_num):
	GPIO.output(green, True)
	time.sleep(1)
	GPIO.output(green,False)
	time.sleep(1)
GPIO.cleanup()
