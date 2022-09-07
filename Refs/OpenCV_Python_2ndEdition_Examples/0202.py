# 0202.py
import cv2
import numpy as np


img_a = cv2.imread("1209.jpg")
img_b = cv2.imread("autobike.jpg")
img_c = img_a + img_b

print(img_a[0][0])
print(img_b[0][0])
print(img_c[0][0])
imageFile = img_c
img = cv2.imread(imageFile)

 
imageFile = './data/Lena.png'
img  = cv2.imread(imageFile)
 
cv2.imshow('Lena color',img)
 
cv2.waitKey()
cv2.destroyAllWindows()