
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


def reMap(value, oldMin, oldMax, newMin, newMax):
    OldRange = (oldMax - oldMin)
    NewRange = (newMax - newMin)
    return (((value - oldMin) * NewRange) / OldRange) + newMin
