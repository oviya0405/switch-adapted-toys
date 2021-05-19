"""
Using what is called a haar cascade to detect faces and eyes.
Haar cascades are pre-trained and look for specific features in images.
A feature could be the distance between two centroids, the colours in
the image, the shapes that are present, etc.

Each haar cascade is trained on one specific thing, such as a face,
a cat, a dog, a car, a person, etc.
"""


import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# comes as a part of opencv
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

while True:
    ret, frame = cap.read()

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # img, scaleFactor (smaller value is higher accuracy but slower performace),
    # minNeighbours (how many can overlap before it determines that what is found is a face (how accurate it is))
    faces = face_cascade.detectMultiScale(grey, 1.1, 3)
    # faces gives a rectangle
    imgToSave = None
    for (x, y, w, h) in faces:
        imgToSave = np.copy(frame)[y:y+h, x:x+w]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # ROI = reigon of interest
        roi_grey = grey[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # eye detection
        eyes = eye_cascade.detectMultiScale(roi_grey, 1.1, 7)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)

    cv2.imshow("face/eye tracking", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    if key == ord("s"):
        if imgToSave is not None: cv2.imwrite("captured_image.png", imgToSave)

cap.release()
cv2.destroyAllWindows()
