import numpy as np
import cv2 as cv
import math

def quantizacao_uniforme(img, k):
    img = np.float32(img)
    quantized = img.copy()

    rows = img.shape[0]
    cols = img.shape[1]

    for i in range(rows):
        for j in range(cols):
            quantized[i, j] = (math.pow(2, k) - 1) * np.float32((img[i, j] - img.min()) / (img.max() - img.min()))
            quantized[i, j] = np.round(quantized[i, j]) * int(256/math.pow(2, k))

    return quantized;

imagem = cv.imread('novo.jpg', 0)
cv.resize(imagem, (600, 600))

cv.imshow('quantização', quantizacao_uniforme(imagem, 2))
cv.waitKey()