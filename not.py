import cv2 as cv
import numpy as np

def operacao(img):
    resultImage = np.zeros((img.shape[0], img.shape[1]), np.uint8)
    rows, cols = img.shape

    for i in range(rows):
        for j in range(cols):
           if img[i, j] == 255:
               resultImage[i, j] = 0
           else:
               resultImage[i, j] = 255

    return resultImage

def conv(img):
    rows, cols = img.shape

    for i in range(rows):
        for j in range(cols):
            if img[i, j] < 127:
                img[i, j] = 0;
            else:
                img[i, j] = 255
    return img



img = cv.imread('img2.png', 0)
img = conv(img)

cv.imshow('not', operacao(img))
cv.waitKey()
