import cv2 as cv
import numpy as np

def media(img):
    resultImage = np.zeros((img.shape[0], img.shape[1]), np.uint8)

    value = 0
    windowsSize = 3
    edge = 1

    neighbors = []
    mask = (1, 2, 1, 2, 4, 2, 1, 2, 1)

    rows, cols = img.shape

    for i in range(edge ,rows - edge):
        for j in range(edge, cols - edge):

            for x in range(windowsSize):
                for y in range(windowsSize):

                    neighbors.append(img[i - edge + x][j - edge + y])


            for k in range(len(neighbors)):
                value += neighbors.pop() * mask[k]

            result = round(value/16)

            if result < 0:   result = 0
            if result > 255: result = 255

            resultImage[i, j] = result

            value = 0

    return resultImage

img = cv.imread('soma2.jpg', 0)

cv.imshow('gaus', media(img))

cv.waitKey()