import math
import tkinter

from PIL import Image, ImageTk, ImageDraw, ImageSequence
from Functions import vec, scaleImageToViewPort
from tkinter import ttk

class GridAnimator:
    hatch_width = 2
    hatch_spacing = 10
    total_hatches = 50

    targetFrames = None

    currentFile = None
    currentSequence = None
    currentSize = None
    numFrames = 0
    filterIntensity = 0.5

    currentColor = str()

    def loadFile(self, filename, viewport):
        self.currentFile = filename
        self.currentSequence = Image.open(self.currentFile)
        self.numFrames = self.currentSequence.n_frames
        self.currentSize = scaleImageToViewPort(viewport, vec(self.currentSequence.size[0], self.currentSequence.size[1]))
        return self.currentSize.x
    

    def setCurrentFilter(self, color):
        self.currentColor = color

    # Generates the final image
    def makeCompositeImage(self, progress_bar : ttk.Progressbar):

        # Base Image
        new_image = Image.new("RGBA", (self.currentSize.x, self.currentSize.y), (0, 0, 0, 0))

        # Frames to include
        includedFrames = self.reduceNumberOfFrames()

        # Generate the composite image
        col = 0
        steps = 0
        while col < self.currentSize.x:
            frameIndex = 0
            for frame in ImageSequence.Iterator(self.currentSequence):
                if frameIndex in includedFrames:
                    # Resize the current frame and change the coloring mode into RGBA
                    frame = frame.resize((self.currentSize.x, self.currentSize.y))
                    frame = frame.convert("RGBA")

                    for j in range(self.hatch_width):
                        if col < self.currentSize.x:
                            for row in range(self.currentSize.y-1):
                                # Blend based on color TODO
                                
                                new_image.putpixel((col, row), frame.getpixel((col, row)))

                            col += 1
                            steps += 1
                            progress_bar.step(100/self.currentSize.x)

                frameIndex += 1
        return ImageTk.PhotoImage(new_image)

    # Applies the filter to the image
    def applyFilter(self, pixelColor):
        pixelColor = list(pixelColor)
        if self.currentColor == "red":
            pixelColor[0] = min(255, max(0, int(pixelColor[0] * self.filterIntensity)))
        elif self.currentColor == "green":
            pixelColor[1] = min(255, max(0, int(pixelColor[1] * self.filterIntensity)))
        elif self.currentColor == "blue":
            pixelColor[2] = min(255, max(0, int(pixelColor[2] * self.filterIntensity)))
        return tuple(pixelColor)

    # Generates the mask/bars for the final image
    def makeBarMask(self, viewport):
        img_mask = Image.new("RGBA", (viewport.x, viewport.y), (0, 0, 0, 0))
        new_mask = ImageDraw.Draw(img_mask)
        x = 0

        if self.targetFrames is not None:
            self.numFrames = self.targetFrames

        for i in range(int(viewport.x / self.hatch_width)):
            new_mask.rectangle((x, 0, x + self.hatch_width*(self.numFrames-1), viewport.y), fill="#000000FF")
            x += self.hatch_width*(self.numFrames-1) + self.hatch_width
        return ImageTk.PhotoImage(img_mask)

    # Frame reduction alogirthm, skips n frames
    def reduceNumberOfFrames(self):
        print("Number of Frames: ", self.numFrames)
        includedFrames = list()
        if self.targetFrames is None:
            includedFrames = range(self.numFrames)
            return includedFrames

        if self.targetFrames > self.numFrames:
            includedFrames = range(self.numFrames)
            self.targetFrames = None
        else:
            framesToSkip = math.ceil(self.numFrames / self.targetFrames)

            for i in range(self.numFrames)[0:self.numFrames:framesToSkip]:
                includedFrames.append(i)
            includedFrames.append(self.numFrames)
        return includedFrames
