# Thresolding is a popular segmentation technique used for seperating an object from its bavkground.
# The process of thresholding involves comparing each pixel of an image with a predefined threshold value. 
# This type of comparision devides all the pixels of the input image into two groups.
# First group involves pixels having intensity value lesser then that threshold value.
# Second group involves pixels having intensity value greater then that threshold value.
# Using different thresholding techniques wecan give different values to these pixels which are higher and lower then the threshold value.


import cv2 as cv
import numpy as np

img = cv.imread('F:\648390_15051915470027597677.jpg',0)
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)


cv.imshow("Image", img)
cv.imshow("th1", th1)
cv.imshow("th2", th2)
cv.imshow("th3", th3)
cv.imshow("th4", th4)
cv.imshow("th5", th5)

cv.waitKey(0)
cv.destroyAllWindows()