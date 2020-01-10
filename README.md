## astroscholars_anand
Material to support Anand's "Telescopes and Optic" lab.  Assumes astroconda is the python environment being used.
Code started 2019

- Examine RGB channels of jpg images, write separate FITS files for each channel. 

- On a **Unix** command line:

		(astroconda) bash$ cd /code/ImageExamples
		(astroconda) bash$ python jpg_rgbfits.py anyfile.jpg

- Pinhole camera predictions

		(astroconda) bash$ python photo_pinhole.py
		
- Here's what Nadia did to run python on **Windows**:

	In the Windows "App Start" menu I searched for "Anaconda" and started the Anaconda  terminal power shell. I cd-ed to the appropriate directory and ran the commands shown above.

	The only small "issue" is that the program prints a message 
	
		"Click on the upper left corner to close the image" 
On Windows it's the **upper right corner**. 