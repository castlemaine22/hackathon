
import cv2 
import numpy as np
from josie import circles
from josie import small_h


#### how many pixels are added onto the perimeter
perim = 15

#### define the type of image file that are saved
typ = '.jpg'

# process the info from the Josie script

# reference the hsv
im = small_h

#extract the data container from the array to make code cleaner
data = circles[0]
print(data)


#### debug script
#cv2.imshow("Test Picture", im) # displays captured image
#cv2.waitKey(0)



height, width = im.shape[:2] # retrieves the size of the image imported

#### debug script
#print(width,height)

# function to prevent the values going below 0
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
        


# function to prevent below zero #### DUPLICATE TO integrate
def zerotest(num):
    if num < 0:
        return 0
    else:
        return num


### COLOUR REGION 
target = [135, 110, 10]  # RGB target colour of bad region
diff = 50 # threshold around the target value that will be regarded as bad
boundaries = [([zerotest(target[2]-diff), zerotest(target[1]-diff), zerotest(target[0]-diff)],
               [zerotest(target[2]+diff), zerotest(target[1]+diff), zerotest(target[0]+diff)])]
               # boundaries of colour
 #in order BGR as opencv represents images as numpy arrays in reverse order

#print(boundaries)


master = []


for idx in range(len(data)): #for each circle detected

    #extract the coordinate data for that particular circle
    x = data[idx][0]
    y = data[idx][1]
    r = data[idx][2]
    #print(x,y,r)

    # set the coordinates for the crop around the beet. Square crop around the centre point, dimesions are
    # the diameter plus a bonus perimiter
    x1 = low_limit(int(x-r-perim))
    x2 = width_limit(int(x+r+perim),width)
    y1 = low_limit(int(y-r-perim))
    y2 = hight_limit(int(y+r+perim),height)

    #### debug script
    #print(x1,x2,y1,y2)


    img2 = im[y1:y2, x1:x2] # crops the image

    cv2.imwrite('single_cropped'+str(idx)+typ,img2) # saves the image


    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype=np.uint8) #convert
        upper = np.array(upper, dtype=np.uint8) #convert
        mask = cv2.inRange(img2, lower, upper) 
        output = cv2.bitwise_and(img2, img2, mask=mask)#

        ratio_target = cv2.countNonZero(mask)/(img2.size/3)
        print(str(idx),' target pixel percentage:', np.round(ratio_target*100, 2))
        #np.append(data[idx],(np.round(ratio_target*100, 2)))

        cv2.imwrite('single_filter'+str(idx)+typ,np.hstack([img2, output])) # saves the image
        
    _temp = [data[idx],np.round(ratio_target*100, 2)]
    master.append(_temp)
    

    ### debug test
    #cv2.imshow(str(idx), img2) #shows the image
    #cv2.waitKey(0) # wait

print(master)
    