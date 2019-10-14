import cv2 as cv
import numpy as np

def Cinza(img):
    result = np.zeros((img.shape[0], img.shape[1], img.shape[2]), np.uint8)
    rows, cols, pixel = img.shape

    for i in range(rows):
        for j in range(cols):
            r = img[i, j, 0]
            g = img[i, j, 1]
            b = img[i, j, 2]

            c = 255 - r
            m = 255 - g
            y = 255 - b

            result[i, j, 0] = c
            result[i, j, 1] = m
            result[i, j, 2] = y



    return result


img = cv.imread('novo.jpeg', 1)
cv.imshow('cmy', Cinza(img))

cv.waitKey()