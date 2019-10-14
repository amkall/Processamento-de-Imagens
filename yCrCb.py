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

            y = ((0.299 * r) + (0.587 * g) + (0.114 * b))
            Cr = ((r - y) * 0.713) + 128
            Cb = ((b-y) * 0.564) + 128

            result[i, j, 0] = y
            result[i, j, 1] = Cr
            result[i, j, 2] = Cb



    return result


img = cv.imread('novo.jpeg', 1)
cv.imshow('yCrCb', Cinza(img))

cv.waitKey()