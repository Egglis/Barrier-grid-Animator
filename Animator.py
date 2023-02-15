# Process:
# 1. Black/White each frame of a "gif", (Might be optional, we will see)
# 2. Then Hatch vertical lines into the image
# 3. Then combine in the hatched frames into a composite image


## Key option
# - Hatch with - Should match the "mask" which is overlayed

from PIL import Image, ImageTk, ImageDraw
from Functions import vec
import numpy as np
import tkinter as tk
from matplotlib import pyplot as plt

class GridAnimator:
    hatch_width = 2
    hatch_spacing = 10
    total_hatches = 50

    currentSize = None
    numFrames = 0

    def __hatchFrame(self, frame):
        # Return a hatched frame
        pass

    def __combineFrames(self, frames):
        # Combined each frame into a composite image for displaying
        pass

    def makeCompositeImage(self, filename):
        sequence = Image.open(filename)
        sequence.seek(0)

        new_image = Image.new("RGBA", sequence.size, (0, 0, 0, 0))

        self.currentSize = vec(sequence.size[0], sequence.size[1])
        self.numFrames = sequence.n_frames

        col = 0
        while col < self.currentSize.x:
            for i in range(self.numFrames):
                sequence.seek(i)
                for j in range(self.hatch_width):
                    if col < sequence.width:
                        for row in range(self.currentSize.y):
                            new_image.putpixel((col, row), sequence.getpixel((col,row)))
                    col += 1

        return ImageTk.PhotoImage(new_image)


    def makeBarMask(self, viewport):
        img_mask = Image.new("RGBA", (viewport.x, viewport.y), (0, 0, 0, 0))
        new_mask = ImageDraw.Draw(img_mask)
        x = 0
        for i in range(int(viewport.x / self.hatch_width)):
            new_mask.rectangle((x, 0, x + self.hatch_width*(self.numFrames-1), viewport.y), fill="#000000ff")
            x += self.hatch_width*(self.numFrames-1) + self.hatch_width
        return ImageTk.PhotoImage(img_mask)


def makeBarrierGridAnimation(filename):
    gif = Image.open(filename)
    for frame in range(0, gif.n_frames):
        gif.seek(frame)

        curr_frame = gif.copy()



# ()
"""
	
	baseImage = QImage(size0, QImage::Format_ARGB32_Premultiplied);
	
	/* go from left to right through baseImage. Write k columns of each
	 * image again and again.
	 */
	for ( int col=0 ; col<size0.width() ; )
		for ( int i=0 ; i<nrImgs ; i++ )
			for ( int j=0 ; j<stripWidth && col<size0.width() ; j++, col++ ) {
				pbar->setValue(col+1);
				for ( int row=0 ; row<size0.height() ; row++ )
					baseImage.setPixel(col, row, imgs[i]->pixel(col, row));
			}
	
	/*
	 * then, compute barmask
	 */
	
	barMask = QImage(size0, QImage::Format_Mono);
	for ( int col=0 ; col < size0.width() ; )
		for ( int i=0 ; i<nrImgs ; i++ )
			for ( int j=0 ; j<stripWidth && col<size0.width() ; j++, col++ ) {
				pbar->setValue(size0.width()+col+1);
				for ( int row=0 ; row < size0.height() ; row++ )
					barMask.setPixel(col, row, (i == 0) ? 1 : 0 );
			}
			
	/* image is the one displayed on imageLabel */
	
	image = QImage(size0, QImage::Format_ARGB32_Premultiplied);
	
	/* remove progress bar again */
	statusBar()->removeWidget(pbar);
	delete pbar;

"""
