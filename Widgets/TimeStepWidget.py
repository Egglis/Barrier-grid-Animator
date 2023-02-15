from Widgets.WidgetInterface import Widget
from tkinter import Scale

class TimeStepWidget(Widget):
    def setupWidget(self):
        self.obj = Scale(self.root, length=720, orient="horizontal")
        self.obj.pack()
        self.obj.config(command=self.handler.onTimeStepChange)

    def setFromTo(self, from_, to):
        self.obj.config(from_=from_, to=to)
