from PIL import Image
from numpy import *


def main():
	Graylevel_transform("download.jpg")

def Graylevel_transform(image_path):
	im= array(Image.open(image_path).convert('L'))
	
	im2 = 255 - im # invert image

	im3 = (100.0/255)* im + 100 #clamp to inverval 100...200

	im4 = 255.0 * (im/255.0)**2 #squared

	print int(im.min()), int(im.max())
	return
	
def Array_image_representation(image_path):
	im = array (Image.open(image_path))
	print im.shape, im.dtype
	im = array (Image.open(image_path).convert('L'),'F')
	print im,shape, im.dtype
	return

main()