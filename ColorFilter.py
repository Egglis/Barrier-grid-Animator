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
        # add either red, green or blue to current filter
        if color == "red":
            if self.currentFilter.x == 0:
                self.currentFilter.x = 255
            else:
                self.currentFilter.x = 0
        elif color == "green":
            if self.currentFilter.y == 0:
                self.currentFilter.y = 255
            else:
                self.currentFilter.y = 0
        elif color == "blue":
            if self.currentFilter.z == 0:
                self.currentFilter.z = 255
            else:
                self.currentFilter.z = 0

    def updateFilter(self, color: str):
        pass

    # Removes a color from the filter
    def removeFilter(self, color: str):
        # remove either red, green or blue from current filter
        if color == "red":
            self.currentFilter.x = 0
        elif color == "green":
            self.currentFilter.y = 0
        elif color == "blue":
            self.currentFilter.z = 0

    # Returns the current filter
    def getFilter(self, viewport: vec):
        img_filter = Image.new("RGBA", (viewport.x, viewport.y), (0, 0, 0, 0))
        new_filter = ImageDraw.Draw(img_filter)

        new_filter.rectangle((0, 0, viewport.x, viewport.y), fill=(self.currentFilter.x, self.currentFilter.y, self.currentFilter.z, 25))
        print("Filter: ", self.currentFilter)
        return ImageTk.PhotoImage(img_filter)