from PIL import Image
from pylab import *

def main():
	intaractive_animation("pictures/download.jpg")
	

def intaractive_animation(image_path):
	im = array(Image.open(image_path))
	imshow(im)
	print "please click 4 points"
	x = ginput(4)
	print "youclicked:",x
	show()
	pass

def histogram(image_path):
	#read image to array
	im = array(Image.open(image_path).convert('L'))

	#create new figure
	figure()
	#dont use colours
	gray()
	#show countours with orinin upper left corner
	contour(im, origin='image')
	axis('equal')
	axis('off')
	figure()
	hist(im.flatten(),128)
	show()
	return

def plot_graph(image_path):

	#read image to array

	im = array(Image.open(image_path))

	#plot the image
	imshow(im)

	#some points
	x = [100,100,400,400]
	y = [200,500,200,500]

	#plot the points with red star-markers
	plot(x,y,'r*')

	#line plot connecting the first two points
	plot(x[:2],y[:2])

	#add a title and show the plot 
	title('plotting: empire.jpg')
	axis('off')
	show()
	return


main()