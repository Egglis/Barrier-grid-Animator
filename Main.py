import tkinter as tk  # Python3

from WidgetHandler import WidgetHandler

window = tk.Tk()
window.geometry("1280x720")
widgetHandler = WidgetHandler(window)

window.mainloop()

## More Plans
# Make backgorund customizable
# Make sliders for bar widths etc

# Plan/Uml
# TODO For the LOVE OF GOD PLEASE KEEP THE FILES as SHORT as POSSIBLE, pytho  /: 
# TODO Make a custom widget for every single gui options
# Main.py
#   - C: Canvas
#       - update()
#   - C: Ui
#       - Get Xsetting()
#       - Set Xsetting()
#       - OnUiChange() -> Call Canvas.update()
#   - C: FileLoader
#       - getImage(timeStep)
#       - loadFile(fileName)  
#   - C: Animator -> Does the magic 
#       - ComputeNewImage()
#       + FindEdge()
#       + LookForPossibleOptimizations()
#       + 
##

