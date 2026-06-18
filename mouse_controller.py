import pyautogui
import numpy as np

screen_w, screen_h = pyautogui.size()

class MouseController:
    def __init__(self, smoothening=5):
        self.smoothening = smoothening
        self.plocX, self.plocY = 0, 0
        self.clocX, self.clocY = 0, 0

    def move_mouse(self, x, y, frame_w, frame_h):
        # Convert webcam coords to screen coords
        screen_x = np.interp(x, (0, frame_w), (0, screen_w))
        screen_y = np.interp(y, (0, frame_h), (0, screen_h))

        # Smooth movement
        self.clocX = self.plocX + (screen_x - self.plocX) / self.smoothening
        self.clocY = self.plocY + (screen_y - self.plocY) / self.smoothening

        pyautogui.moveTo(self.clocX, self.clocY)

        self.plocX, self.plocY = self.clocX, self.clocY

    def click(self):
        pyautogui.click()
