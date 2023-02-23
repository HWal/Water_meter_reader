Water meter reader - This is work in progress!
==============================================

These programs, written in python, is an attempt to convert an image of a water meter into the numbers showing water usage.

Hardware
--------
* A water meter
* An ESP32 cam webcam

The camera is cheap, and can be found on Ebay.

Note: Testing at this stage is done with a mobile phone camera.


Files
-----
Three python programs.
10 number templates in .txt format.

Usage:
------
* Prepare an image file of the water meter face in RGB (multi band), with name: "meter_face_clr.png". The image size should ideally be 1000 x 1000 pixels. If necessary, rotate the image so that the digits on the volume counter closely follows an imaginary x-axis.
* Run the program "ToGray.py". This will generate the black/white (single band) image file: "meter_face_gr.png". You may try and alter the different enhance parameters in the program to get the black/white image as good as possible.
* From the color image, extract an image of each of the possible digits that can appear on the volume counter. Select a rectangle as close as possible to the digit, and save the images as "_.png" where n is the digit. If done correctly, the images should be close to, but less than (W x H) 40 x 60 pixels.
* Run each of the "_.png" files through the program "MakeTemplate.py". Edit the input filename in the program to "_.png" and output filename to "_.txt" to suit the actual digit file. Experiment with the pix_color variable to achieve a text array with 1's and 0's where the 1's collectively resembles the actual digit as good as possible. Normally the best value of the variable pix_color will be in the range 57 -> 85. Now add zeros to the text area so it will hold 40 x 60 characters with the digit in a central position. Note (and check) that each line also has an End-of-line character.
* Rename each digit text file to "__40x60.txt".

To get the numbers:
* Run "meter_face_clr.png" through "ToGray.py" to produce a new grayscale file "meter_face_gr.png".
* Run "meter_face_gr.png" through "test_v12.py" to display the reading of the water meter.