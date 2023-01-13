import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)

# Read image
img = cv2.imread('images/2.jpg')
#Add blure to the image
img = cv2.GaussianBlur(img, (11, 11), 0)
# Change color of image // Изменение цветовой палитры
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Angles of picture // Удаление нежелательных пикселей, которые могут не составлять края
img = cv2.Canny(img, 100, 100)
# Changing the contour of the outline angles // Увеличение размера выделенного контура
img = cv2.dilate(img, kernel, iterations=1)
# Уменьшаем обводку в жирности // Уменьшение размера выделенного контура
img = cv2.erode(img, kernel, iterations=1)


# New options with shape
# new_image = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
# img[0:100, 0:100]

cv2.imshow('text', img)
# Show size of the image
# print(img.shape)
# Unlimited interrupt to show image
cv2.waitKey(0)

# Read video, if webcam, then 0
# cap = cv2.VideoCapture(0)
# Set sizes for video
# cap.set(3, 500)
# cap.set(4, 500)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow('text', img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
