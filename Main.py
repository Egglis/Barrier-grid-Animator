import tkinter as tk  # Python3
from WidgetHandler import WidgetHandler

window = tk.Tk()
window.geometry("1280x720")
# 1290x720, 1280x720
widgetHandler = WidgetHandler(window)

window.bind("<Configure>", widgetHandler.on_resize)

window.mainloop()

print("Window Closed")

# Future Plans:
# TODO Make more options for testing diffirent configurations
# TODO Attempt a cricle barrier gird animation
# TODO Cross-Fading gifs

