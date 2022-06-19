# ASCII-ART-GENERATOR
ASCII art is the technique of representing picture in form of ASCII Character consisting of 128 characters.

Example of an ASCII ART is shown below:
![alt text](https://i.imgur.com/fJsEVJi.png)
In the above example an image is converted to ASCII Art.

Extending this idea of converting image to ASCII Art in this project we will be converting a video (.mp4 file ) to ASCII Video.

# HOW TO RUN PROJECT

1. Python 3 should be installed in your system. (Go to terminal and type "python --version" to check python version).
2. OpenCV must be installed.(Install using "pip install opencv-python" )
3. Python Pillow be installed. (Install using "pip install Pillow")

# CODE...

Our code have two functions "asciify_img()" and "asc_vid()" for converting image and video to ascii art respectively.<br>
"main()" function will first call "asc_vid()" function for converting given video to ASCII ART.<br>
"asciify_img()" will convert current frame of video to ASCII art <br>
Converting an image to ASCII format include mapping each pixel to corresponding character from charArray (line 9 of code)<br>
than resizing image using "scale_factor" (line 20 of code)
from line 25 to line 31 of we iterate over pixels of image to corresponding characters .
"asc_vid()" will call "asciify_image()" to convert every frame of video to ASCII ART and will return the ASCIIFIED frame<br>
code will than append the resulting frame to video<br>
The process will run for every frame.<br>
We will finally get ASCIIFIED video as a result.<br>

# LEARNINGS FROM PROJECT
Basics of Images ,how images are stored, image manipulation like resizing and resampling , using OpenCV and Pillow for Image manipulation, working with videos using OpenCV.

