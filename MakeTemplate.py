from PIL import Image, ImageOps

image_input  = "7.png"

# Open image file from Paintbrush or from cam
image0 = Image.open(image_input,"r")
# Convert color image to grayscale
image1 = ImageOps.grayscale(image0)

# Width and height for image
width, height = image1.size

# Find graycolor for each pixel (0 = black, 255 = white)
with open("7.txt", "w") as txt_file:
    for y in range(height):
        for x in range(width):
            coordinate = x, y
            pix_color = (image1.getpixel(coordinate));
            # if pix_color < 85:
            if pix_color < 57:
                val = 1
            #if pix_color >= 85:
            if pix_color >= 57:
                val = 0
            # print pix_color,
            print val,
            txt_file.write(str(val))
        txt_file.write("\n")
        print
