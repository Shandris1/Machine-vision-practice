import cv2
import numpy as np
from matplotlib import pyplot as plt
camera = cv2.VideoCapture(0)
Vfile = "video.vga"
#import standart libriaries




def main():
  state = 1
  while state != 0:
    state=BlackandWhite()
    print state
    cv2.destroyAllWindows()
    if state==1:
      state=Contours()


        

    cv2.destroyAllWindows()

def AdapriveEdgeDetection():
  while(1):
    img = camera.read()[1] # read from webcam
    img = cv2.medianBlur(img,5)

  pass

def edgedetection():
  while(1):
    img = camera.read()[1] # read from webcam
    edges = cv2.Canny(img,75,100)

    cv2.imshow('Edge detection',edges) # Display to window
    key=cv2.waitKey(5)
    if key==27: #close window on escape
      status=0
      break
    if key==32:
      status=2
      break 
  return status

def BlackandWhite():
  while(1):
    status=0
    im = camera.read()[1] # read from webcam
    im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #convert to BW
    cv2.imshow('BW image2',im_gray) # Display to window
    key=cv2.waitKey(5)
    if key==27: #close window on escape
      status=0
      break
    if key==32:
      status=1
      break 

  return status

def Contours():
  while(1):
    status=0
    im = camera.read()[1] # read from webcam
    im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #convert to BW
    ret,thresh = cv2.threshold(im_gray,127,255,0)
    #print (thresh) 
    #cv2.imshow('BW image2',thresh) # Display to window
    im_contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.drawContours(im, im_contours, -1, (0,255,0), 3)
    cv2.imshow('BW image2',img) # Display to window
    key=cv2.waitKey(5)
    if key==27: #close window on escape
      status=0
      break
    if key==32:
      status=1
      break 
    cv2.destroyAllWindows()


main()
    

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

