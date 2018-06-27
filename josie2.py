import cv2
import numpy as np

img = cv2.imread('img.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

img = cv2.imread('img.jpg', 0)
img = cv2.medianBlur(img,5)


# Resize the image to make it half the size
small = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
small_h = cv2.resize(hsv, (0, 0), fx=0.5, fy=0.5)
cv2.imshow('small', small)

# Detect Circles
circles = cv2.HoughCircles(small,cv2.HOUGH_GRADIENT,dp = 1,minDist = 100, param1 = 20,param2 = 30, minRadius = 25, maxRadius = 55)

circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # draw the outer circle
    #cv2.circle(small_h, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle

    crop_img = small_h[i[1] - i[2] - 10:i[1] + i[2] - 10, i[0] - i[2] - 10:i[0] + i[2] - 10]

    avg_color_per_row = np.average(crop_img, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)  # Blue, Green, Red
    print(avg_color)

    if(i[2]<35):
        print('Too Small')
        #cv2.circle(small, (i[0], i[1]), i[2], (0, 255, 255), 2)
        cv2.circle(small, (i[0], i[1]), 2, (0, 0, 255), 3)
        cv2.putText(small, "Too Small", (i[0], i[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 0)
    elif(avg_color[0]>135):
        cv2.circle(small, (i[0], i[1]), 2, (0, 0, 255), 3)
        cv2.putText(small, "Marks", (i[0], i[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 0)
    else:
        print('Correct Size')
        cv2.circle(small, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(small, (i[0], i[1]), 2, (0, 0, 255), 3)


cv2.imshow('detected circles', small)
cv2.waitKey(0)
cv2.destroyAllWindows()
