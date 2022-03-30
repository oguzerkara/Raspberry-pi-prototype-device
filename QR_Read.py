import cv2
import numpy as np
from pyzbar.pyzbar import decode

def read_qr():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # Width
    cap.set(4, 480)  # Height
    global my_data
    my_data = "x"
    location = "Last location"  # last known location
    while True:
        success, img = cap.read()
        print("Current Location: ", location)
        for barcode in decode(img):
            # print(barcode.data)
            my_data = barcode.data.decode('utf-8')
            print(my_data)
            #  Polygon to draw rectangle
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1,1,2))
            cv2.polylines(img,[pts],True,(255,0,0),5)
            pts2 = barcode.rect
            cv2.putText(img,my_data,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,255,0),2)

            if my_data == "Doctor's Office A":
                location = "Doctor's Office A"

            if my_data == "Room B":
                location = "Room B"

            if my_data == "Charging Station C":
                location = "Charging Station C"

        cv2.imshow('Result', img)
#        return (location)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
	

if __name__ == '__main__':
    read_qr()


