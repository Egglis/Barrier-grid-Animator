import tkinter as tk  # Python3

from WidgetHandler import WidgetHandler

window = tk.Tk()
window.geometry("1280x720")
# 1290x720, 1280x720
widgetHandler = WidgetHandler(window)

window.bind("<Configure>", widgetHandler.on_resize)

window.mainloop()

print("Window Closed")

# Plan/Uml
# TODO For the LOVE OF GOD PLEASE KEEP THE FILES as SHORT as POSSIBLE, pytho  /: 
# TODO MAKE more options for testing different stuff
# TODO Try out blurred images??
# TODO Try using colored overlays as shown in the paper in the pdf
# TODO Try circle mask instead
# TODO Look into cross fading gifs then frame reduction???
# TODO Apply Color filter  

