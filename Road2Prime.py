import win32gui
import pyautogui
import time
from ScanCodeKeys import PressKey, ReleaseKey


button_offsets = {
    "PLAY" : [0.035,0.17],
    "WINGMAN" : [0.21, 0.217],
    "GO":[0.779,0.961],
    "ACCEPT":[0.444,0.58]
    }

def get_window_info(window_name):
    window = {}
    def callback(hwnd, extra):
        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        if win32gui.GetWindowText(hwnd) == window_name:
            print("Window \"%s\":" % win32gui.GetWindowText(hwnd))
            print("\tLocation: (%d, %d)" % (x, y))
            print("\t    Size: (%d, %d)" % (w, h))
            location = {"x": x, "y": y}
            size = {"x": w, "y": h}
            window["location"] = location
            window["size"] = size
    win32gui.EnumWindows(callback, None)
    return window
    
def toggle_console():
    PressKey(0xC0)
    ReleaseKey(0xC0)
    
def anti_afk():
    toggle_console()
    time.sleep(0.5)
    pyautogui.write('+left;+right;mm_dedicated_search_maxping 350')
    pyautogui.press('enter')
    toggle_console()

#window needs to be visible to work
def focus_window():
    startx = test["size"]["x"]/2
    clickx = test["location"]["x"] + startx
    clicky = test["location"]["y"] + 5
    pyautogui.moveTo(clickx,clicky)
    pyautogui.click()
    
def click_cs_button(button):
    startx = test["size"]["x"]*button_offsets[button][0]
    starty = test["size"]["y"]*button_offsets[button][1]
    clickx = test["location"]["x"] + startx
    clicky = test["location"]["y"] + starty
    if button == "ACCEPT":
        accept_visible = False
        while not accept_visible:
            if pyautogui.pixelMatchesColor(int(clickx),int(clicky),(76, 175, 80)):
                accept_visible=True
    pyautogui.moveTo(clickx,clicky)
    pyautogui.click()
    pyautogui.click()

def main():
    global test
    test = get_window_info("Counter-Strike: Global Offensive")
    focus_window()    
    anti_afk()
    click_cs_button("PLAY")
    click_cs_button("WINGMAN")
    click_cs_button("GO")
    click_cs_button("ACCEPT")

if __name__ == '__main__':
    main()