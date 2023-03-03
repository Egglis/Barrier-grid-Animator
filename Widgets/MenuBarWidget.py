from Widgets.WidgetInterface import Widget
from tkinter import Menu

class MenuBarWidget(Widget):

    file_menu = None

    def setupWidget(self):
        self.obj = Menu(self.root)
        self.root.config(menu=self.obj)
        self.__initFileMenu()

    def __initFileMenu(self):
        self.file_menu = Menu(self.obj, tearoff=0)
        self.file_menu.add_command(label="Open", command=lambda: self.handler.openFileSelectionMenu())
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        self.obj.add_cascade(label="File", menu=self.file_menu)