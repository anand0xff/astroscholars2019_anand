#! /usr/bin/env python
"""
    Code to split a jpg image into R,G,B channels and write them as fits files

    After  https://www.codementor.io/@innat_2k14/image-data-analysis-using-numpy-opencv-part-1-kfadbafx6 
    Written to support AstroScholars 2019
    started: anand@stsci.edu December 2019
"""
import os, sys
import imageio
import numpy as np
from astropy.io import fits
#%matplotlib inline
import matplotlib.pyplot as plt


def fitsorder(jarr):
    """
    Take jpg order jarr of shape (h,w,3) and return farr, fits-ordered array (3,w,h)
    Assumes type uint8 arrays
    """
    farr = np.zeros((jarr.shape[2], jarr.shape[1], jarr.shape[0]), np.uint8)
    for cc in range(jarr.shape[2]):  # for each color in r, g, b...
        for ww in range(jarr.shape[1]):
            for hh in range(jarr.shape[0]):
                farr[cc,ww,hh] = jarr[hh,ww,cc]
    return farr


def jpg2fits(jpgfn=None):

    pic = imageio.imread(jpgfn)  # shape (npixh, npixw, 3)
    # create numpy array of numbers for R G B values
    img_array = np.asarray(pic)
    print("Image converted to", type(img_array), 
          "of", type(img_array[0,0,0]), 
          "and shape", img_array.shape)

    fig = plt.figure(figsize = (4.0,5.0))
    fig.tight_layout()

    print('\tImage type: ' , type(pic))
    print('\tImage shape: {}'.format(pic.shape))
    print('\tImage height {}'.format(pic.shape[0]))
    print('\tImage width {}'.format(pic.shape[1]))
    print('\tImage dimension {}'.format(pic.ndim))
    print('\tImage size {} pixels'.format(pic.size))
    print('\tMaximum RGB values in this image {}, R {} G {} B {}'.format(pic.max(),
           pic[:,:,0].max(), pic[:,:,1].max(), pic[:,:,2].max()))
    print('\tMinimum RGB values in this image {}, R {} G {} B {}'.format(pic.min(),
           pic[:,:,0].min(), pic[:,:,1].min(), pic[:,:,2].min()))

    print("\nTo continue, click the image window's top left corner button")
    plt.imshow(pic)
    plt.show()
    
    # Now split channels to visualize with colors:
    fig, ax = plt.subplots(nrows = 2, ncols=3, figsize=(9,8))
    fig.tight_layout()

    titles = ("R", "G", "B",
              "Red numerical value",
              "Green numerical value",
              "Blue numerical value")
    # write each channel into empty image separately and show in color
    for c in range(3):
        plt.subplot(2, 3, c+1)
        # create zero matrix of 8-bit unsigned integers
        split_img = np.zeros(pic.shape, dtype="uint8")
        # fill in only one channel... R G or B
        split_img[ :, :, c] = pic[ :, :, c]
        plt.imshow(split_img)
        plt.title(titles[c])

    # display each channel and show in greyscale
    for c, ax_ in zip(range(3), ax[1,:]):
        plt.subplot(2, 3, c+1+3)
        plt.imshow(img_array[:,:,c], cmap=plt.cm.get_cmap('gray'))
        plt.title(titles[c+3], fontsize=10)
        img_array_fits = fitsorder(img_array)
        # change the slice's orientation to suit DS9 fits viewer
        #mg_array_fits[:,:,c] = np.rot90(img_array[:,:,c], 3) # good for square images
        #img_array_fits[c,:,:] = np.rot90(img_array[:,:,c], 3)
        # (I don't know how to "rot -90"...)

    plt.savefig(jpgfn.replace('jpg','pdf'))
    # change the array's axes sequence to suit fits writing using T (transpose)
    rgb = "RGB"
    for c in range(3):
        fits.PrimaryHDU(data=img_array_fits[c,:,:]).writeto(
                                                 jpgfn.replace('.jpg',rgb[c]+'.fits'),
                                                 overwrite=True)
    print("Image array is now", type(img_array.T), 
          "of", type(img_array[0,0,0]), 
          "and shape", img_array.T.shape)
    print("\tFigure is saved in", jpgfn.replace('jpg','pdf'))

    print("\tRGB data written as three separate fits files", 
          jpgfn.replace('.jpg','[RGB].fits'))
    print("\tOpen the fits files with DS9 to view them and explore their contents.")
    print("\nTo exit, click the image window's top left corner button")
    plt.show()

if __name__ == "__main__":
    #jpg2fits(jpgfn="Roses_rgb.jpg")
    jpg2fits(jpgfn="Gigi_in_Central_Park.jpg")
