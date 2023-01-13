import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)

# Read video, if webcam, then 0
cap = cv2.VideoCapture('videos/test.mp4')
# Set sizes for video
cap.set(3, 500)
cap.set(4, 500)

while True:
    success, img = cap.read()

    img = cv2.GaussianBlur(img, (11, 11), 0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img, 30 , 30)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    cv2.imshow('video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break