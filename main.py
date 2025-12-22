import threading
import time

from pynput import keyboard
from pynput.mouse import Controller, Button

mouse = Controller()

interval = float(input("Interval (secs): "))
mouse_btn = input("Mouse button l - left, r - right: ").lower()
match mouse_btn:
	case "l":
		mouse_btn = Button.left
	case "r":
		mouse_btn = Button.right
	case _:
		mouse_btn = Button.left

clicking = False

print("R Shift - toggle clicking")
print("Ctrl + Esc - exit the program")


def click_loop():
	global clicking
	while True:
		if clicking:
			mouse.click(mouse_btn, 1)
			time.sleep(interval)
		else:
			time.sleep(0.5)


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
