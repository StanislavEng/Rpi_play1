from smbus import SMBus
from time import sleep

addr = 0x8 # bus address
bus = SMBus(1) #indicates I2C bus 1 in /dev/ic2-1

numb = 1
datSend = 0

while numb == 1:
    print("Do you want to turn on red, blue or yellow LED?")
    whatLED = input(">>> ")

    #if ledstate == "1":
        #bus.write_byte(addr,0x1) # switches it off by sending value of 1
    #elif ledstate == "0":
        #bus.write_byte(addr,0x0) # switches it off by sending value of 0
    #else:
    #    numb = 0

    if whatLED == "red":
#        bus.write_byte(addr,0x1)
        datSend = 0x1
    elif whatLED == "blue":
#        bus.write_byte(addr,0x2)
        datSend = 0x2
    elif whatLED == "yellow":
#        bus.write_byte(addr,0x4)
        datSend = 0x4
    else:
        numb = 0
#    sleep(0.5)
    print("Press 1 to turn ON or 0 to turn OFF ")
    ledstate = input(">>> ")
    if ledstate == "1":
#        bus.write_byte(addr,0x1)
        datSend = (datSend<< 1 ) | 0x1
    else:
#        bus.write_byte(addr,0x0)
        datSend = (datSend<< 1 )
    bus.write_byte(addr,datSend)
    print("You said: ", whatLED, " and ", ledstate)
    print("Your data is: " , datSend)
    
