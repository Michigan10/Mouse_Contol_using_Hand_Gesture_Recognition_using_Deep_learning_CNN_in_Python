import cv2
import pyautogui
import tkinter as tk
from PIL import Image, ImageTk

# to avoid boundary warning
pyautogui.FAILSAFE = False
root = tk.Tk()
root.geometry("250x250+900+40")
# tkinter window always on top
root.wm_attributes("-topmost", 1)

lmain = tk.Label(root)
lmain.pack()

from tensorflow.contrib import predictor
# model path
model_path = ".\\export_model\\1539926721\\"
# loading the model
predict_fn = predictor.from_saved_model(export_dir = model_path)

cam = cv2.VideoCapture(0)
pred_previous = 0

my_dict = {0:"copy a file", 1: "move a mouse", 2: "do nothing", 3: "open a file", 4: "paste a file"}

print(my_dict)

count = 0

old_top = (1000,500)

position1 = (0,0)

frame_count = 0

position1_dict = []

# move the mouse
def relative_mouse(top):
    global old_top
    diff_x = top[0] - old_top[0]
    diff_y = top[1] - old_top[1]
    if abs(diff_x) >= 30:
        mul_x = 40
    elif abs(diff_x) >= 20:
        mul_x = 20
    elif abs(diff_x) >= 15:
        mul_x = 15
    elif abs(diff_x) >= 10:
        mul_x = 10
    elif abs(diff_x) >= 5:
        mul_x = 5
    else:
        mul_x = 1

    if abs(diff_y) >= 30:
        mul_y = 20
    elif abs(diff_y) >= 25:
        mul_y = 15
    elif abs(diff_y) >= 20:
        mul_y = 12
    elif abs(diff_y) >= 15:
        mul_y = 9
    elif abs(diff_y) >= 10:
        mul_y = 6
    else:
        mul_y = 1

    pyautogui.moveRel(diff_x * mul_x, diff_y * mul_y, duration=0.1)
    old_top = top
    return pyautogui.position()

# open a file
def click_mouse():
    x, y = pyautogui.position()
    pyautogui.doubleClick(x, y)

# copy a file
def copy_commd():
    pyautogui.hotkey('ctrl', 'c')

# paste a file
def paste_cmmd():
    x, y = pyautogui.position()
    pyautogui.click(x,y)
    pyautogui.hotkey('ctrl', 'v')


def main():
    global count, pred_previous, position1, frame_count, position1_dict
    frame_count += 1
    # reading frame from web cam
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    # croping the required area
    crop = frame[50:300, 300:550]
    crop_RGB = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
    # coverting to gray scale
    grey = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    value = (35, 35)
    blurred = cv2.GaussianBlur(grey, value, 0)
    _, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    thresh1 = thresh / 255
    # reshaping the image for predicting on the image
    thresh1 = thresh1.reshape(1, 250, 250, 1)
    # predicting on the input image
    pred_new = predict_fn({'image': thresh1})
    pred_new = pred_new["output"][0]

    # for moving the mouse
    if pred_new == 1:
        _, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        max_area = -1
        for i in range(len(contours)):
            cnt = contours[i]
            area = cv2.contourArea(cnt)
            if (area > max_area):
                max_area = area
                ci = i
        cnt = contours[ci]
        # getting the top most point to move the move
        topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
        position1 = relative_mouse(topmost)
        if len(position1_dict) == 2:
            del position1_dict[0]
        position1_dict.append(position1)

    if count == 5:
        print(my_dict[pred_new])
        pred_previous = pred_new
        count = 0

        # doing nothing
        if pred_previous == 2:
            pass
        # paste file
        if pred_previous == 4:
            paste_cmmd()
        # copy file
        if pred_previous == 0:
            pyautogui.moveTo(position1_dict[0][0], position1_dict[0][1], duration=0.25)
            pyautogui.click(position1_dict[0][0], position1_dict[0][1])
            print("copy",frame_count)
            copy_commd()
        # open a file
        if pred_previous == 3:
            print("click",frame_count)
            click_mouse()


    if pred_new != pred_previous:
        count += 1
    cv2.putText(crop_RGB, str(my_dict[pred_new]),(5, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),2)
    img = Image.fromarray(crop_RGB)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(100, main)

main()
root.mainloop()