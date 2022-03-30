import Buzz
import QR_Read
import time

def main():

       for i in range (0,9):
                time.sleep(1)

                location =QR_Read.read_qr()
                if location == "Doctor's Office A":
                        Buzz.setup()
                        time.sleep(1)
                        break
if __name__ == '__main__':

	main()
