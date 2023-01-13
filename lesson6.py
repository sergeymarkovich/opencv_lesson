import cv2
import numpy as np

img = np.zeros((350, 350), dtype=np.uint8)

circle = cv2.circle(img.copy(), (0, 0), 80, 255, cv2.FILLED)
square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, cv2.FILLED)

# Побитовое умножение И. Отображение только одинаковых частей изображений фигур, которые пересекаются между собой
# img = cv2.bitwise_and(circle, square
# Побитовое сложение ИЛИ. Отображение общих частей фигур
# img = cv2.bitwise_or(circle, square)
# XOR - общие(одинаковые) части не включаются, не общие отображаются
img = cv2.bitwise_xor(circle, square)

cv2.imshow("Result", img)
cv2.waitKey(0)
