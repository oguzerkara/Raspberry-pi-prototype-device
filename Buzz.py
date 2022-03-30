import RPi.GPIO as GPIO
import time

Buzzer = 32

BL1 = 248
BL2 = 278
BL3 = 294
BL4 = 330
BL5 = 371
BL6 = 416
BL7 = 476

B1 =495
B2 =556
B3 = 624
B4 = 661
B5 = 742
B6 = 833
B7 = 935

BH1 = 990
BH2 = 1112
BH3 = 1178
BH4 = 1322
BH5 = 1484
BH6 = 1665
BH7 = 1869

#tune = [BL1,BL2,BL3,BL4,BL5,BL6,BL7,B1,B2,B3,B4,B5,B6,B7,BH1,BH2,BH3,BH4,BH5,BH6,BH7]
tune = [B1,B2,B5,B1,B2,B5,B1,B2,B5,B1]
#durt =[0.5,0.5,1.5,0.5,0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,0.5,0.5,2,0.5,0.5,1,0.5,0.5,0.5,0.5,0.5,1,0.5,
#0.5,0.5,1,0.5,0.5,0.5,0.5,0.5,0.5,2,0.5,1,0.5,0.5 ]
durt = [1,1,1,0.75,0.75,0.75,0.5,0.5,0.5,0.25]
def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(Buzzer,GPIO.OUT)
	global Buzz
	Buzz = GPIO.PWM(Buzzer,440)
	Buzz.start(50)
#def loop():
	print ('\n You arrived')
	for i in range (1,len(tune)):
		Buzz.ChangeFrequency(tune[i])
		time.sleep(durt[i]*0.5)

if  __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		GPIO.cleanup()
		print("Ending")
