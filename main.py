import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) == 27:  # Press ESC to exit
        break

cam.release()
cv2.destroyAllWindows()