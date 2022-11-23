from init import win
from functions.close_win import close_win
from functions.start import start
import keyboard
from functions.easter_egg import easteregg

# escape to exit
win.bind('<Escape>', lambda e: close_win())

# Easter egg when type harry
keyboard.add_hotkey('h,a,r,r,y', lambda: easteregg(), suppress=True, trigger_on_release=True, timeout=2)

start()

win.mainloop()
