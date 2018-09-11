# stone_paper_scissor_defeator_using_opencv_keras
In this repository i tried to replicate a cool project by a japanese scientist who made a machine which had 100 % accuracy in defeating humans in the game of stone-paper and scissors using convolutional neural networks and computer vision
i have used opencv for computer vision and keras for CNNS
link to video tutorial https://www.youtube.com/watch?v=ecSDKWkktOw

### Requirements
0. Python 3.x
1. <a href="https://tensorflow.org">Tensorflow 1.5</a>
2. <a href="https://keras.io">Keras</a>
3. OpenCV 3.4(for loading,resizing images)
4. h5py(for saving trained model)
5. pyttsx3
6. A good grasp over convolutional neural networks. For online resources refer to standford cs231n, deeplearning.ai on coursera or cs231n by standford university
7. A good CPU (preferably with a GPU).
8. Time
9. datetime
10. Patience.... A lot of it.

## Installing the requirements
1. Start your terminal of cmd depending on your os.
  2. If you have a NVidia GPU then make sure you have the prerequisites for Tensorflow GPU installation (Refer to official site). Then use this commmand

    pip install -r requirements_gpu.txt

  3. In case you do not have a GPU then use this command

    pip install -r requirements_cpu.txt

## Steps for making your own trainig data
Place the camera and don't move it, As soon as the camera starts, perform only one gesture at a time, the numberred images of this gesture will be stored in the root directory(you can modify the code append the path to which ever directory you want)
Gather data for all the classes in the similar way

## Training your own classifier
I used my own laptop for training puproses but you can use aws, google collab, azure ........
For training<br> 
1)Modify the path of the stone,paper and scissor folder in hand_gesture_creating_model.py <br>
2)Run hand_gesture_creating_model.py <br>
After the model is trained you are ready to run it.

## Running the trained model
1)Modify the path to the model file in predicting.py<br>
2)Run predicting.py

Congratulations you just made your very own MAN defeating machine.<br>


## Liked it
Give the repository a star if you really liked  it.<br>
if you have any doubts, you can comment them under my youtube video or you can post your doubts on my facebook page 
<a href="https://www.facebook.com/reactorscience/">REACTOR SCIENCE</a>
<br> 
Thank you
