import YB_Pcb_Car
import time
import pygame
import curses
import Ultrasonic

pygame.init()
win = pygame.display.set_mode((100,100))
car = YB_Pcb_Car.YB_Pcb_Car()

car.Car_Run(150,150)
time.sleep(0.2)
car.Car_Stop()

def getKey(keyName):

	ans = False
	for eve in pygame.event.get():pass
	keyInput = pygame.key.get_pressed()
	myKey = getattr(pygame,'K_{}'.format(keyName))
	if keyInput [myKey]:
		ans = True
	pygame.display.update()
	return ans
def main():
	if getKey('UP'):
		car.Car_Run(150, 150)
	elif getKey('DOWN'):
		car.Car_Back(150, 150)
	elif getKey('LEFT'):
		car.Car_Run(0, 250)
	elif getKey('RIGHT'):
		car.Car_Spin_Right(150,150)
	else:
		car.Car_Stop()
		
if __name__ == '__main__':
	while True:
		dist=Ultrasonic.Distance()
		if dist <= 10.0:
			if getKey('DOWN'):
				car.Car_Back(150,150)
			else:
				car.Car_Stop()
		else:
	 		main()
