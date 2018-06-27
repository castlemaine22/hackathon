
import cv2 
from josie import circles
from josie import small_h


#
#c = [100,100,200] 

#### how many pixels are added onto the perimeter
perim = 20

#### define the type of image file that are saved
typ = '.jpg'

# process the info from the Josie script

# reference the hsv
im = small_h

#extract the data container from the array to make code cleaner
data = circles[0]



### use for live capture

#cam = cv2.VideoCapture(0) #opens up the video capture (video device 0)
#s, im = cam.read() # captures image (im)
#cam.release()

### use for importing image

#im = cv2.imread('test.jpg')

#### debug script
#cv2.imshow("Test Picture", im) # displays captured image
#cv2.waitKey(0)



height, width = im.shape[:2] # retrieves the size of the image imported

#### debug script
print(width,height)

# function to prevent the perimiter adjustment going below 0
def low_limit(xy):
    if xy < 0:
        return 0
    else:
        return xy 

# function to prevent the perimiter adjustment going above the height
def hight_limit(xy,height):
    if xy > height:
        
        return height -1
    else:
        
        return xy 

# function to prevent the perimiter adjustment going above the width
def width_limit(xy,width):
    if xy > width:
        
        return width -1
        
    else:
       
        return xy 
        



for idx in range(1): #for each circle detected

    #extract the coordinate data for that particular circle
    x = data[idx][0]
    y = data[idx][1]
    r = data[idx][2]
    print(x,y,r)

    # set the coordinates for the crop around the beet. Square crop around the centre point, dimesions are
    # the diameter plus a bonus perimiter
    x1 = low_limit(int(x-r-perim))
    x2 = width_limit(int(x+r+perim),width)
    y1 = low_limit(int(y-r-perim))
    y2 = hight_limit(int(y+r+perim),height)

    #### debug script
    print(x1,x2,y1,y2)


    img2 = im[y1:y2, x1:x2] # crops the image

    cv2.imwrite(str(idx)+typ,img2) # saves the image

    ### debug test
    #cv2.imshow(str(idx), img2) #shows the image
    #cv2.waitKey(0) # wait
    