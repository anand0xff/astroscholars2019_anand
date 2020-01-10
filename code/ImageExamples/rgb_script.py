#
"""
    Written to support AstroScholars 2020
    started: Anand Sivaramakrishnan Jan 2020
"""
import os, sys
import numpy as np
import matplotlib.pyplot as plt
import jpg_rgbfits as rgb


if __name__ == "__main__":

    datadir = "./data_10um_pinhole/"
    fns = (
        "P1100006_10um_105mm_1_bin8x8.jpg",
        "P1100007_10um_105mm_2_bin8x8.jpg",
        "P1100008_10um_105mm_3_bin8x8.jpg",
        "P1100009_10um_105mm_4_bin8x8.jpg",
        "P1100010_10um_105mm_5_bin8x8.jpg")
    for fn in fns:
        rgb.jpg2fits(jpgfn=datadir+fn, jpgfig_inches = (3.0,2.0), show=False)
