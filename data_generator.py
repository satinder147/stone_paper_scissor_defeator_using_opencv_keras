import cv2
from pygame import mixer
import time
import numpy as np
pic=0
cap=cv2.VideoCapture(1)
count=0
li=[]
bg=None
while True:
    ret,frame=cap.read()
    #cv2.waitKey(5)
    if(count==0):
        bg=frame.copy().astype("float")
        count=count+1
    elif(count<30):
        cv2.accumulateWeighted(frame,bg,0.5)
        count=count=count+1
    else:
        diff=cv2.absdiff(frame,bg.astype("uint8"))
        diff=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
        thre,diff=cv2.threshold(diff,25,255,cv2.THRESH_BINARY,cv2.THRESH_OTSU)
        diff=cv2.dilate(diff,None,iterations=2)
        diff=cv2.erode(diff,None,iterations=2)
        
        #im,contours,heirarchy=cv2.findContours(diff,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #diff=cv2.cvtColor(diff,cv2.COLOR_GRAY2BGR)

        
        cv2.imshow('frame',diff)
        pic=pic+1
        i=str(pic)
        cv2.imwrite(i+".jpg",diff)
        if(cv2.waitKey(1)&0XFF==ord('q')):
            break
            
            
            

            
cv2.destroyAllWindows()
cap.release()
