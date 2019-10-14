import cv2 as cv
import numpy as np

def Cinza(img):
    result = np.zeros((img.shape[0], img.shape[1]), np.uint8)
    rows, cols, pixel = img.shape

    for i in range(rows):
        for j in range(cols):
            r = img[i, j, 0]
            g = img[i, j, 1]
            b = img[i, j, 2]

            result[i][j] = ((r/3) + (g/3) + (b/3))

    return result


img = cv.imread('novo.jpeg', 1)
cv.imshow('cinza', Cinza(img))

cv.waitKey()