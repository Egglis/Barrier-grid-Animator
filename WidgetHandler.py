# Libraries
from tkinter import filedialog

# Local Imports
from Widgets.PreviewWidget import PreviewWidget
from Widgets.TimeStepWidget import TimeStepWidget
from Widgets.MenuBarWidget import MenuBarWidget
from Animator import  GridAnimator

# Handles the interactions between each of the widgets
class WidgetHandler:
    window = None

    menuBar = None
    canvas = None
    timeStep = None

    animator = GridAnimator()

    def __init__(self, window):
        self.window = window

        self.menuBar = MenuBarWidget(window, self)
        self.canvas = PreviewWidget(window, self)
        self.timeStep = TimeStepWidget(window, self)

        self.__setupWidgets()

    def __setupWidgets(self):
        self.menuBar.setupWidget()
        self.canvas.setupWidget()
        self.timeStep.setupWidget()

    # Functions for interactions
    def onTimeStepChange(self, sliderValue):
        # SliderValue 0-5
        self.canvas.moveMask(sliderValue, self.animator.hatch_width)

    def onFileSelection(self):
        file_path = filedialog.askopenfilename()
        composite_img = self.animator.makeCompositeImage(file_path)
        mask = self.animator.makeBarMask(self.canvas.viewport)

        self.canvas.updateImage(composite_img)
        self.canvas.updateMask(mask)

        self.timeStep.setFromTo(0, self.animator.numFrames)
