import numpy as np
import cv2

# opencv 2.41 - python 2.73

"""
while key!=(32):
    filename = "seed_test.JPG"
    im_uncropped = cv2.imread(filename)
    im = im_uncropped [SW:EW,SH:EH]
    im = cv2.medianBlur(im,5)
    new = im.copy()

    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,100,255,0) ## determinate objects
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #cv2.imshow("original image",im)
    #print "PULSE TO ANY KEY TO CONTINUE"

    for h,cnt in enumerate(contours):
        if (len(cnt)>5):

            ellipse = cv2.fitEllipse(cnt)
            cv2.ellipse(im,ellipse,(0,255,0),2)
            #key = cv2.waitKey(0)
    
        
        
    label = "silueta  %s " 
    text = (label % (h))
    cv2.imshow(text, im)
    key=cv2.waitKey(5)
    if key==32:
        cv2.destroyAllWindows()
        break
    if key==65364:
        EW=EW+5
        print"SW = ",SW

    if key==65362:
        EW=EW-5
        print"SW = ",SW
    #cv2.destroyAllWindows() ##
"""

def main():
    SW = 0
    EW = 760
    SH = 290
    EH = 800
    key = 0
    while(1):
        SW,EW,SH,EH = GenerateImage(SW,EW,SH,EH)

def GenerateImage(Starting_width,Ending_width,Starting_hight,Ending_hight):

    filename = "seed_test.JPG"
    im_uncropped = cv2.imread(filename)
    im = im_uncropped [Starting_width:Ending_width,Starting_hight:Ending_hight]



    #im = cv2.medianBlur(im,3)
    new = im.copy()

    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,100,255,0) ## determinate objects
    kernel= np.ones((3,3),np.uint8)
    thresh = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel)
    thresh = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)
    #cv2.imshow("Image/BW",thresh)

    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #cv2.imshow("original image",im)
    #print "PULSE TO ANY KEY TO CONTINUE"
    cv2.drawContours( im,contours,-1,(0,255,0),5)  
    cv2.imshow("partitioned window", im)

    for h,cnt in enumerate(contours):
        if (len(cnt)>5):
            Carea=cv2.contourArea(cnt)
            #print(Carea)
            if(Carea>100)&(Carea<1500):

                mask = np.zeros(imgray.shape,np.uint8)
                color = cv2.mean(im,mask = mask)
                ellipse = cv2.fitEllipse(cnt)
                cv2.ellipse(im,ellipse,(0,255,255),2)
    key=cv2.waitKey(5)
    if key==32:
        cv2.destroyAllWindows()
        exit(0)
    if key==65364:
        Starting_hight=Starting_hight+5
        print"Starting_hight = ",Starting_hight

    if key==65362:
        Starting_hight=Starting_hight-5
        print"Starting_hight = ",Starting_hight
    cv2.imshow("Image",im)
    if key==65363:
        Ending_hight=Ending_hight+5
        print"Ending_hight = ",Ending_hight

    if key==65361:
        Ending_hight=Ending_hight-5
        print"Ending_hight = ",Ending_hight
    cv2.imshow("Image",im)
    return (Starting_width,Ending_width,Starting_hight,Ending_hight)

main()