import numpy as np
import cv2


img = cv2.imread('Syngenta.bmp')

with open('rbgs_dos_pixels.txt','w') as arquivo:
    for x in range (1,420):
        for y in range (1,300):
            pixel = img[x,y]
            print(pixel, file=arquivo) 