import threading
import time

import pyautogui
from pynput import keyboard

delay = float(input("Delay (secs): "))
mouse_btn = input("Mouse button l - left, r - right: ")
match mouse_btn:
	case "l":
		mouse_btn = "left"
	case "r":
		mouse_btn = "right"
	case _:
		mouse_btn = "left"

clicking = False

print("R Shift - toggle clicking")
print("Ctrl + Esc - exit the program")


def click_loop():
	global clicking
	while True:
		if clicking:
			pyautogui.mouseDown(button="right")
			time.sleep(0.01)
			pyautogui.mouseUp(button="right")
			time.sleep(delay)
		else:
			time.sleep(0.01)


def on_press(key, injected):
	global clicking
	if key == keyboard.Key.shift_r:
		clicking = not clicking


def on_exit_activated():
	exit(0)


thread = threading.Thread(target=click_loop, daemon=True)
thread.start()


listener = keyboard.Listener(
    on_press=on_press)
listener.start()


with keyboard.GlobalHotKeys({
		"<ctrl>+<esc>": on_exit_activated}) as h:
	h.join()
