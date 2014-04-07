import cv2
import numpy as np
 


SW = 0
EW = 760
SH = 290
EH = 800
img = cv2.imread('seed_test.JPG')
#img = im_uncropped [SW:EW,SH:EH]

 

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,img = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
kernel= np.ones((3,3),np.uint8)
img = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
img = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
cv2.imshow("image",img)
size = np.size(img)
skel = np.zeros(img.shape,np.uint8)
element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
done = False
 
while( not done):
    eroded = cv2.erode(img,element)
    temp = cv2.dilate(eroded,element)
    temp = cv2.subtract(img,temp)
    skel = cv2.bitwise_or(skel,temp)
    img = eroded.copy()
 
    zeros = size - cv2.countNonZero(img)
    if zeros==size:
        done = True
 

#for i in range(0,1):
#	kernel= np.ones((2,2),np.uint8)
#	skel = cv2.morphologyEx(skel,cv2.MORPH_CLOSE,kernel)
#	skel = cv2.morphologyEx(skel,cv2.MORPH_OPEN,kernel)
cv2.imshow("skel",skel)



cv2.waitKey(0)
cv2.destroyAllWindows()