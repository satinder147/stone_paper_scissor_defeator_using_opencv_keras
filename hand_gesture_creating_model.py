import cv2
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import img_to_array
from keras.utils import to_categorical
import os
import cv2
import numpy as np
import random

bg=None
count=0

#from keras.preprocessing.image import img_to_array

def build(width,height,depth,classes):
    model=Sequential()
        
    input_Shape=(height,width,depth)
    if(K.image_data_format()=="channels_first"):
        input_Shape=(depth,height,width)
    model.add(Conv2D(20,(5,5),padding="same",input_shape=input_Shape))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
    model.add(Conv2D(50,(5,5),padding="same"))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
    model.add(Flatten())
    model.add(Dense(500))
    model.add(Activation("relu"))
    model.add(Dense(classes))
    model.add(Activation("softmax"))
    return model


    
model=build(64,64,1,3)
learning_rate=0.001
epochs=25
bs=32
data=[]
labels=[]
path='C:/Users/satinder/Desktop\desk/New folder/New folder/paper'
f=os.listdir(path)

for a in f:
    img=cv2.imread(path+'/'+a,-1)
    img=cv2.resize(img,(64,64))
    img=img_to_array(img)
    data.append(img)
    labels.append(0)

path='C:/Users/satinder/Desktop\desk/New folder/New folder/scissor'

f=os.listdir(path)
for a in f:
    img=cv2.imread(path+'/'+a,-1)
    img=cv2.resize(img,(64,64))
    img=img_to_array(img)
    data.append(img)
    labels.append(1)
path='C:/Users/satinder/Desktop\desk/New folder/New folder/stone'

f=os.listdir(path)
for a in f:
    img=cv2.imread(path+'/'+a,-1)
    img=cv2.resize(img,(64,64))
    img=img_to_array(img)
    data.append(img)
    labels.append(2)
c=list(zip(data,labels))
random.shuffle(c)
data[:],labels[:]=zip(*c)
print(len(data))
data=np.array(data,dtype="float")/255.0
labels=np.array(labels)
trainX,testX,trainY,testY=train_test_split(data,labels,test_size=0.25,random_state=42)
trainY=to_categorical(trainY,num_classes=3)
testY=to_categorical(testY,num_classes=3)
aug=ImageDataGenerator(rotation_range=30,width_shift_range=0.1,height_shift_range=0.1,shear_range=0.2,zoom_range=0.2,horizontal_flip=True,fill_mode="nearest")
opt=Adam(lr=learning_rate,decay=learning_rate/epochs)
model.compile(loss="categorical_crossentropy",optimizer=opt,metrics=["accuracy"])
h=model.fit_generator(aug.flow(trainX,trainY,batch_size=bs),validation_data=(testX,testY),steps_per_epoch=len(trainX)//bs,epochs=epochs,verbose=1)
model.save("stone.model")


