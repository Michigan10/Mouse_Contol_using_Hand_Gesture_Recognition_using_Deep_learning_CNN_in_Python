import cv2
import time
import os

# create database for storing the image
fileDir = os.path.dirname(os.path.realpath(__file__))
if not os.path.exists("database"):
    os.makedirs("database")
dbTestDir = os.path.join(fileDir, 'database')

# capture the image from the cam
def image_capture(dir):
    time.sleep(2)
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test", cv2.WINDOW_NORMAL)
    img_counter = 0

    while True:
        ret, frame = cam.read()
        frame = cv2.flip(frame, 1)
        cv2.rectangle(frame,(300,50),(600,350),(250,0,0),2,cv2.LINE_AA)
        # croping the required image
        crop_img = frame[50:300, 350:600]
        img_name = str(dir + "\\" + str(img_counter) + ".jpg")
        # saving the image
        cv2.imwrite(img_name, crop_img)
        img_counter += 1
        print("Image capture no ", img_counter)

        cv2.imshow("test", frame)
        cv2.imshow("crop", crop_img)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break


        elif img_counter == 150:
            break
    cam.release()
    cv2.destroyAllWindows()


def main():
    name = input("enter ur name ")

    # create dir in database of username
    dir = os.path.join(dbTestDir, name)
    os.makedirs(dir)

    # calling the image_capture function
    print("put u hand in the box")
    image_capture(dir)

if __name__ == '__main__':
    main()