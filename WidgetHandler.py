# Libraries
from tkinter import filedialog
from Functions import vec

# Local Imports
from Widgets.CanvasWidget import CanvasWidget
from Widgets.TimeStepWidget import TimeStepWidget
from Widgets.MenuBarWidget import MenuBarWidget
from Widgets.OptionsWidget import OptionsWidget
from Widgets.FileLoadWidget import FileLoaderWidget
from Animator import  GridAnimator
from ColorFilter import ColorFilter

# Handles the interactions between each of the widgets
class WidgetHandler:
    window = None

    menuBar = None
    canvas = None
    timeStep = None
    options = None
    loadPopup = None

    animator = GridAnimator()
    filter = ColorFilter()

    currentFile = None

    def __init__(self, window):
        self.window = window

        self.animator.initProgressBar(window)
        self.menuBar = MenuBarWidget(window, self)
        self.canvas = CanvasWidget(window, self)
        self.timeStep = TimeStepWidget(window, self)
        self.options = OptionsWidget(window, self)
        self.loadPopup = FileLoaderWidget(window, self)

        self.__setupWidgets()

    def __setupWidgets(self):
        self.menuBar.setupWidget()
        self.canvas.setupWidget()
        self.timeStep.setupWidget()
        self.options.setupWidget()

    def on_resize(self, event):

        self.window.columnconfigure(1, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.canvas.updateViewport()

    # Functions for interactions
    def onTimeStepChange(self, sliderValue):
        self.canvas.moveMask(sliderValue, self.animator.hatch_width)

    def openFileSelectionMenu(self):
        self.loadPopup.setupWidget()

    def reloadImage(self):
        self.loadImage()

    def loadImage(self):
        # Make composite image and the mask
        composite_img = self.animator.makeCompositeImage(self.currentFile, self.canvas.viewport)
        mask = self.animator.makeBarMask(self.canvas.viewport)
        colorFilter = self.filter.getFilter(self.canvas.viewport)

        # Update Canvas
        self.canvas.updateImage(composite_img)
        self.canvas.updateMask(mask)
        self.canvas.updateFilter(colorFilter)

        self.timeStep.setValue(0)
        self.timeStep.setFromTo(0, self.canvas.viewport.x)

    def onFileSelection(self):

        file_path = filedialog.askopenfilename()
        self.currentFile = file_path
        # Set the target frames and None if no frame reduction is used
        targetFrames = self.loadPopup.nrFramesSlider.get()
        if not self.loadPopup.nrFramesVar.get():
            self.animator.targetFrames = None
        else:
            self.animator.targetFrames = targetFrames

        self.loadImage()

        self.loadPopup.destroyWindow()

    def onMaskHide(self):
        self.canvas.hideMask(self.options.isMaskHidden.get())