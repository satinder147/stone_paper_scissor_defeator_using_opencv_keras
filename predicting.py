##satinder singh
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import cv2
import serial
ser=serial.Serial('COM9',9600,timeout=1)
flag=None
def stoney():
    ser.write(b'1')
    data=ser.readline().decode('ascii')
    return data
def papery():
    ser.write(b'2')
    data=ser.readline().decode('ascii')
    return data
def scissory():
    ser.write(b'3')
    data=ser.readline().decode('ascii')
    return data
bg=None
count=0
model=load_model('stone.model')
print('model loaded')
cap=cv2.VideoCapture(1)
while True:
    frame=cap.read()[1]
    if(count==0):
        bg=frame.copy().astype('float')
        count=count+1
    elif(count<30):
        cv2.accumulateWeighted(frame,bg,0.05)
        count=count+1
    elif(count>29):
        #print('bg caliberation done')
        diff=cv2.absdiff(frame,bg.astype('uint8'))
        
        diff=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
        diff=cv2.threshold(diff,30,255,cv2.THRESH_BINARY)[1]
        diff=cv2.erode(diff,None,iterations=2)
        diff=cv2.dilate(diff,None,iterations=2)
        grey=diff

        
        
        diff=cv2.resize(diff,(64,64))
        diff=diff.astype('float')/255.0
        diff=img_to_array(diff)
        diff=np.expand_dims(diff,axis=0)
        prob=0
        (hand,scissor,stone)=model.predict(diff)[0]
        #print(hand,scissor,stone)
        if(hand>stone and hand>scissor):
            label='hand'
            prob=hand
            
            print(scissory())
            
        elif(stone>hand and stone>scissor):
            label='stone'
            prob=stone
            print(papery())
        else:
            label='scissor'
            prob=scissor
            print(stoney())
        #print(prob)
        cv2.putText(frame,label+str(prob),(10,25),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
        cv2.imshow('frame',frame)
        cv2.imshow('bg',grey)
        if(cv2.waitKey(1)&0XFF==ord('q')):
            break
cap.release()
cv2.destroyAllWindows()
