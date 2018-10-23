# Mouse_Contol_using_Hand_Gesture_Recognition_using_Deep_learning_CNN_in_Python
This is my personal projects for self learning.
Hand gesture recognition is very significant for human-computer interaction. With the help of hand gesutre i am try to control the mouse events such as copy, paste, open a file, moving the mouse. The  data set of 100 images of each gesture. Here i have used only 5 gesture to contol my mouse action. Our method performs well and is highly efficient.

## How to run our code

 
1. database - where we save the image for each gesture under particular folder.

2. export_model - folder where we save our predict function.

3. model - folder where we are saving our complete model

4. create_dataset_tfrecords.py - python script will create tfrecords file for the database folder that data will be passed to model. it will create 2 file train_gray.tfrecords and test_gray.tfrecords.

5. model.ipynb - python notebook for creating the cnn model using tensorflow

6. saving_image_database.py - python script to save the image in database folder in proper format

7. testing.py - python script to contol the mouse functionality for testing our save tensorflow model


# Our model accuracy is 98%

## References
## 1. [tensorflow](https://www.tensorflow.org/tutorials/estimators/cnn)
## 2. [tensorbord](https://www.tensorflow.org/guide/summaries_and_tensorboard)
## 3. [pyautogui](https://automatetheboringstuff.com/chapter18/)
