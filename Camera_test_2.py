import pygame
import pygame.camera
import os
from PIL import Image
from numpy import *
from pylab import *

def histeq(im,nbr_bins=256):
	#Histogram equalization of a grayscale image
	#get image histogram
	imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
	cdf = imhist.cumsum()
	cdf = 255*cdf / cdf [-1]

	im2= interp(im.flatten(),bins[:-1],cdf)
	return im2.reshape(im.shape), cdf

pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
img = cam.get_raw()
print img


#pygame.image.save(img,"seeds.jpg")

cam.stop()

im = array(Image.open('seeds.jpg').convert('L'))
im2,cdf = histeq(im)
show_picture=Image.fromarray(im2)
print show_picture
imshow(img)
show()