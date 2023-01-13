import cv2
import numpy as np

img = cv2.imread("images/2.jpg")

# Поворот 1 - по горизонтали 0 - по вертекали
# img = cv2.flip(img, 1)

# Функция поворота изображения на угол переданный аргументом
def rotate(img_param, angle):
    height, width = img_param.shape[:2]
    point = (width // 2, height // 2)

    matrix = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img, matrix, (width, height))

# img = rotate(img, 90)

# 1 - ширина 0 - высота

# Функция смещения изображения на заданные в параметр координаты
def transform(img_param, x, y):
    matrix = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img_param, matrix, (img_param.shape[1], img_param.shape[0]))

img = transform(img, 30, 200 )

cv2.imshow("img", img)

cv2.waitKey(0)