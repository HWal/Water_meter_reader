from PIL import Image, ImageOps

image_input  = "9_40x68.png"

# Open image file from Paintbrush or from cam
image0 = Image.open(image_input,"r")
# Convert color image to grayscale
image1 = ImageOps.grayscale(image0)

# Width and height for image
width, height = image0.size

# Find graycolor for each pixel (0 = black, 255 = white)
with open("9_40x68.txt", "w") as txt_file:
    for y in range(height):
        for x in range(width):
            coordinate = x, y
            pix_color = (image1.getpixel(coordinate));
            # if pix_color < 100:
            if pix_color < 87:
                val = 1
            #if pix_color >= 100:
            if pix_color >= 87:
                val = 0
            # print pix_color,
            print val,
            txt_file.write(str(val))
        txt_file.write("\n")
        print
