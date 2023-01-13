import cv2
import numpy as np

img = cv2.imread('images/2.jpg')

# RGB to HSV format
# img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

# RGB to LAB format
# img = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Разбитие на слои
r, g, b = cv2.split(img)

# Объединение слоев
img = cv2.merge([b, g, r])

cv2.imshow('Result', img)
cv2.waitKey(0)
