import pyautogui as coordinates

while True:
    log = coordinates.position()
    print(log, end="\r")