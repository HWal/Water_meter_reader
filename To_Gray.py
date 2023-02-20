# OPTIMIZE PHOTO OF WATER METER

from PIL import Image, ImageEnhance, ImageOps
import os

# Open color image
image_in0 = Image.open("meter_disc_clr.png","r")

# Print band info from color image
print image_in0.getbands()

# print pixel values
coordinate = 20,15
pix_color = (image_in0.getpixel(coordinate))
print pix_color

# Convert image to grayscale from color
ImageOps.grayscale(image_in0).save('5.png')
# Now a single band (one channel) image (L)

# Remove colors from image - keep only grey
# ImageEnhance.Color(image_in0).enhance(0.0).save('1.png')
# Still RGB + (A)lpha

image_in0.close()

image_in1 = Image.open("5.png","r")

# Print band info from grayscale image
print image_in1.getbands()

# print pixel values
pix_color = (image_in1.getpixel(coordinate))
print pix_color

# Set contrast - 0.0 gives grey image - 1.0 keeps original
ImageEnhance.Contrast(image_in1).enhance(2.0).save('6.png')

image_in1.close()
os.remove("5.png")

# Set brightness - 0.0 gives black image - 1.0 keeps original
image_in2 = Image.open("6.png","r")
ImageEnhance.Brightness(image_in2).enhance(1.0).save('7.png')

image_in2.close()
os.remove("6.png")

# Set sharpness - 0.0 gives blurred image - 1.0 keeps original
image_in3 = Image.open("7.png","r")
ImageEnhance.Sharpness(image_in3).enhance(3.0).save('meter_disc_gr.png')

# Print band info from color image
print image_in3.getbands()

image_in3.close()
os.remove("7.png")
