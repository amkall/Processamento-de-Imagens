import cv2 as cv
import numpy as np


def soma(img1, img2):
    resultImage = np.zeros((img1.shape[0], img1.shape[1], img1.shape[2]), np.uint8)
    rows, cols, pixel = img1.shape

    for i in range(rows):
        for j in range(cols):
            for k in range(pixel):

                result = ((img1[i, j, k] / 2) + (img2[i, j, k] / 2))

                if resultImage[i][j][k] > 255:

                    resultImage[i][j][k] = 255

                resultImage[i, j, k] = result


    return resultImage


img = cv.imread('soma1.jpg', 1)
img2 = cv.imread('soma2.jpg', 1)


cv.imshow('soma', soma(img2, img ))
cv.waitKey()