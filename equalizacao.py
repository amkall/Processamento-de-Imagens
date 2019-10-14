import cv2 as cv
import numpy as np

def equalize(img):
    rImage = np.zeros((img.shape[0], img.shape[1]), np.uint8)
    resultImage = np.zeros(img.max()+1, )
    rows, cols = img.shape

    for i in range(rows):
        for j in range(cols):
            resultImage[img[i, j]] += 1

    acumular = resultImage

    for i in range(img.max() - 1):
        acumular[i + 1] += acumular[i]

    for i in range(img.max()):
        aux = acumular[i] * (255/(rows * cols))
        acumular[i] = round(aux)

    for i in range(rows):
        for j in range(cols):
            rImage[i][j] = acumular[img[i][j]]

    return rImage

img = cv.imread('novo.jpg', 0)

cv.imshow('equalize', equalize(img))
cv.imshow('foto', img)
cv.waitKey()

