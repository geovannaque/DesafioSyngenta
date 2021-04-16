# TENTATIVA 3 
# Aplicar máscara HSV para visualizar apenas os pixels verdes na expectaviva de visualizar algum padrão ou figura
import cv2
import numpy as np

image = cv2.imread("Syngenta.bmp")
imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

green = [96, 192, 0]
thresh = 40

hsv = cv2.cvtColor( np.uint8([[green]] ), cv2.COLOR_BGR2HSV)[0][0]

minHSV = np.array([hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh])
maxHSV = np.array([hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh])

maskHSV = cv2.inRange(imageHSV, minHSV, maxHSV)
resultHSV = cv2.bitwise_and(imageHSV, imageHSV, mask = maskHSV)


cv2.imshow("Result HSV", resultHSV)
cv2.waitKey(0)

   