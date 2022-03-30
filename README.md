# Raspbot


This project is a prototype of an autonomous wheelchair for elderly and disabled people, which also uses green energy from solar panels. The project is divided into 3 sub groups.

This part of mine is about organizing and designing the device input and outputs so that the device could move properly.

The actual device has assisting sub-codes for device to process the camera input data and learn the movement, also, decide which way to go. Because the algorithm mentioned as decide system was not my part I only include the codes used in device's I/O interaction system.

In this part that I am responsible from the device is introduced as it can go in the given directions. It can also use camera for video, buzzer, and QR codes.

The movement codes are supplied from the Internet because the robot is using I2C protocol chip integrated on device board. The movement script is called YB_Pcb_Car. 

