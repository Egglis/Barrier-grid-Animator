
from Widgets.WidgetInterface import Widget
import tkinter as tk

class OptionsWidget(Widget):

    hideMask = None
    isMaskHidden = None

    def setupWidget(self):
        self.obj = tk.Frame(self.root)
        self.obj.pack()

        self.isMaskHidden = tk.BooleanVar()

        self.hideMask = tk.Checkbutton(self.obj, text="Hide Mask", variable=self.isMaskHidden)
        self.hideMask.pack(side="left", fill="y")

        self.hideMask.config(command=self.handler.onMaskHide)

