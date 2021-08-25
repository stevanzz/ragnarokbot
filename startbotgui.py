import PySimpleGUI as sg
from screenshot import screenshot_image
from utils import confidence, get_region
import time
import win32api
import win32con
import pyautogui
import threading

global run_bot
run_bot = False

image_name_1 = "lempar-pancing.png"
image_name_2 = "angkat-pancing.png"


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def start_bot():
    gagal_counter = 0
    gagal_counter_limit = 2
    while run_bot:
        # Jika gagal_counter_limit telah tercapai, bot akan stop
        # kemungkinan screenshot "Angkat Pancing" kurang jelas, silahkan upload screenshot yang baru
        if gagal_counter >= gagal_counter_limit:
            print("gagal counter limit", gagal_counter_limit," telah tercapai, tolong dicek lagi screenshotnya")
            window["Start Bot"].update(disabled=False)
            break

        if pyautogui.locateOnScreen(image_name_1, region=get_region(), confidence=confidence) != None:
            print("lempar")
            click(1460 + 90, 680 + 100)
            gagal_counter += 1
            time.sleep(0.5)
        elif pyautogui.locateOnScreen(image_name_2, region=get_region(), confidence=confidence) != None:
            print("angkat")
            click(1460 + 90, 680 + 100)
            gagal_counter = 0
            time.sleep(0.5)
        else:
            # semakin kecil interval semakin sering bot akan check screen
            # semakin besar, bot akan lebih jarang check screen (lebih besar kemungkinan gagal)
            # print("sleep")
            time.sleep(0.1)


# ----- Full layout -----
layout = [
    [sg.Button("Load Screenshots")],
    [
        [sg.Text(image_name_1), sg.Button("Screenshot 1")],
        [sg.Image(key="-lemparpancingimage-")]
    ],
    [
        [sg.Text(image_name_2), sg.Button("Screenshot 2")],
        [sg.Image(key="-angkatpancingimage-")]
    ],
    [sg.Text()],
    [
        sg.Button("Start Bot"), sg.Button("Stop Bot")
    ]
]

window = sg.Window("RoX Fishing Bot", layout)


# Run the Event Loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Load Screenshots":
        try:
            window["-lemparpancingimage-"].update(filename="./" + image_name_1)
            window["-angkatpancingimage-"].update(filename="./" + image_name_2)
        except Exception as e:
            print("gagal load screenshots")
            print(e)
    elif event == "Screenshot 1":
        try:
            screenshot_image(image_name_1)
            window["-lemparpancingimage-"].update(filename="./" + image_name_1)
        except Exception as e:
            print("gagal screenshot lempar pancing")
            print(e)
    elif event == "Screenshot 2":
        try:
            screenshot_image(image_name_2)
            window["-angkatpancingimage-"].update(filename="./" + image_name_2)
        except Exception as e:
            print("gagal screenshot angkat pancing")
            print(e)
    elif event == "Start Bot":
        try:
            run_bot = True
            threading.Thread(target=start_bot, daemon=True).start()
            window["Start Bot"].update(disabled=True)
        except Exception as e:
            print("Bot error")
            print(e)
            break
    elif event == "Stop Bot":
        window["Start Bot"].update(disabled=False)
        run_bot = False


window.close()
