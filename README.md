# Mouse_Contol_using_Hand_Gesture_Recognition_using_Deep_learning_CNN_in_Python
This is our personal projects for self learning.
Hand gesture is user friendly interface technique for human-computer interaction. With the help of hand gesutre we tried to control the mouse events such as copy, paste, open a file, moving the mouse. The  data set contains 100 images of each gesture. Here we have used only 5 gesture to contol mouse events. Our method performs well and is highly efficient.

<p align="center"> *************************************************************************************************************************************</p>

<div align="center"><img src ="https://github.com/Michigan10/Mouse_Contol_using_Hand_Gesture_Recognition_using_Deep_learning_CNN_in_Python/blob/master/hand_gesture_image.png"  width="791" height="626" /></div>

<p align="center"> *************************************************************************************************************************************</p>

## How to run our code

1. database - where we save the image for each gesture under particular folder.

2. export_model - folder where we save our predict function.

3. model - folder where we are saving our complete model

4. create_dataset_tfrecords.py - python script will create tfrecords file for the database folder that data will be passed to model. It will create 2 file train_gray.tfrecords and test_gray.tfrecords.

5. model.ipynb - python notebook for creating the cnn model using tensorflow

6. saving_image_database.py - python script to save the image in database folder in proper format

7. testing.py - python script to contol the mouse functionality for testing our save tensorflow model


## Our model accuracy is 98.25%

## References
## 1. [tensorflow](https://www.tensorflow.org/tutorials/estimators/cnn)
## 2. [tensorbord](https://www.tensorflow.org/guide/summaries_and_tensorboard)
## 3. [pyautogui](https://automatetheboringstuff.com/chapter18/)
<p align="center"> *************************************************************************************************************************************</p>

<div align="center"><img src ="https://github.com/Michigan10/Mouse_Contol_using_Hand_Gesture_Recognition_using_Deep_learning_CNN_in_Python/blob/master/loss_image.png"  width="507" height="354" /></div>
