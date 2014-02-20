from cv2 import *

# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()


imshow("cam-test",img)
for x in xrange(1,10000000000000):
	x-1
	
#waitKey(0)
#destroyWindow("cam-test")
#imwrite("filename123.jpg",img) #save image