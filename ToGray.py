# MAKE GRAYSCALE PHOTO OF WATER METER FACE

from PIL import Image, ImageEnhance, ImageOps
import os

# Open color image
image_in0 = Image.open("meter_face_color_12.png","r")

# Print band info from color image
print image_in0.getbands()

# Convert image to grayscale from color and save to file
ImageOps.grayscale(image_in0).save('5.png')
# Now a single band (one channel) image (L)

image_in0.close()

image_in1 = Image.open("5.png","r")

# Set contrast - 0.0 gives grey image - 1.0 keeps original
ImageEnhance.Contrast(image_in1).enhance(2.0).save('6.png')

# Delete temporary file
image_in1.close()
os.remove("5.png")

# Set brightness - 0.0 gives black image - 1.0 keeps original
image_in2 = Image.open("6.png","r")
ImageEnhance.Brightness(image_in2).enhance(1.0).save('7.png')

# Delete temporary file
image_in2.close()
os.remove("6.png")

# Set sharpness - 0.0 gives blurred image - 1.0 keeps original
image_in3 = Image.open("7.png","r")
ImageEnhance.Sharpness(image_in3).enhance(3.0).save('meter_face_gray_12.png')

# Print band info from color image
print image_in3.getbands()

# Delete temporary file
image_in3.close()
os.remove("7.png")
