import numpy as np
import cv2

img = cv2.imread('img.jpg')
small = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
#cv2.imshow('small', img)


imgray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
imh= cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
ret, thresh = cv2.threshold(imgray, 140, 255, 0)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(small, contours, -1, (0,255,0), 3)


# Use thresholding to get the circles
circles = cv2.HoughCircles(thresh,cv2.HOUGH_GRADIENT,dp = 1,minDist = 100, param1 = 20,param2 = 30, minRadius = 25, maxRadius = 55)
print(circles)
cv2.imshow('img2', thresh)
print('here')
cv2.waitKey(0)
cv2.destroyAllWindows()
