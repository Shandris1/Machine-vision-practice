import cv2
import numpy as np
camera = cv2.VideoCapture(0)
#import standart libriaries


while(1):
    im = camera.read()[1]
    im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    cv2.imshow('BW image2',im_gray)
    if cv2.waitKey(5)==27:
        break
cv2.destroyAllWindows()
    

"""
import VideoCapture as VC
from PIL import Image
from PIL import ImageOps
import time

def capture_image():
  cam = VC.Device() # initialize the webcam
  img = cam.getImage() # in my testing the first getImage stays black.
  time.sleep(1) # give sometime for the device to come up
  img = cam.getImage() # capture the current image
  del cam # no longer need the cam. uninitialize
  return img

if __name__=="__main__":  
  img = capture_image()

  # use ImageOps to convert to grayscale.
  # show() saves the image to disk and opens the image.
  # you can also take a look at Image.save() method to write image to disk.
  ImageOps.grayscale(img).show()
"""
"""
import cv2
import numpy
from numpy import *


cap=cv2.VideoCapture(0)

frames = []
while True:
	ret,im = cap.read()
	cv2.imshow('video',im)
	frames.append(im)
	if cv2.waitKey(10) ==27:
		break
	frames = [frames]

	#print im
	print frames
"""




















"""
import cv2


# Camera 0 is the integrated web cam on my netbook
camera=cv2.VideoCapture(0)
im = camera.read()[1]

cv2.imshow("this window will not pop up", im)
cv2.imwrite("test0previous0image0here.jpg",im)
"""

