import cv2 


# VARIABLES
##### number of photos to take
num = 5
#####
#### define the type of image file that are saved
typ = '.jpg'
#####




### use for live capture

for idx in range(num):

    current = idx+1 # adjust 

    print('Ready to take picture ' + str(current))
    input("Press Enter to take photo...")

    cam = cv2.VideoCapture(0) #opens up the video capture (video device 0)
    s, im = cam.read() # captures image (im)
    cam.release() # shuts down the camera stream
    cv2.imwrite(str(idx+1)+typ,im) # saves the image
    
    print('Photo taken! :)')



