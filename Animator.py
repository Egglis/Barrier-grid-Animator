from PIL import Image, ImageTk, ImageDraw, ImageSequence
from Functions import vec

def calcNewSize(viewport, current):
    aspectRatio = current.x / current.y
    new_size = current
    if current.x < viewport.x or current.y < viewport.y:
        if (viewport.x / aspectRatio) < viewport.y:
            new_size.x = viewport.x
            new_size.y = int(new_size.x / aspectRatio)
        else:
            new_size.y = viewport.y
            new_size.x = int(new_size.y * aspectRatio)
    else:

        new_size.x = current.x
        new_size.y = current.y
    return new_size


class GridAnimator:
    hatch_width = 2
    hatch_spacing = 10
    total_hatches = 50

    currentSize = None
    numFrames = 0

    def makeCompositeImage(self, filename, viewport):
        sequence = Image.open(filename)

        # Set Current Information
        self.numFrames = sequence.n_frames
        self.currentSize = calcNewSize(viewport, vec(sequence.size[0], sequence.size[1]))

        # Base Image
        new_image = Image.new("RGBA", (self.currentSize.x, self.currentSize.y), (0, 0, 0, 0))

        col = 0
        while col < self.currentSize.x:
            for frame in ImageSequence.Iterator(sequence):

                # Resize the current frame and change the coloring mode into RGBA
                frame = frame.resize((self.currentSize.x, self.currentSize.y))
                frame = frame.convert("RGBA")

                for j in range(self.hatch_width):
                    if col < self.currentSize.x:
                        for row in range(self.currentSize.y-1):
                            new_image.putpixel((col, row), frame.getpixel((col, row)))
                        col += 1



        return ImageTk.PhotoImage(new_image)


    def makeBarMask(self, viewport):
        img_mask = Image.new("RGBA", (viewport.x, viewport.y), (0, 0, 0, 0))
        new_mask = ImageDraw.Draw(img_mask)
        x = 0
        for i in range(int(viewport.x / self.hatch_width)):
            new_mask.rectangle((x, 0, x + self.hatch_width*(self.numFrames-1), viewport.y), fill="#000000FF")
            x += self.hatch_width*(self.numFrames-1) + self.hatch_width
        return ImageTk.PhotoImage(img_mask)

