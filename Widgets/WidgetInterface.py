

# A general widget interface
class Widget:
    root = None
    obj = None
    handler = None

    def __init__(self, window, handler):
        self.root = window
        self.handler = handler