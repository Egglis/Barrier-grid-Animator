# Libraries
from tkinter import filedialog

# Local Imports
from Widgets.PreviewWidget import PreviewWidget
from Widgets.TimeStepWidget import TimeStepWidget
from Widgets.MenuBarWidget import MenuBarWidget
from Widgets.OptionsWidget import OptionsWidget
from Animator import  GridAnimator

# Handles the interactions between each of the widgets
class WidgetHandler:
    window = None

    menuBar = None
    canvas = None
    timeStep = None
    options = None

    animator = GridAnimator()

    def __init__(self, window):
        self.window = window

        self.menuBar = MenuBarWidget(window, self)
        self.canvas = PreviewWidget(window, self)
        self.timeStep = TimeStepWidget(window, self)
        self.options = OptionsWidget(window, self)

        self.__setupWidgets()

    def __setupWidgets(self):
        self.menuBar.setupWidget()
        self.canvas.setupWidget()
        self.timeStep.setupWidget()
        self.options.setupWidget()



    # Functions for interactions
    def onTimeStepChange(self, sliderValue):
        self.canvas.moveMask(sliderValue, self.animator.hatch_width)

    def onFileSelection(self):
        file_path = filedialog.askopenfilename()
        composite_img = self.animator.makeCompositeImage(file_path, self.canvas.viewport)
        mask = self.animator.makeBarMask(self.canvas.viewport)

        self.canvas.updateImage(composite_img)
        self.canvas.updateMask(mask)

        self.timeStep.setValue(0)
        self.timeStep.setFromTo(0, self.canvas.viewport.x)

    def onMaskHide(self):
        self.canvas.hideMask(self.options.isMaskHidden.get())