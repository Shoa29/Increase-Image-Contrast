
#pip install opencv-python
import cv2 as cv
#pip install numpy
import numpy as np


#reading the image of skeleton

img = cv.imread('assets/skeleton.png') #put the image path inside these brackets

new_img = np.zeros(img.shape, img.dtype)#initializing the new images pixels to 0
#but setting the size of new image same as previous one


alpha = 1.5  # Contrast control can set from 1 - 3 (you can change and play with these values according to you)
beta = 20    # Brightness control, can set from 0-100 range

# Scaling happens with this operation for each row and column of pixels - new_img(row,col) = alpha*image(row,col) + beta
#converting scale of all pixels from old image with alpha and beta value to new image
new_img = cv.convertScaleAbs(img, alpha=alpha, beta=beta)




cv.imshow('Original Skeleton Image', img)
cv.imshow('New Skeleton Image', new_img)

# Display both the images and wait till user presses any key
cv.waitKey()