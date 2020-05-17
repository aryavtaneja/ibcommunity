import cv2
import pyttsx3
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
speaker = pyttsx3.init()
video = cv2.VideoCapture(0)

while True:
    return_code, frame_cap = video.read()
    grayimage = cv2.cvtColor(frame_cap, cv2.COLOR_BGR2GRAY)
    all_faces = face_cascade.detectMultiScale(grayimage, 1.1, 6)
    num_of_faces = len(all_faces)
    print(num_of_faces)
    for (x,y, w, h) in all_faces:
        cv2.rectangle(frame_cap, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow('output', frame_cap)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
    if num_of_faces == 1:
        speaker.say("There is 1 person ahead of you")
    else:
        speaker.say("There are %d people ahead of you" % num_of_faces)
    speaker.runAndWait()
    time.sleep(4)
video.release()
cv2.destroyAllWindows()
