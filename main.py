import cv2
import numpy as np
import pyautogui
from hand_tracking_module import HandDetector
from mouse_controller import MouseController

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
mouse = MouseController()

screen_w, screen_h = pyautogui.size()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList = detector.findPosition(img)

    if lmList:
        # Index finger tip (id 8)
        x1, y1 = lmList[8][1], lmList[8][2]

        # Middle finger tip (id 12)
        x2, y2 = lmList[12][1], lmList[12][2]

        frame_h, frame_w, _ = img.shape

        # Move mouse using index finger
        mouse.move_mouse(x1, y1, frame_w, frame_h)

        # Click gesture: distance between index and middle finger
        distance = np.hypot(x2 - x1, y2 - y1)

        if distance < 40:
            mouse.click()
            cv2.putText(img, "CLICK", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("Hand Mouse System", img)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
