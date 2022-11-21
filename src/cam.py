import cv2
import time

faceCascade = cv2.CascadeClassifier('/Users/Radit./Documents/kelas/smt3/Algeo/Algeo02-21021/src/haar.xml')
video_capture = cv2.VideoCapture(1)
c=1
ct=0
while True:
    time.sleep(0.1)
    ct+=1
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    if ct>=100:
        filename="src/test"+str(c)+".jpg"
        img=frame
        crop_img = img[y:y+h, x:x+w]
        cv2.imwrite(filename,crop_img)
        c+=1
        ct=0
    # Display the resulting frame
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cv2.namedWindow("preview")
# vc = cv2.VideoCapture(1)

# if vc.isOpened(): # try to get the first frame
#     rval, frame = vc.read()
# else:
#     rval = False

# while rval:
#     cv2.imshow("preview", frame)
#     rval, frame = vc.read()
#     key = cv2.waitKey(20)
#     if key == 27: # exit on ESC
#         break

# vc.release()
# cv2.destroyWindow("preview")