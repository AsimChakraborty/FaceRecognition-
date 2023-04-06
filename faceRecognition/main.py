# ##### libaries #####
import numpy as np
import cv2
import face_recognition

imgsakib = face_recognition.load_image_file("images/sakib.jpg")
imgsakib = cv2.cvtColor(imgsakib, cv2.COLOR_BGR2RGB)  # convert to rgb color

# Testing image

imgTest = face_recognition.load_image_file("images/tamim.jpg")
imgsTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceloc = face_recognition.face_locations(imgsakib)[0]  # detect the face
encodesakib = face_recognition.face_encodings(imgsakib)[0]  # encode the face

cv2.rectangle(imgsakib, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (255, 0, 255), 2)


faceloctest = face_recognition.face_locations(imgTest)[0]
encodetest = face_recognition.face_encodings(imgTest)[0]
# print(faceloc (46, 155, 136, 66))
cv2.rectangle(imgTest, (faceloctest[3], faceloctest[0]), (faceloctest[1], faceloctest[2]), (255, 0, 255), 2)



results = face_recognition.compare_faces([encodesakib], encodetest)

facedis = face_recognition.face_distance([encodesakib], encodetest)
print(results, facedis)

cv2.putText(imgTest, f'{results} {round(facedis[0], 1)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2) # origin 50,50,font size 1,color 0,0,255, thikness 2

cv2.imshow('sakib', imgsakib)  # show the image
cv2.imshow('test', imgTest)
cv2.waitKey(0)
