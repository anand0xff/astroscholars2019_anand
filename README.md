## astroscholars2019_anand
Material to support Anand's "Telescopes and Optic" lab.  Assumes astroconda is the python environment being used.
Code started 2019

- Examine RGB channels of jpg images, write separate FITS files for each channel

		(astroconda) bash$ cd /code/ImageExamples
		(astroconda) bash$ python jpg_rgbfits.py anyfile.jpg

- Pinhole camera predictions

		(astroconda) bash$ python photo_pinhole.py