import cv2

# Carrega a "cascade" que será responsável por visualizar o rosto do usuário
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Captura o vídeo da WebCam
cap = cv2.VideoCapture(0)
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

face_encodings = []

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detecta os rostos
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Coloca quantas pessoas, a partir de seus rostos, estão aparecendo na webcam
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = f"Pessoas: {len(faces)}"
    cv2.putText(img, text, (10, 30), font, 1, (255, 255, 255), 2)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if len(faces) >= 5:
        print("Que tanto de gente")
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()
