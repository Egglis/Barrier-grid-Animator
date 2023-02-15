from Widgets.WidgetInterface import Widget
from tkinter import Canvas
from Functions import vec, reMap

class PreviewWidget(Widget):
    viewport = vec(1280, 720)

    image = None
    image_id = 0

    mask = None
    mask_id = 0
    prevMaskStep = 0

    def setupWidget(self):
        self.obj = Canvas(self.root, width=self.viewport.x, height=self.viewport.y, background="white")
        self.obj.pack()

    def updateImage(self, image):
        self.image = image
        x = (self.viewport.x * 0.5) - (image.width() * 0.5)
        y = (self.viewport.y * 0.5) - (image.height() * 0.5)
        self.image_id = self.obj.create_image(x, y, anchor="nw", image=image)

    def updateMask(self, mask):
        self.mask = mask
        #x = (self.viewport.x * 0.5) - (mask.width() * 0.5)
        #y = (self.viewport.y * 0.5) - (mask.height() * 0.5)

        self.mask_id = self.obj.create_image(0, 0, anchor="nw", image=mask)
        #self.obj.create_rectangle(0, 0, self.width, self.height, fill="#aa0000")

    def moveMask(self, sliderValue, hatchWidth):
        value = int(sliderValue) - self.prevMaskStep
        self.obj.move(self.mask_id, value*hatchWidth, 0)
        self.prevMaskStep = int(sliderValue)