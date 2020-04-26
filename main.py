import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)

while True:
    return_code, frame_cap = video.read()
    grayimage = cv2.cvtColor(frame_cap, cv2.COLOR_BGR2GRAY)
    all_faces = face_cascade.detectMultiScale(grayimage, 1.1, 4)
    num_of_faces = '%d faces' % len(all_faces)
    print(num_of_faces)
    for (x,y, w, h) in all_faces:
        cv2.rectangle(frame_cap, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow('output', frame_cap)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

video.release()
cv2.destroyAllWindows()
