from Functions import vec
from PIL import  Image, ImageDraw, ImageTk

class ColorFilter:


    filters = {
        "Red": vec(255, 0, 0, 0),
        "Green": vec(0, 255, 0, 0),
        "Blue": vec(0, 0, 255, 0)
    }
    currentFilter = vec(0, 0, 0, 0)

    def __init__(self):
        pass

    # Adds a color to the filter
    def addFilter(self, color: str):
        pass

    def updateFilter(self, color: str):
        pass

    # Removes a color from the filter
    def removeFilter(self, color: str):
        pass

    # Should return the current filter, which can be a combination of several filters
    def getFilter(self, viewport: vec):
        img_filter = Image.new("RGBA", (viewport.x, viewport.y), (0, 0, 0, 0))
        new_filter = ImageDraw.Draw(img_filter)

        new_filter.rectangle((0, 0, viewport.x, viewport.y), fill=(255, 0, 0, 25))

        return ImageTk.PhotoImage(img_filter)