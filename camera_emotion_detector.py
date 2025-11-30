import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
emotion_model = load_model('emotion_model.h5')  # fixed filename

emotions = ['Angry','Sad','Disgust','Fear','Happy','Surprised','Neutral']
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()  # fixed variable name
    if not ret:
        print("Error: Failed to capture")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        # resize to model input — change (48,48) if your model expects a different size
        roi_resized = cv2.resize(roi_gray, (48, 48))
        roi_resized = roi_resized.astype('float32') / 255.0
        roi_resized = img_to_array(roi_resized)     # will add channel dim for grayscale
        roi_resized = np.expand_dims(roi_resized, axis=0)
        emotion_pred = emotion_model.predict(roi_resized)
        max_index = np.argmax(emotion_pred[0])
        predicted = emotions[max_index]
        cv2.putText(frame, predicted, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)

    cv2.imshow('Face and Emotion Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
