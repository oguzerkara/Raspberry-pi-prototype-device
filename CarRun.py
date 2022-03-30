import YB_Pcb_Car
import time
import pygame

pygame.init()
win = pygame.display.set_mode((100,100))


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

	    car = YB_Pcb_Car.YB_Pcb_Car()
	    car.Car_Run(150,150)
	    time.sleep(0.5)
	    car.Car_Stop()
	    car.Car_Spin_Left(150,150)
	    time.sleep(0.5)
	    car.Car_Stop()
	    car.Car_Run(150,150)
	    time.sleep(2)
	    car.Car_Stop()
	    car.Car_Run(50,250)
	    time.sleep(1.2)
	    car.Car_Stop()
	    car.Car_Spin_Left(150,150)
	    time.sleep(1)
	    car.Car_Stop()

if __name__ == '__main__':
	
	 if getKey('UP'):
	    car.Car_Stop()
	 else:
	    main()
