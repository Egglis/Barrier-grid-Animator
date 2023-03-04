
from Widgets.WidgetInterface import Widget
import tkinter as tk

class OptionsWidget(Widget):

    hideMask = None
    isMaskHidden = None

    reloadButton = None

    def setupWidget(self):
        self.obj = tk.Frame(self.root)
        self.obj.grid(row=0, column=0)
        self.hideMaskOption()
        self.reloadOption()

    def hideMaskOption(self):
        self.isMaskHidden = tk.BooleanVar()

        self.hideMask = tk.Checkbutton(self.obj, text="Hide Mask", variable=self.isMaskHidden)
        self.hideMask.pack()

        self.hideMask.config(command=self.handler.onMaskHide)

    def reloadOption(self):
        self.reloadButton = tk.Button(self.obj, text="Reload Image")
        self.reloadButton.pack()

        self.reloadButton.config(command=self.handler.reloadImage)