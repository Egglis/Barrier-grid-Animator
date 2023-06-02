import tkinter

from Widgets.WidgetInterface import Widget
from PIL import Image, ImageTk, ImageDraw, ImageSequence
from tkinter import Canvas
from Functions import vec, reMap

class CanvasWidget(Widget):
    viewport = vec(1280, 720)

    image = None
    image_id = 0

    mask = None
    mask_id = 0
    prevMaskStep = 0

    colorFilter = None
    colorFilter_id = 0

    def setupWidget(self):
        self.obj = Canvas(self.root, background="white")
        #, width=self.viewport.x, height=self.viewport.y
        self.obj.grid(row=0, column=1, sticky="sewn", padx=10, pady=20)

    def updateViewport(self):
        w = self.obj.winfo_width()
        h = self.obj.winfo_height()

        self.viewport = vec(w, h)

    def updateImage(self, image):
        self.image = image
        x = (self.viewport.x * 0.5) - (image.width() * 0.5)
        y = (self.viewport.y * 0.5) - (image.height() * 0.5)
        self.image_id = self.obj.create_image(x, y, anchor="nw", image=image)

    def updateMask(self, mask):
        self.mask = mask
        self.mask_id = self.obj.create_image(0, 0, anchor="nw", image=mask)

    def updateFilter(self, colorFilter):
        self.colorFilter = colorFilter
        self.colorFilter_id = self.obj.create_image(0, 0, anchor="nw", image=colorFilter)
        self.obj.itemconfigure(tagOrId=self.colorFilter_id, image=self.colorFilter)

    def hideMask(self, hidden):
        if hidden:
            self.obj.itemconfig(self.mask_id, state="hidden")
        else:
            self.obj.itemconfig(self.mask_id, state="normal")

    def moveMask(self, sliderValue, hatchWidth):
        value = int(sliderValue) - self.prevMaskStep
        self.obj.move(self.mask_id, value, 0)
        self.prevMaskStep = int(sliderValue)

    def hideFilter(self, hidden):
        if hidden:
            self.obj.itemconfig(self.colorFilter_id, state="hidden")
        else:
            self.obj.itemconfig(self.colorFilter_id, state="normal")