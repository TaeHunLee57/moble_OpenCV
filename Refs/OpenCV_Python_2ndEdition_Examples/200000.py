# 0207.py
import cv2
import numpy as np

imageFile='./data/lena.jpg'
img=cv2.imread(imageFile)
cap = cv2.VideoCapture('./data/vtest.avi')

resize_img = cv2.resize(img,(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))), interpolation= cv2.INTER_CUBIC)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print('frame_size =', frame_size)

while True:   
    retval, frame = cap.read()
    if not retval:
        break
    cap2=cv2.add(resize_img,frame)
    cv2.imshow('frame',cap2)
    
    key = cv2.waitKey(25)
    if key == 27: # Esc
        break
if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()