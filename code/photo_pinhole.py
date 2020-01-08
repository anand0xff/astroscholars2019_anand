#! /usr/bin/env python
"""
    Code to calculate and display pinhole camera characteristics
    Written to support AstroScholars 2020
    started: Anand Sivaramakrishnan Dec 2019
"""
import os, sys
import numpy as np

# All units SI unless otherwise stated.

def airyscale(dia, wave):
    return wave/dia

mm = 1.0e-3
um = 1.0e-6
inch = 25.4 * mm
deg = np.pi / 180.0

F = 100.00 * mm    # Image distance
D = (10*um, 100*um, 500*um, inch/16, inch/4)  # Pinhole diameters

"""
Select one of these three sets by commenting in or  out...
#1:
band = "r" # red laser
lams = (0.6328*um,)
#2:
band = "g" # green laser
lams = (0.532*um,)
"""
#3:
band = "RGB"
lams = (0.43*um, 0.54*um, 0.575*um)  # wavelengths

pixel = 3.75434 * um

print("\nDistance to detector {:.0f} mm, pixel size = {:.2f} um".format(F/mm, pixel/um))
resols = []

"""
 d =   10 um, res = 5.75e-02 rad (3.29 deg)  f/10000  f*lambda 5750.0 um = 1531.6 pixels
  Hole dia.       Angular resolution         Aperture       Resolution on detector
"""
coltitle = "  Hole dia.       Angular resolution            Aperture       Resolution on detector"
for bnd,lam in zip(band,lams):
    print("\nWavelength {:s} = {:.2f} um".format(bnd, lam/um))
    print(coltitle)
    for d in D:
        print(" d = {:<4.0f} um ".format(d/um), end="")
        resols.append(airyscale(d, lam))
        print("  res = {:.2e} rad ({:.2f} deg)".format(resols[-1], 
                                                      resols[-1]/deg), 
                                                      end="")
        print("    f/{:<5.0f}  f*lambda {:6.1f} um ".format(F/d, F/d*lam/um), end="")
        print("= {:<6.1f} pixels".format(F*resols[-1]/pixel))
print()
