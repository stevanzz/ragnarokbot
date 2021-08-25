from utils import confidence, get_region
import time
import win32api
import win32con
import pyautogui

gagal_counter = 0
gagal_counter_limit = 2

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while True:
    # Jika gagal_counter_limit telah tercapai, bot akan stop
    # kemungkinan screenshot "Angkat Pancing" kurang jelas, silahkan upload screenshot yang baru
    if gagal_counter >= gagal_counter_limit:
        print("gagal counter limit", gagal_counter_limit," telah tercapai, tolong dicek lagi screenshotnya")
        break

    if pyautogui.locateOnScreen('lempar-pancing.png', region=get_region(), confidence=confidence) != None:
        print("lempar")
        click(1460 + 90, 680 + 100)
        gagal_counter += 1
        time.sleep(0.5)
    elif pyautogui.locateOnScreen('angkat-pancing.png', region=get_region(), confidence=confidence) != None:
        print("angkat")
        click(1460 + 90, 680 + 100)
        gagal_counter = 0
        time.sleep(0.5)
    else:
        # semakin kecil interval semakin sering bot akan check screen
        # semakin besar, bot akan lebih jarang check screen (lebih besar kemungkinan gagal)
        # print("sleep")
        time.sleep(0.1)
