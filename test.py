import p5 as p
import numpy as np
import cv2 as cv

def setup():
    p.size(800,600)
    
def show(img):
    cv.imshow('cv',img)    
    if cv.waitKey(1)==27:
        exit()

def draw():
    p.background(0)
    
    p.rect((100,200),20,30)
    arr=np.zeros((600,800))
    arr[200:230,100:120]=255
    
    show(arr)
    
p.run()