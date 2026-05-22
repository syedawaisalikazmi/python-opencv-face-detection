#face detection using opencv live webcam
import cv2
#haar cascade classifier ka use karain ge face detection ke liye
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
# ya xml file hai jisme face detection ke liye trained data hota hai
#live webcam se video capture karain ge
camera_detect = cv2.VideoCapture(0)
if not camera_detect.isOpened():
    print("Camera not found")
    exit()
while True:
    #video frame read karain ge
    camera_status, frame = camera_detect.read()
    #agar frame read ho gaya to face detection karain ge
    if camera_status:
        #grayscale image banain ge face detection ke liye
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #face detection karain ge
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        #face detection ke baad rectangle draw karain ge detected faces ke around
        for (left, right, w, h) in faces:
            cv2.rectangle(frame, (left, right), (left + w, right + h), (255, 0, 0), 2)#(ya 255 kya aur 0 ,0) ya color code hai jo rectangle ka color define karta hai, yahan par blue color use kiya gaya hai
        #video frame display karain ge
        cv2.imshow('Face Detection', frame)
    #agar user 'q' press kare to loop break karain ge
    if cv2.waitKey(1) == ord('q'):
        break
#video capture release karain ge
camera_detect.release()
#windows close karain ge
cv2.destroyAllWindows()
print("Face detection stopped.")
