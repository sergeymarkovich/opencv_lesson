import cv2
import numpy as np

photo = np.zeros((300, 300, 3), dtype='uint8')

# RGB - classic standard
# BGR - format in opengl
# photo[:] = 255, 0, 0

# cube
cv2.rectangle(photo, (20, 20), (100, 100), (255, 0, 0), thickness=2)

# line
cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (255, 0, 0), thickness=2)

#circle
cv2.circle(photo, (photo.shape[0] // 2, photo.shape[1] // 2), 25, (0, 255, 0), thickness=cv2.FILLED)

#some text
cv2.putText(photo, "Some text", (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), thickness=2)

cv2.imshow("photo", photo)
cv2.waitKey(0)