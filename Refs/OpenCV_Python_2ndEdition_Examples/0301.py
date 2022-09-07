import cv2
import numpy as np
 
imageFile = './data/lena.jpg'
img = cv2.imread(imageFile)
cv2.imshow('Lena Original',img)
 
pt1 = 100, 100
pt2 = 400, 400
cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)
 
cv2.line(img, (0, 0), (500, 0), (255, 0, 0), 5)
cv2.line(img, (0, 0), (0, 500), (0,0,255), 5)
 
cv2.imshow('Lena Lines',img)
 
cv2.imwrite('./data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 2])
 
imageFile = './data/Lena2.jpg'
img  = cv2.imread(imageFile)
 
cv2.imshow('Lena 2nd',img)
 
cv2.waitKey()
cv2.destroyAllWindows()