import cv2
import numpy as np
import tkinter, tkinter.filedialog

# Open tkinter filedialog window to select paths
root = tkinter.Tk()
root.withdraw()

print('Select first image')
path1 = tkinter.filedialog.askopenfilename()
print('Select second image')
path2 = tkinter.filedialog.askopenfilename()

root.destroy()

# load images
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

def interleave(first, second):
    """
    Takes pixels in checkerboard pattern from second image to replace the pixels from the first image.
    :param first: numpy array that represents a matrix of pixels from an image
    :param second: numpy array that represents a matrix of pixels from an image the same size as the first image (doesn't fail if not the case)
    :return: numpy array that represents a matrix of pixels from an image, but pixels have been interleaved in checkerboard pattern
    """
    # get image size
    height = len(first)
    width = len(first[0])

    # create copy of the original array
    res = np.array(first, copy=True)

    # set the pixels equal to the pixels of the second image in checkerboard pattern 
    for row in range(height):
        for col in range(width):
            if ((col + row) % 2 != 0):
                res[row][col] = second[row][col]
    
    return res

##########

modified = interleave(img1, img2)

cv2.imshow('image', modified)
cv2.waitKey(0)
cv2.destroyAllWindows()