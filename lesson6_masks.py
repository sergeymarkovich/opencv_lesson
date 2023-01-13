import cv2
import numpy as np

photo = cv2.imread('images/2.jpg')
img = np.zeros(photo.shape[:2], dtype=np.uint8)

circle = cv2.circle(img.copy(), (0, 0), 80, 255, cv2.FILLED)
square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, cv2.FILLED)

img = cv2.bitwise_and(photo, photo, mask=square)

cv2.imshow("Result", img)
cv2.waitKey(0)
