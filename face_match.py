from deepface import DeepFace
import cv2
import time

# Open camera
cap = cv2.VideoCapture(0)

print("Look at the camera...")
time.sleep(5)

ret, frame = cap.read()

if not ret:
    print("Camera Error")
    exit()

# Save current image
cv2.imwrite("current.jpg", frame)

cap.release()

# Face Verification
result = DeepFace.verify(
    img1_path="faces/bhavana.jpg",
    img2_path="current.jpg",
    enforce_detection=False
)

# Show details
print("Verified =", result["verified"])
print("Distance =", result["distance"])
print("Threshold =", result["threshold"])

if result["verified"]:
    print("FACE VERIFIED")
else:
    print("FACE NOT VERIFIED")