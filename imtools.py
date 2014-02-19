import os
from PIL import Image

def main():
	infile = "download.jpg"
	outfile = os.path.splitext(infile)[0] + "M.jpg"

	pil_im = Image.open('download.jpg')
	print pil_im


	#pil_im.thumbnail((128,128))

	pil_im = Resize_rotate(pil_im)
	print pil_im
	pil_im.save(outfile)
	open(outfile)

def copy_paste_region(path):
	box = (50,50,110,110)
	region = path.crop(box)
	region = region.transpose(Image.ROTATE_180)
	path.paste(region,box)
	return (path)

def Resize_rotate(path):
	out1 = path.resize((128,128))
	out2 = out1.rotate(45)
	return (out2)

def get_imlist(path):
	###***Returns a list of filenames for all jpg images in a directory***
	return [os.path.john(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

def imresize(im,sz):
	# Resize an image array using PIL
	pil_im = Image.fromarray(uint8(im))

	return array(pil_im.resize(sz))

def compute_averege(imlist):
	#compute the average of tha list of images

	#open first image and make into array of type float
	averageim= array(Image.open(imlist[0]),'f')

	for imname in imlist[1:]:
		try:
			averageim += array(Image.open(imname))
		except:
			print imname + '...skipped'
	averageim /=len(imlist)

	#return average as uint8
	return array(averageim,'uint8')
	pass

main()

