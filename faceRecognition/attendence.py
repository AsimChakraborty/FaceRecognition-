import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'imgattendence'
images = []
classNames = []
midlename = []
mylist = os.listdir(path)

print(len(mylist))
for cls in mylist:
    currentimg = cv2.imread(f'{path}/{cls}')
    images.append(currentimg)

    classNames.append(os.path.splitext(cls)[0])
    # n=len(mylist)
    # if n ==4:
    #    middle = ' '.join(mylist[:2]), ' '.join(mylist[2:])
    #    print("mid")
    # # midlename.append(os.path.splitext(cls)[(len(mylist)-1)//2:(len(mylist)+2)//2])
    #
    # # midlename.append(os.path.splitext(cls).split('-')[1])
    # midlename.append(middle)


print(classNames)
print(midlename)


# encode the img
def findencoding(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist
# def findencoding(images):
#     encodelist = []
#     for img in images:
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         face_locations = face_recognition.face_locations(img)
#         if len(face_locations) > 0:
#             encode = face_recognition.face_encodings(img, face_locations)[0]
#             encodelist.append(encode)
#     return encodelist










# mark attendance
def markattendance(name):
    with open('a.csv', 'r+') as f:
        mydatalist = f.readline()
        # print(mydatalist)
        namelist = []
        for line in mydatalist:
            entry = line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstring}')


# markattendance('asim')

encodelistknown = findencoding(images)

print(len(encodelistknown))

print('encoding complete')

# matche the img using webcam

cap = cv2.VideoCapture(0)
while True:
    sucesss, img1 = cap.read()
    imgs = cv2.resize(img1, (0, 0), None, 0.25, 0.25)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
    facecurrentfram = face_recognition.face_locations(imgs)
    encodecurrent = face_recognition.face_encodings(imgs, facecurrentfram)

    for encodeface, faceLoc in zip(encodecurrent, facecurrentfram):
        matchs = face_recognition.compare_faces(encodelistknown, encodeface)
        facedis = face_recognition.face_distance(encodelistknown, encodeface)
        print(facedis)
        matchindex = np.argmin(facedis)
        if matchs[matchindex]:
            print("known face")
            name = classNames[matchindex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img1, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img1, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img1, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markattendance(name)
    if cv2.waitKey(2) == ord('a'):
        break
    cv2.imshow('Granny Cam', img1)
    # cv2.waitKey(1)
