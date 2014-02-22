import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()




class Capture(object):
    def calibrate(self):
        # capture the image
        self.snapshot = self.cam.get_image(self.snapshot)
        # blit it to the display surface
        self.display.blit(self.snapshot, (0,0))
        # make a rect in the middle of the screen
        crect = pygame.draw.rect(self.display, (255,0,0), (320,240,10,10), 4)
        # get the average color of the area inside the rect
        self.ccolor = pygame.transform.average_color(self.snapshot, crect)
        # fill the upper left corner with that color
        self.display.fill(self.ccolor, (0,0,50,50))
        pygame.display.flip()

    def __init__(self):
        self.size = (640,480)
        # create a display surface. standard pygame stuff
        self.display = pygame.display.set_mode(self.size, 0)
        
        # this is the same as what we saw before
        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        self.cam = pygame.camera.Camera(self.clist[0], self.size, "RGB")
        self.cam.start()

        # create a surface to capture to.  for performance purposes
        # bit depth is the same as that of the display surface.
        self.snapshot = pygame.surface.Surface(self.size, 0, self.display)
        self.thresholded = pygame.surface.Surface(self.size, 0, self.display)

    def get_and_flip(self):
        # if you don't want to tie the framerate to the camera, you can check 
        # if the camera has an image ready.  note that while this works
        # on most cameras, some will never return true.
        if self.cam.query_image():
            self.snapshot = self.cam.get_image(self.snapshot)
            #pygame.transform.threshold(self.thresholded,self.snapshot,self.ccolor,(30,30,30),(0,0,0),2)
            self.thresholded = pygame.transform.laplacian(self.snapshot)
            #bpygame.transform.threshold(self.thresholded,self.snapshot,(0,255,0),(90,170,170),(0,0,0),2)


        # blit it to the display surface.  simple!
        self.display.blit(self.thresholded, (0,0))

        

        pygame.display.flip()

    

    def main(self):
        going = True
        going2 = True

        while going:
            self.calibrate()
            events = pygame.event.get()

            for e in events:
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_SPACE):
                    # close the camera safely
                    
                    going = False
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    # close the camera safely
                    self.cam.stop()
                    going = False
                    return

        going = True                
        while going:
            events = pygame.event.get()

            for e in events:
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    # close the camera safely
                    self.cam.stop()
                    going = False
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_SPACE):
                    # close the camera safely
                    self.cam.stop()
                    take_picture = Capture().main()

            events = pygame.event.get()

            self.get_and_flip()




take_picture = Capture().main()
