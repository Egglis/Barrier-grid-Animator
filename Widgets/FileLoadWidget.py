from Widgets.WidgetInterface import Widget
import  tkinter as tk

# Widget for loading a file and reducing frames if needed
class FileLoaderWidget(Widget):

    frameReduction = True


    selectFileButton = None
    nrFramesSlider = None
    nrFramesCheckbox = None
    nrFramesVar = None

    def setupWidget(self):
        self.obj = tk.Toplevel(self.root)
        self.obj.title("File Loading")

        self.nrFramesVar = tk.BooleanVar()
        self.nrFramesVar.set(True)

        self.nrFramesCheckbox = tk.Checkbutton(self.obj,
                                               text="Enable Frame reduction",
                                               variable=self.nrFramesVar)
        self.nrFramesCheckbox.pack()

        self.nrFramesSlider = tk.Scale(self.obj, from_=2, to=10,
                                       orient=tk.HORIZONTAL,
                                       label="Nr Frames:",
                                       state=tk.NORMAL)
        self.nrFramesSlider.set(6)
        self.nrFramesSlider.pack()

        self.selectFileButton = tk.Button(self.obj, text="Select File", command=self.handler.onFileSelection)
        self.selectFileButton.pack()

    def on_nrFramesCheckbox(self):
        if self.nrFramesVar.get():
            self.nrFramesSlider.config(state=tk.NORMAL)
        else:
            self.nrFramesSlider.config(state=tk.DISABLED)

    def destroyWindow(self):
        self.obj.destroy()
