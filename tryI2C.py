from smbus import SMBus

addr = 0x8 # bus address
bus = SMBus(1) #indicates I2C bus 1 in /dev/ic2-1

numb = 1

print("Enter 1 for ON or 0 for OFF")
try:
	while numb == 1:
		ledstate = input(">>> ")

		if ledstate == "1":
			bus.write_byte(addr,0x1) # switches it off by sending value of 1
		elif ledstate == "0":
			bus.write_byte(addr,0x0) # switches it off by sending value of 0
		else:
			numb = 0


except KeyboardInterrupt:
	GPIO.cleanup()