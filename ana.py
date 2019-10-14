import cv2 as cv
import numpy as np

def media(img):
    resultImage = np.zeros((img.shape[0], img.shape[1]), np.uint8)

    windowsSize = 3
    edge = 1

    neighbors = []


    rows, cols = img.shape

    for i in range(edge ,rows - edge):
        for j in range(edge, cols - edge):

            for x in range(windowsSize):
                for y in range(windowsSize):

                    neighbors.append(img[i - edge + x][j - edge + y])

            order = sorted(neighbors)

            resultImage[i, j] = order[5]

            neighbors.clear()

    return resultImage

img = cv.imread('soma2.jpg', 0)

cv.imshow('mediana', media(img))

cv.waitKey()