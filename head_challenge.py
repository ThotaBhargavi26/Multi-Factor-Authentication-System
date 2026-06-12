import cv2

left_done = False
right_done = False

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:

        center_x = x + w // 2

        # Show current value on screen
        cv2.putText(
            frame,
            f"Center X: {center_x}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        # Left detection
        if center_x < 250:
            left_done = True
            cv2.putText(
                frame,
                "LEFT VERIFIED",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        # Right detection
        if center_x > 350:
            right_done = True
            cv2.putText(
                frame,
                "RIGHT VERIFIED",
                (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        # Final confirmation
        if left_done and right_done:
            cv2.putText(
                frame,
                "REAL PERSON CONFIRMED",
                (20, 170),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                3
            )

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )
    cv2.imshow("Head Challenge", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()