# seam_carver
Content aware Image resizing using Seam Carving algorithm. Original Paper by Engineers at MERL.

TODOs:

1. Image Processing
	1. Using an Energy function to transform given image.
	
2. Algorithms
	1. Implement DP algorithm to identify minimum energy (vertical) seam.
	2. Update 2-D matrix image by removing seam (1-pixel width)
	3. Repeat 1,2 until desired width of image is attained.