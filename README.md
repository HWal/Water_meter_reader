Water meter reader  -  Work in progress!
========================================

An attempt to convert an image of a water meter into the numbers showing water usage.
Note: This is not a general application. It is written around my specific water meter.
By editing the code, other meters may have their readings decoded in the same way.

Hardware
--------
* A water meter, type ROSSWEINER OR MEIBES DE-09-MI001-PTB016
* An ESP32 CAM webcam

The camera is cheap, and can be found on Ebay.

Files:
------
4 python programs.  
10 number templates in .txt format.  
Color photo of the meter.  

Usage:
------
* Prepare an image file of the water meter face in RGB (multi band), with name: "meter_face_color.png". The image size should ideally be 800 x 600 pixels. If necessary, rotate the image so that the digits on the counter closely follows an imaginary x-axis.
* From "meter_face_color.png", extract an image of each of the possible digits that can appear on the volume counter. The images should be cropped to (W x H) 40 x 68 pixels, and the digit should ideally fill the image perfectly. Save the image as "n_40x68.png" where "n" is the digit.
* Run each of the "n_40x68.png" files in turn through the program "MakeTemplate.py". Edit the input filename in the program to suit the actual digit file. Experiment with the pix_color variable to achieve a text array with 1's and 0's where the 1's collectively resembles the actual digit as closely as possible. Normally the best value of the variable pix_color will be in the range 50 -> 100. Now add or subtract zeros to the text area so it will hold 40 x 68 characters with the digit in a central position. Also correct possible stray 0's or 1's where needed. Check that each line also has an End-of-line character.
* Run the program "ToGray.py". This will generate the black/white (single band) image file: "meter_face_gray.png". You may try and alter the different enhance parameters in the program to get the black/white image as good as possible.
* Edit lines 11 -> 37 of "test.py" so that the program defines an area centrally around each digit place. In the application here, the areas should be 50 pixels wide and 98 pixels high. Other meters may need other numbers. Study the example values in the code to find the correct numbers for each application and digit.

To get new counter numbers:
* Note: For taking new photos, always keep the camera in the same position.
* Provide a new photo of the meter, named: "meter_face_color.png".
* Run "meter_face_color.png" through "ToGray.py" to produce a new grayscale file "meter_face_gray.png".
* Run the program;"Test.py" to display the reading of the water meter.

A brief explanation of how the programs work:
---------------------------------------------
MakeTemplate.py  
Opens an RGB image of one digit "n_40x68.png"; digit n corresponds to the file name.
Converts the image to grayscale. Now a single band image (one band, L, grayshades).
Reads through all pixels and stores as text file where 0 is white and 1 is black.
Opening the text file (template file) in an editor will show the digit drawn by 1's.
Text file name: "n_40x68.txt".

ToGray.py  
Opens an RGB image of the meter: "meter_face_color.png".
Converts the image to grayscale. Now a single band image (one band, L, grayshades).
Adjusts Contrast, Brightness and sharpness in turn, temporarily storing image after each modification.
The finished image is stored as "meter_face_gray.png". This is the file that will be decoded.
Temporary files are deleted during the program run.

Test.py  
Opens an L (grayshade) image of the meter "meter_face_gray.png".
Sets borders for where the digit areas are on the meter face.

Function analyzer(...):
Reads the pixels in each digit area in turn, starting with the least significant.
Saves area as text file in same format as the template files (0's and 1's).
Reads back the text file and places the values in an array. Removes text file.
Reads each of the ten template files in turn, places values in array, and evaluates:
For each template array, tests for correspondence (hits) with the digit area array.
Counts number of hits, keeping the template with the highest number of hits.
The highest number of hits is weighed against the number of 1's in each template.
Weighed highest number of hits is then determined as the actual number on the meter.

The function is run for each of the digit areas on the meter face.
From this, the complete reading of the meter is done.

MaxHitsPossible.py  
Running this program creates a report of the number of 1's in each digit template.
For reference, a report is given for templates with only 1's and 0's respectively.
Output from this program is used in the program Test.py to weigh the results.