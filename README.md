## astroscholars_anand
Material to support Anand's "Telescopes and Optic" lab.  Assumes astroconda is the python environment being used.  Code available at [https://github.com/anand0xff/astroscholars_anand](https://github.com/anand0xff/astroscholars_anand) (download a zip on Windows or clone from this location on UNIX)

- Examine RGB channels of jpg images, write separate FITS files for each channel. 

- On a **Unix** command line, to deconstruct a jpg image into R, G, B:

		(astroconda) bash$ cd astroscholars_anand/code/ImageExamples
		(astroconda) bash$ python jpg_rgbfits.py anyfile.jpg

	Pinhole camera predictions

		(astroconda) bash$ cd astroscholars_anand/code
		(astroconda) bash$ python photo_pinhole.py
		
- Here's what Nadia did to run python on **Windows**:

	In the Windows "App Start" menu I searched for "Anaconda" and started the Anaconda  terminal power shell. I cd-ed to the appropriate directory and ran the commands shown above.

	The only small "issue" is that the program prints a message 
	
		"Click on the upper left corner to close the image" 
	On Windows it's the **upper right corner**. 