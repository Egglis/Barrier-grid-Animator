
from Widgets.WidgetInterface import Widget
import tkinter as tk

# Widgets for all the option on the left side of the GUI
class OptionsWidget(Widget):

    hideMask = None
    isMaskHidden = None

    reloadButton = None

    redButton = None
    greenButton = None
    blueButton = None

    hideFilter = None
    isFilterActive = False
    filterSlider = None

    def setupWidget(self):
        self.obj = tk.Frame(self.root)
        self.obj.grid(row=0, column=0)
        self.hideMaskOption()
        self.reloadOption()
        self.colorOptions()
        self.hideFilter()
        self.filterSlider()

    def hideMaskOption(self):
        self.isMaskHidden = tk.BooleanVar()

        self.hideMask = tk.Checkbutton(self.obj, text="Hide Mask", variable=self.isMaskHidden)
        self.hideMask.pack()

        self.hideMask.config(command=self.handler.onMaskHide)

    def reloadOption(self):
        self.reloadButton = tk.Button(self.obj, text="Reload Image")
        self.reloadButton.pack()

        self.reloadButton.config(command=self.handler.reloadImage)

    def colorOptions(self):
        self.redButton = tk.Button(self.obj, text="Red")
        self.redButton.pack()

        self.redButton.config(command=lambda: self.handler.onFilterChange("red"))

        self.greenButton = tk.Button(self.obj, text="Green")
        self.greenButton.pack()

        self.greenButton.config(command=lambda: self.handler.onFilterChange("green"))

        self.blueButton = tk.Button(self.obj, text="Blue")
        self.blueButton.pack()

        self.blueButton.config(command=lambda: self.handler.onFilterChange("blue"))

    def hideFilter(self):
        self.isFilterActive = tk.BooleanVar()

        self.hideFilter = tk.Checkbutton(self.obj, text="Hide Filter", variable=self.isFilterActive)
        self.hideFilter.pack()

        self.hideFilter.config(command=self.handler.onFilterHide)

    def filterSlider(self):
        self.filterSlider = tk.Scale(self.obj, from_=0, to=255, orient=tk.HORIZONTAL)
        self.filterSlider.pack()

        self.filterSlider.config(command=self.handler.onFilterMove)

    def updateFilterButtons(self, color):
        if color == "red":
            if self.redButton.cget("background") == "red":
                self.redButton.config(background="white")
            else:
                self.redButton.config(background="red")
        elif color == "green":
            if self.greenButton.cget("background") == "green":
                self.greenButton.config(background="white", foreground="black")
            else:
                self.greenButton.config(background="green", foreground="white")
        elif color == "blue":
            if self.blueButton.cget("background") == "blue":
                self.blueButton.config(background="white", foreground="black")
            else:
                self.blueButton.config(background="blue", foreground="white")