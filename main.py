import cv2
import numpy as np
import tkinter, tkinter.filedialog
import os

# Open tkinter filedialog window to select paths
root = tkinter.Tk()
root.withdraw()

print('Select first image')
path1 = tkinter.filedialog.askopenfilename()
print('Select second image')
path2 = tkinter.filedialog.askopenfilename()

print('Processing...')

root.destroy()

# load images
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

def interleave(first, second):
    """
    Takes pixels in checkerboard pattern from second image to replace the pixels from the first image.
    :param first: numpy array that represents a matrix of pixels from the first image
    :param second: numpy array that represents a matrix of pixels from the second image the same size as the first image
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

def preprocess(first, second):
    """
    Sets the size of both images equal by taking the smallest width and height and thus cutting off other pixels.
    :param first: numpy array that represents a matrix of pixels from the first image
    :param second: numpy array that represents a matrix of pixels from the second image
    :return: two numpy arrays with containing modified images
    """

    # get image size
    height1 = len(first)
    width1 = len(first[0])
    height2 = len(second)
    width2 = len(second[0])

    # Minimum size
    height_min = min(height1, height2)
    width_min = min(width1, width2)

    # initialize new arrays
    first_mod = np.empty([height_min, width_min, 3]) # 3 because RGB
    second_mod = np.empty([height_min, width_min, 3])

    # Set pixels of both images
    for row in range(height_min):
        for col in range(width_min):
            first_mod[row][col] = first[row][col]
            second_mod[row][col] = second[row][col]
    
    return first_mod, second_mod



##########

mod1, mod2 = preprocess(img1, img2)

modified = interleave(mod1, mod2)

# # # Show image
# # cv2.imshow('image', modified)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# Set working directory to save location
image_dir = '/'.join(path1.split('/')[:-1]) + '/'
os.chdir(image_dir)

cv2.imwrite('interleaved.jpg', modified)

print('Successfully saved at: ', image_dir)