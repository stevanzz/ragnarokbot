import pyautogui
import time
import win32api
import win32con
from utils import confidence, get_region

count = 0


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# Kalau 2x gagal, bot akan stop
# kemungkinan screenshot "Angkat Pancing" kurang jelas, silahkan upload screenshot yang baru
while count < 2:
    if pyautogui.locateOnScreen('lemparpancing.png', region=get_region(), confidence=confidence) != None:
        # print("cast")
        click(1460 + 90, 680 + 100)
        count += 1
        time.sleep(0.5)
    elif pyautogui.locateOnScreen('angkatpancing.png', region=get_region(), confidence=confidence) != None:
        # print("reel")
        click(1460 + 90, 680 + 100)
        count = 0
        time.sleep(0.5)
    else:
        # semakin kecil interval semakin sering bot akan check screen
        # semakin besar, bot akan lebih jarang check screen (lebih besar kemungkinan gagal)
        time.sleep(0.1)
