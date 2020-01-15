#
"""
    Written to support AstroScholars 2020
    started: Anand Sivaramakrishnan Jan 2020
"""
import os, sys
import glob
import numpy as np
import matplotlib.pyplot as plt
import jpg_rgbfits as rgb

if __name__ == "__main__":

    # Perform rebinning on out-of-camera JPGs in data directory, 
    # write smaller jpgs to the same directory...
    datadir = "../../epl5-astroschol_bin8x8/"

    for fn in glob.glob(datadir+"*.JPG"):
        print('\t', fn)
        rgb.imresize(jpgfn=fn, binby=8)

   # convert a single jpg to fits
   #rgb.jpg2fits(jpgfn=datadir+fn, jpgfig_inches = (3.0,2.0), show=False)
