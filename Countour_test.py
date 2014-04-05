import numpy as np
import cv2
from matplotlib import pyplot as plt
camera = cv2.VideoCapture(0)
Vfile = "video.vga"

# opencv 2.41 - python 2.73

#im = camera.read()[1] # read from webcam
filename = "seed_test.JPG" 
im = cv2.imread(filename)
new = im.copy()

threshold_value=100

while(1):
    im_live = camera.read()[1] # read from webcam
    im_live = cv2.medianBlur(im_live,5)
    im_gray_live = cv2.cvtColor(im_live,cv2.COLOR_BGR2GRAY)
    ret,im_BW_live = cv2.threshold(im_gray_live,threshold_value,255,0) #convert to BW
    #th3 = cv2.adaptiveThreshold(im_live,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,2)
    cv2.imshow('BW image2',im_BW_live) # Display to window
    #cv2.imshow('adaptiveThreshold',th3)
    key=cv2.waitKey(5)
    if key==32:
        cv2.destroyAllWindows()
        break
    if key==65364:
        threshold_value=threshold_value+5
    if key==65362:
        threshold_value=threshold_value-5

# new_image = old_image [heght:end_heght,width:end_width]

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,threshold_value,255,0) ## determinate objects
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
single_contour= contours [10]
ellipse = cv2.fitEllipse(single_contour)
cv2.ellipse(im,ellipse,(0,255,0),2)
cv2.imshow("ellipse",im)


cv2.imshow("original image",thresh)
print "PULSE TO ANY KEY TO CONTINUE"
print "threshold_value = ",threshold_value

#cv2.drawContours( im,contours,-1,(0,255,0),5)  
cv2.imshow("partitioned window", im)

# for h,cnt in enumerate(contours):
    
#     mask = np.zeros(imgray.shape,np.uint8)
#     cv2.drawContours(mask,[cnt],0,255,-1)   
#     mean = cv2.mean(im,mask = mask) # calculate figure color

#     key = cv2.waitKey(0)
    
#     label = "silueta  %s "
#     text = (label % (h))
#     cv2.imshow(text, mask)
   
#     maskc = cv2.cvtColor(mask,cv2.COLOR_GRAY2RGB)
#     label2 = "figura  %s "
#     text2 = (label2 % (h))
#     cv2.drawContours(maskc,[cnt],0,mean,-1)
#     cv2.imshow(text2, maskc)   

cv2.waitKey(0) ## Wait for keystroke
cv2.destroyAllWindows()