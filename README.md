## astroscholars_anand
Material to support Anand's "Telescopes and Optic" lab.  Assumes astroconda is the python environment being used.  Code available at 

[https://github.com/anand0xff/astroscholars_anand](https://github.com/anand0xff/astroscholars_anand) 

(download a zip on Windows or clone from this location on UNIX)

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

#### Monday's class: salient points?
	What did each of you particularly like or recall from
	Monday's project work?

##### Monday's material for presentation:

	I put 8x8 binned images up on the github site with a filelist.txt 
	containing image creation dates/times, and some explanation if
	you want to use these.
	
	
#### Useful links
	

[Understanding focal length](http://hyperphysics.phy-astr.gsu.edu/hbase/geoopt/foclen.html)  
[Image formation: ray tracing through a lens](https://www.physicsclassroom.com/class/refrn/Lesson-5/Converging-Lenses-Ray-Diagrams)  
[Pinhole diffraction in ocean waves](https://www.flickr.com/photos/exploratorium/3789624153/)  
[Interference, diffraction, superposition, Huygen's Principle](https://www.thoughtco.com/interference-diffraction-principle-of-superposition-2699048)  
[Pixel scale and resolution element size](https://github.com/anand0xff/astroscholars_anand/blob/master/PLSCL.pdf)   
[Simple and multi-element lens focal length](https://photo.stackexchange.com/questions/21668/what-is-the-reference-point-that-the-focal-length-of-a-lens-is-calculated-from) 
[Waves](https://blog.soton.ac.uk/soundwaves/further-concepts/1-mechanical-waves-and-light-waves/)  
[Rays and wavefronts](https://phys.libretexts.org/Courses/University_of_California_Davis/UCD%3A_Physics_7C_-_General_Physics/09%3A_Optics/9.1%3A_Rays_and_Wavefronts)  
[Adaptive optics: why?](https://www.youtube.com/watch?v=F6hmLcJOkzM)  
[Adaptive Optics off and on](https://github.com/anand0xff/astroscholars_anand/blob/master/optics/0_AO-On-Off%20(Converted).mov)  
[AO Keck data](http://www.ctio.noao.edu/~atokovin/tutorial/intro.html)  
[Shack Hartmann wavefront sensor](http://www.ctio.noao.edu/~atokovin/tutorial/part3/wfs.html)