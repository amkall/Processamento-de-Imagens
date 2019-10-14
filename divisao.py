import cv2 as cv
import numpy as np

def multiplicao(img1, img2):

    resultImage = np.zeros((img1.shape[0], img1.shape[1], img1.shape[2]), np.uint8)
    rows, cols, pixel = img1.shape

    for i in range(rows):
        for j in range(cols):

            if img[i, j, 0] == 0:
                img[i, j, 0] = 1

            if img2[i, j, 0] == 0:
                img2[i, j, 0] = 1

            div = img[i, j, 0] / img2[i, j, 0]

            round(div)

            resultImage [i, j, 0] = div

    return resultImage

img = cv.imread('soma1.jpg', 1)
img2 = cv.imread('soma2.jpg', 1)
cv.imshow('mult', multiplicao(img, img2))

cv.waitKey()


