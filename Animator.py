import math

from PIL import Image, ImageTk, ImageDraw, ImageSequence
from Functions import vec, scaleImageToViewPort
from tkinter import ttk

class GridAnimator:
    hatch_width = 2
    hatch_spacing = 10
    total_hatches = 50

    currentSize = None
    numFrames = 0
    targetFrames = None

    progressBar = None

    def initProgressBar(self, window):
        self.progressBar = ttk.Progressbar(window, orient="horizontal", mode="determinate")
        #self.progressBar.pack(fill="x")
        pass

    def makeCompositeImage(self, filename, viewport):
        sequence = Image.open(filename)

        # Set Current Information
        self.numFrames = sequence.n_frames
        self.currentSize = scaleImageToViewPort(viewport, vec(sequence.size[0], sequence.size[1]))

        # Base Image
        new_image = Image.new("RGBA", (self.currentSize.x, self.currentSize.y), (0, 0, 0, 0))


        includedFrames = self.reduceNumberOfFrames()

        col = 0
        while col < self.currentSize.x:
            frameIndex = 0
            for frame in ImageSequence.Iterator(sequence):
                if frameIndex in includedFrames:
                    # Resize the current frame and change the coloring mode into RGBA
                    frame = frame.resize((self.currentSize.x, self.currentSize.y))
                    frame = frame.convert("RGBA")

                    for j in range(self.hatch_width):
                        if col < self.currentSize.x:
                            for row in range(self.currentSize.y-1):
                                new_image.putpixel((col, row), frame.getpixel((col, row)))
                            col += 1

                frameIndex += 1
        return ImageTk.PhotoImage(new_image)


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


    def reduceNumberOfFrames(self):
        print("Number of Frames: ", self.numFrames)
        includedFrames = list()
        if self.targetFrames > self.numFrames:
            includedFrames = range(self.numFrames)
            self.targetFrames = None
        else:
            framesToSkip = math.ceil(self.numFrames / self.targetFrames)

            for i in range(self.numFrames)[0:self.numFrames:framesToSkip]:
                includedFrames.append(i)
            includedFrames.append(self.numFrames)
        return includedFrames
