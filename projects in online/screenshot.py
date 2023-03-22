import time
import pyautogui
import tkinter as tk # for gui purpose

def screenshot():
    name = int(round(time.time()*10000))
    name = 'C:/Users/Cyber/OneDrive/Documents/projects in online/screenshot of deskop/{}.png'.format(name)
    #time.sleep(2)
    img = pyautogui.screenshot(name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button = tk.Button(
    frame,
    text = "take the screenshot",
    command = screenshot
)

button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text = "exit",
    command = quit)
button.pack(side =tk.BOTTOM)
stop = tk.Button(
    frame,
    text = 'stop',
    command = 'stop'
)
close.pack(side = tk.LEFT)
stop.pack(side = tk.BOTTOM)
root.mainloop()