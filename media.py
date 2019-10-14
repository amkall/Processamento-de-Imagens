import cv2 as cv
import numpy as np

def media(img):
    resultImage = np.zeros((img.shape[0], img.shape[1]), np.uint8)

    value = 0
    windowsSize = 3
    edge = 1

    rows, cols = img.shape

    for i in range(edge ,rows - edge):
        for j in range(edge, cols - edge):

            for x in range(windowsSize):
                for y in range(windowsSize):

                    value += img[i - edge + x][j - edge + y]


            resultImage[i, j] = round((value * 1) / (windowsSize * windowsSize))
            value = 0

    return resultImage

img = cv.imread('soma2.jpg', 0)

cv.imshow('media', media(img))

cv.waitKey()