from random import shuffle
import sys
import cv2
import os
import tensorflow as tf


def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def load_image(addr):
    # loading the image
    img = cv2.imread(addr)
    # converting to gray scale image
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    value = (35, 35)
    blurred = cv2.GaussianBlur(grey, value, 0)
    _, thresh1 = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # normalizing the data
    thresh1 = thresh1/255
    if img is None:
        return None
    return thresh1


def createDataRecord(out_filename, addrs, labels):
    # open the TFRecords file
    writer = tf.python_io.TFRecordWriter(out_filename)
    for i in range(len(addrs)):
        # print how many images are saved every 1000 images
        if not i % 10:
            print('Train data: {}/{}'.format(i, len(addrs)))
            sys.stdout.flush()
        # Load the image
        img = load_image(addrs[i])

        label = labels[i]

        if img is None:
            continue

        # Create a feature
        feature = {
            'image_raw': _bytes_feature(img.tostring()),
            'label': _int64_feature(label)
        }
        # Create an example protocol buffer
        example = tf.train.Example(features=tf.train.Features(feature=feature))

        # Serialize to string and write on the file
        writer.write(example.SerializeToString())

    writer.close()
    sys.stdout.flush()


train_path = '.\\database\\'
name_id = 0
names = {}
addrs = []
labels = []


# finding the files that end with png or jpg and adding then to features after doing some processing
for root, dirs, files in os.walk(train_path):
    for file in files:
        if file.endswith(".jpg") or file.endswith(".png"):
            path = os.path.join(root,file)
            name = os.path.basename(root).replace(" ","_").lower()
            if name not in list(names.keys()):
                names[name] = name_id
                name_id += 1
            addrs.append(path)
            labels.append(names[name])

print(addrs)
print(labels)
# to shuffle data
c = list(zip(addrs, labels))
shuffle(c)
addrs, labels = zip(*c)


# Divide the data into 90% train, 10% test
train_addrs = addrs[0:int(0.9 * len(addrs))]
train_labels = labels[0:int(0.9 * len(labels))]
test_addrs = addrs[int(0.9 * len(addrs)):]
test_labels = labels[int(0.9 * len(labels)):]

# creating data file train and test
createDataRecord('train_gray1.tfrecords', train_addrs, train_labels)
createDataRecord('test_gray1.tfrecords', test_addrs, test_labels)