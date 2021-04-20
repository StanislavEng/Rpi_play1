from time import sleep
import RPi.GPIO as GPIO

bl = 12 # my blue LED
yl = 15 # my yellow LED
b1 = 11 # my button 1
b2 = 16 # my button 2

GPIO.setmode(GPIO.BOARD)

LED = [bl,yl]
button = [b1, b2]
for pin in button: # set up buttons as input
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for pin in LED: # set up LED as output
    GPIO.setup(pin,GPIO.OUT)
    
b1m = False # the memory state of button 1 (was last press for on or off)
b2m = False # the memory state of button 2

try:
    while True:
        if GPIO.input(b1) == 0:
            print ("Button one was pressed")
            b1m = not b1m # changes state of memory
            GPIO.output(bl,b1m) # changes output based on memory state
            sleep(0.5) # gives me time to take finger off
        if GPIO.input(b2) == 0:
            print ("Button two was pressed")
            b2m = not b2m
            GPIO.output(yl,b2m)
            sleep(0.5) # same as other

### tutorial example ###
#         if GPIO.input(b1) == 0:
#             print "Button 1 was pressed"
#             if b1m == False:
#                 GPIO.output(bl, True)
#                 b1m = True:
#                 sleep(0.5)
#             else:
#                 GPIO.output(bl, False)
#                 b1m = False:
#                 sleep(0.5)
#         if GPIO.input(b2) == 0:
#             print "Button 2 was pressed"
#             if b2m == False:
#                 GPIO.output(yl, True)
#                 b2m = True:
#                 sleep(0.5)
#             else:
#                 GPIO.output(yl, False)
#                 b2m = False:
#                 sleep(0.5)

### my initial guess ###
#        if GPIO.input(b1) == 0:
#            GPIO.output(bl,True)
#        else:
#            GPIO.output(bl,False)
#        if GPIO.input(b2) == 0:
#            GPIO.output(yl,True)
#        else:
#            GPIO.output(yl,False
except KeyboardInterrupt:
    GPIO.cleanup()
    