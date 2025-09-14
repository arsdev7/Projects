#-------------------------------------------------  arsdev7  ----------------------------------------------------------------------------

# IT WILL DETECT YOUR FACE AND EYE AND SMILE USING OPENCV   
# TO EXIT PRESS ON ( Q ) KEYBORD
    
import cv2

face_cascade = cv2.CascadeClassifier("C:\ZBACKUP\STUDY\OpenCV\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("C:\ZBACKUP\STUDY\OpenCV\haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("C:\ZBACKUP\STUDY\OpenCV\haarcascade_smile.xml")


cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        roi_frame = frame[y:y+h,x:x+h]
        roi_gray = gray[y:y+h,x:x+h]

        eye = eye_cascade.detectMultiScale(gray,1.1,10)
        smile = smile_cascade.detectMultiScale(gray,1.7,20)

        if len(eye) > 0:
            cv2.putText(frame,"Eye Detected",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
        if len(smile) > 0:
            cv2.putText(frame,"Smile Detected",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0.255),2)
    cv2.imshow("Smart Detector",frame)
    if cv2.waitKey(1) & 0xff == ord("q"):
            print("Quiting....")
            break
cap.release()
cv2.destroyAllWindows()