
import cv2

"""
0 -> Grayscale image
1 -> Color image
-1  -> color image with transparency effects

"""

img_one = cv2.imread("galaxy.jpg",0) 


print(type(img_one))
# print(img)
# Yeh, python stores images by ndarray of numpy...
# print(img.shape)
