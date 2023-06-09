import cv2
import pyttsx3

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Opencv DNN models

net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(350, 350), scale=1 / 255)

# Load class lists
classes = []
with open("dnn_model/classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)

print("object list")
print(classes)

# Initialze camera

cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
while True:

    # Get frames
    ret, frame = cap.read()

    # object detection

    (class_ids, scores, bboxes) = model.detect(frame)
    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x, y, w, h) = bbox
        print(x, y, w, h)
        class_name = classes[class_id]
        cv2.putText(frame, class_name, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (200, 0, 40), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 50, 255), 2)

        # Speak out the class name
        engine.say(class_name)
        engine.runAndWait()

    print("class_ids", class_ids)
    print("scores", scores)
    print("bboxes", bboxes)

    cv2.imshow('Frame', frame)
    cv2.waitKey(2)
