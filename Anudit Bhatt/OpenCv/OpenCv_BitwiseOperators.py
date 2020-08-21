#Bitwise operations are useful while working with masks. 
#Masks are binary images that indicates the pixel in which the operation is to be performed.

import cv2
import numpy as np


img1 = np.zeros((250, 500, 3), np.uint8) #This will create a black image with the same dimension as img2

#This will create a white rectangle inside the black image that we got from above code

img1 = cv2.rectangle(img1,(200, 0), (300, 100), (255, 255, 255), -1) #(255, 255, 255) is used to indicate white color and -1 is the thickness 
img2 = cv2.imread("image_1.png")

bitAnd = cv2.bitwise_and(img2, img1) #Works on the logic of AND GATE......only 1   1   =   1 rest all of'em becomes 0
bitOr = cv2.bitwise_or(img2, img1) #Works on the logic of OR GATE......only 0   0   =   0 rest all of'em becomes 1
bitXor = cv2.bitwise_xor(img1, img2) #Works on the logic of XOR GATE......only 1   1   =   0    and 0   0  = 0 rest all of'em becomes 1
bitNot1 = cv2.bitwise_not(img1) #Works on the logic of Not GATE...... If the input is 0 output is 1 and vice versa
bitNot2 = cv2.bitwise_not(img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow('bitAnd', bitAnd)
cv2.imshow('bitOr', bitOr)
cv2.imshow('bitXor', bitXor)
cv2.imshow('bitNot1', bitNot1)
cv2.imshow('bitNot2', bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()