import cv2 as cv
import numpy as np


def dithering(img):
    resultImage = np.zeros((img.shape[0], img.shape[1], img.shape[2]), np.uint8)
    rows, columns, pixel = img.shape

    for i in range(rows):
        for j in range(columns):
            temp = img[i][j][0] + np.random.randint(-127, 127)
            threshold = 127
            if temp < threshold:
                resultImage[i][j] = 0
            else:
                resultImage[i][j] = 255
    return resultImage





img = cv.imread('koala.jpeg', 1)
cv.imshow('img', dithering(img))
cv.namedWindow('img', cv.WINDOW_AUTOSIZE)
# cv.resizeWindow('img', 300, 300)
cv.waitKey(0)