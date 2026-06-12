from deepface import DeepFace
import cv2
import time
import speech_recognition as sr

# FACE VERIFICATION

cap = cv2.VideoCapture(0)

print("Look at the camera...")
time.sleep(5)

ret, frame = cap.read()

cv2.imwrite("current.jpg", frame)

cap.release()

result = DeepFace.verify(
    img1_path="faces/bhavana.jpg",
    img2_path="current.jpg",
    enforce_detection=False
)

if result["verified"]:

    print("FACE VERIFIED")

    # VOICE VERIFICATION

    secret_code = "apple"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak the secret code:")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio).lower()

        print("You said:", text)

        if text == secret_code:
            print("ACCESS GRANTED")
        else:
            print("ACCESS DENIED")

    except:
        print("Could not understand audio")

else:
    print("FACE NOT VERIFIED")
    print("ACCESS DENIED")