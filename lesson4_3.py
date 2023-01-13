# search contour in image
import cv2
import numpy as np

img = cv2.imread('images/2.jpg')
new_img = np.zeros(img.shape, dtype='uint8')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)

# Удаление нежелательных пикселей, которые могут не составлять края
img = cv2.Canny(img, 100, 200)

# Возвращает две переменные - список со всеми контурами, во втором - иерархия самих объектов
# RETR_LIST - получаем полностью все доступные контуры
# CHAIN_APPROX_NONE - найденны обсолютно все координаты контуров (для линии - все точки линии)
# CHAIN_APPROX_SIMPLE - начальная координата линии и конечная
con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(new_img, con, -1, (100, 150, 120), 1)

cv2.imshow('Result', new_img)
cv2.waitKey(0)