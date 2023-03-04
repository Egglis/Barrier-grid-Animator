
# Just a simple vec2-4 class for better syntax in the rest of the program
class vec:
    x, y, z, w, r, g, b, a = None, None, None, None, None, None, None, None
    size = None
    n = 2
    def __init__(self, x, y, z=None, w=None):
        self.x = x
        self.y = y

        self.a = x
        self.g = y

        self.size = (x, y)

        if z is not None:
            self.z = z
            self.b = z
            self.n += 1
        if w is not None:
            self.w = w
            self.a = w
            self.n += 1
    def __str__(self):
        if self.n == 2:
            return "({0},{1})".format(self.x, self.y)
        elif self.n == 3:
            return "({0},{1},{2})".format(self.x, self.y, self.z)
        elif self.n == 4:
            return "({0},{1},{2},{3})".format(self.x, self.y, self.z, self.w)


# Your basic re-map function, most likely a package for this :(
def reMap(value, oldMin, oldMax, newMin, newMax):
    OldRange = (oldMax - oldMin)
    NewRange = (newMax - newMin)
    return (((value - oldMin) * NewRange) / OldRange) + newMin

def scaleImageToViewPort(viewport, current):
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
