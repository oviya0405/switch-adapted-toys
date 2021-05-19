import numpy as np
import cv2, random

# number of webcam/video device (only one on my laptop so using 0)
cap = cv2.VideoCapture(0)

while True:
    # ret is false if an error occured
    ret, frame = cap.read()
    # uint8 is unsigned 8 bit int
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    # for i in range(0, smaller_frame.shape[0], 2):
    #     for j in range(0, smaller_frame.shape[1], 2):
    #         smaller_frame[i][j] = [random.randrange(0, 255), random.randrange(0, 255) ,random.randrange(0, 255)]
    # cap.get(3) gets the width property of the video capture
    # 3 is the identifier for width and it is 4 for height
    width = int(cap.get(3))
    height = int(cap.get(4))
    # start at 0, 0 and go to height//2, width//2
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    # start at height//2 and width//2 and go to end of img
    image[height//2:, :width//2] = smaller_frame
    image[height//2:, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[:height//2, width//2:] = smaller_frame
    cv2.imshow("frame", image)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()