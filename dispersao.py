import cv2 as cv
import numpy as np


def ditheringDispersao(img):
    matrixP = np.array([[2, 3], [4, 1]])

    resultImage = np.zeros((img.shape[0], img.shape[1]), np.uint8)
    rows, columns = img.shape

    for i in range(rows):
        for j in range(columns):
            m = i % matrixP.shape[0]
            n = j % matrixP.shape[1]

            temp1 = (img[i][j] * 1.0) / img.max()
            temp2 = (matrixP[m][n] * 1.0) / matrixP.max()

            if temp1 > temp2:
                resultImage[i][j] = 255
            else:
                resultImage[i][j] = 0
    return resultImage


img = cv.imread('koala.jpeg', 0)
cv.imshow('img', ditheringDispersao(img))
cv.namedWindow('img', cv.WINDOW_AUTOSIZE)
# cv.resizeWindow('img', 300, 300)
cv.waitKey(0)