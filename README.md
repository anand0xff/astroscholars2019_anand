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
		
- To run python on **Windows**:

	In the Windows "App Start" menu I searched for "Anaconda" and started the Anaconda  terminal power shell. I cd-ed to the appropriate directory and ran the commands shown above.


#### Monday's class

- Understandable quantification of a radian
- Combination of math of resolution limit and practical hands on demo with pinholes
- Raytracing to understand image formation
- [Thin lens equation](https://en.wikipedia.org/wiki/Thin_lens) in "Image Formation" related object distance, image distance, and lens focal length 
- Larger pinholes produce larger [circle of confusion](https://en.wikipedia.org/wiki/Circle_of_confusion) blur
- Smaller pinholes crate larger diffraction blur: the Point-Spread function is an [Airy pattern](https://en.wikipedia.org/wiki/Airy_disk).

Monday's data:

		I put 8x8 binned images up on the github site with a filelist.txt 
		containing image creation dates/times, and some explanation if
		you want to use these.  epl5-astroschol_bin8x8.zip


#### Tuesday's class

Resolution, pixel or plate scale on detector, f-ratio = Diameter/focal_length  
Motivation for new instrumentation by Scott Acton: Adaptive Optics (AO)  
Palomar 200" Hale telescope AO off and AO on movie of real data (Soummer & Lloyd)  
Keck AO 3D plot of without/with AO  
Shack-Hartmann wavefront sensing  

Discussion of resolution: radio meter wavelengths, optical micron wavelength, X-ray nanometer wavelengths.  

##### Wave description: complex amplitude


   Describing light numerically/mathematically: a plane wave of monochromatic
   light (in a homogenous or non-dispersive medium or vacuum, with spatial
   coordinates (x,y,z) is a propagating oscillation of the electric and magnetic
   fields.  
   
   One of the fields - let's say the electric field,  can be expressed by the
   real part of a complex number that has a (real) ** amplitude **  A and a
   unit-strength ** phasor ** exp(i(kz - wt + phi(x,y))).  Here we use w
   instead of the usual Greek omega. phi(x,y) is the (real) ** phase **
   (out-of-plane corrugation) of the ** wavefront **.  A wavefront is a
   surface of constant phase.  The wave moves in the z direction at
   speed w/k (why is that so? What is actually moving?).


   We often drop the "purely propagating" multiplicative factor, exp(i(kx - wt)),
   of the phasor, and just work on the in-plane phase disturbances exp(i
   phi(x,y)).  This will be justified later.  With this shorthand the wave's 
   ** complex amplitude ** is written  A exp(i phi(x,y)).
    
   What mathematical/numerical operation must you perform on a complex array
   describing the wave's complex amplitude to get a real array proportional to
   the intensity (brightness) that a CCD or IR array might detect?  Recall that
   the electric (or magnetic) field of an EM wave oscillates between +A and -A,
   but intensity is a positive (or zero) quantity.  Think in complex number
   space here.
			


Interference - usually a photon only interferes with itself.  What if two lasers shine through a pihole at the same time?  Generate experimental data to test after writing down hypotheses.

Tuesday's data:

	Updated filelist, data in epl5-astroschol_bin8x8_Tue2lasers.zip
	
Select a good image, split it into separate fits files, look at the three channels in the fits file, and conclude which hypothesis (or hypotheses) are correct.

	You might have to comment out a few lines in rgb_script.py and uncomment
	the call to splitting a jpg file into fits and showing the jpg &
	numerical values.
	
	Two sets of fits files & pdfs from Tuesday's data: RGlasers_exps38_59.zip 

##### Possible start-to-finish instrumentation exercise

- Select an astronomical phenomenon or object you want to observe with enough resolution to separate out the details that interest you.  
- Assign a typical distance (in meters) to your object of interest ([distance translation here](http://www.kylesconverter.com/length/parsecs-to-light-years))
- What physical separation (in meters) do you need to resolve with the telescope you will have to design for this science? E.g. do you want see the two different nuclei of a merging galaxy?
- At the object's distance, what angle does that physical scale subtend at your telescope on or near the Earth?
- What EM radiation band are you interested in observing this object (Gamma ray, X-ray, UV, optical, infrared, microwave, millimeter, radio (meter)...)?
- With these science requirements, calculate the telescope's primary mirror diameter.
- Hazard a wild guess at how much that would cost and how long it might take to build.


#### Wednesday's class

#### Pupil (or aperture) planes, image planes (using camera)
- partially obscuring the camera lens (i.e. pupil) dims the image but doesn't change it substantially.  So we know each point in the image gets light from every part of the pupil
- partially covering the image just blocks off part of the image
- The lens creates an image whether or not there is a screen to make it visible!  If there is no screen or detector at the image plane, an aerial image is formed, and light simply goes on past that plane
-Use an **eyepiece** (another convex lens) to ispect that aerial image closely.  The [angular magnification](http://hyperphysics.phy-astr.gsu.edu/hbase/geoopt/teles.html) of this telescope is the ratio of objective (front lens) focal length to eyepiece focal length.



	In class - develop a presentation plan & initial list of what to cover.  Divide and conquer, but teach each other too.



	
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