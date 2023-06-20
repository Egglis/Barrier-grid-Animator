import tkinter

from Widgets.WidgetInterface import Widget
from tkinter import Scale

# The timestep/timeline widget
class TimeStepWidget(Widget):
    def setupWidget(self):
        self.obj = Scale(self.root, length=720, orient="horizontal")
        #.obj.pack(side=tkinter.TOP, fill=tkinter.X)
        self.obj.grid(row=1, column=1)
        self.obj.config(command=self.handler.onTimeStepChange)

    def setFromTo(self, from_, to):
        self.obj.config(from_=from_, to=to)

    def setValue(self, value):
        self.obj.set(value)