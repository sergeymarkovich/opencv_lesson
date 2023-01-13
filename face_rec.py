import face_rec

img = face_recognition.load_image_file("images/test.jpg")
img_face_locations = face_recognition.face_locations(img)

print(img_face_locations)