import cv2
import numpy as np

# import test image
img = cv2.imread('test.jpg')
#convert test image to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#import again as greyscale
img = cv2.imread('test.jpg', 0)
img = cv2.medianBlur(img,5)

#
# Resize the image to make it half the size
small = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
small_h = cv2.resize(hsv, (0, 0), fx=0.5, fy=0.5)
#cv2.imshow('small', small)

# Detect Circles
circles = cv2.HoughCircles(small,cv2.HOUGH_GRADIENT,dp = 1,minDist = 100, param1 = 20,param2 = 30, minRadius = 25, maxRadius = 55)



circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(small_h, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(small_h, (i[0], i[1]), 2, (0, 0, 255), 3)

# print how many circles were detected
#print(circles[0][0][0])




#cv2.imshow('detected circles', small_h)

#cv2.waitKey(0)
#cv2.destroyAllWindows()