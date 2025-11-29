import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error Could Not Open Camera")
    exit()
while True:
    rect,frame=cap.read()
    if not rect:
        print("Error Failed to Capture image ")
        break
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:  
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) # Blue rectangle with thickness 2
    # Display the resulting frame
    cv2.imshow('Face Detection - Press q to Quit', frame)    
    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




