# CONVERT WATER METER DIAL TO DIGITS

def main():
    from PIL import Image, ImageOps

    # Use a grayscale single band version of the meter disc image
    meter_disc_gr  = "meter_face_gr.png"
    meter = Image.open(meter_disc_gr,"r")

    # General
    upper = 296
    lower = 406
    width = 40

    # Digit fields: exp0 = litres, exp7 = 10000000 litres
    exp0_left = 692
    exp0_right = exp0_left + width
    exp1_left = 627
    exp1_right = exp1_left + width
    exp2_left = 562
    exp2_right = exp2_left + width
    exp3_left = 495
    exp3_right = exp3_left + width
    exp4_left = 426
    exp4_right = exp4_left + width
    exp5_left = 357
    exp5_right = exp5_left + width
    exp6_left = 288
    exp6_right = exp6_left + width
    exp7_left = 221
    exp7_right = exp7_left + width

    # Analyze digit areas against digit templates
    def analyzer(left, right, upper, lower, exp_ind):

        # File for saving each digit area on the meter face
        out_exp = "exp" + str(exp_ind) + ".txt"

        # Get grayscale value for each pixel (0=black, 255=white)
        # Write pixel values 0 or 1 to text file exp_.txt
        with open(out_exp, "w") as txt_file:
            for y in range(upper, lower, 1):
                for x in range(left, right, 1):
                    coordinate = x, y
                    pix_color = (meter.getpixel(coordinate))
                    if pix_color < 57:
                        val = 1
                    if pix_color >= 57:
                        val = 0
                    txt_file.write(str(val))
                txt_file.write("\n")
        txt_file.close()

        # Read back file exp_.txt into array
        in_exp = "exp" + str(exp_ind) + ".txt"
        exp_reader = open(in_exp, "r")

        # Initialize exp array with zeros
        exp_arr = [[0] * (right - left) for z in range(lower - upper)]

        # Read characters in each line including EOL character
        for y in range(lower - upper):
            line = exp_reader.read(right - left + 1)
            for x in range(right - left):
                exp_arr[y][x] = int(line[x])
        exp_reader.close()

        # All digit templates
        template_files = ["0_40x60.txt", "1_40x60.txt", "2_40x60.txt",
                          "3_40x60.txt", "4_40x60.txt", "5_40x60.txt",
                          "6_40x60.txt", "7_40x60.txt", "8_40x60.txt",
                          "9_40x60.txt"]

        # Max hits per digit
        Match_max = 0
        Digit = 0

        for p in range(10):
            # Create array from template file - template has fixed size
            template = template_files[p]
            template_columns = 40
            template_rows = 60
            template_reader = open(template,"r")

            # Initialize and fill the template array with zeros
            template_arr = [[0] * template_columns for z in range(template_rows)]

            # y = rows (outer index), x = columns (inner index)
            for y in range(template_rows):
                # The line variable includes EOL character
                line = template_reader.read(template_columns + 1)
                for x in range(template_columns):
                    template_arr[y][x] = int(line[x])
            template_reader.close()
            
            match_max = 0
            digit = 0

            # Look for matches
            for z in range(50):
                match = 0
                for m in range(60):
                    for n in range(40):
                        if template_arr[m][n] == 1 and exp_arr[m+z][n] == 1:
                            match = match + 1
                if match > match_max:
                    match_max = match
                    digit = p

            # Keep the found digit
            if match_max > Match_max:
                Match_max = match_max
                Digit = p

        print "Hits:", Match_max, ",", "Found digit:", Digit, ", Position: 10 ^", exp_ind
        return Digit * (10 ** exp_ind)
    # ---------------------------- End of analyzer function -----------------------------

    # Call analyzer function
    exp_ind = 0
    first = analyzer(exp0_left, exp0_right, upper, lower, exp_ind)
    exp_ind += 1
    second = analyzer(exp1_left, exp1_right, upper, lower, exp_ind)
    exp_ind += 1
    third = analyzer(exp2_left, exp2_right, upper, lower, exp_ind)
    exp_ind += 1
    fourth = analyzer(exp3_left, exp3_right, upper, lower, exp_ind)
    exp_ind += 1
    fifth = analyzer(exp4_left, exp4_right, upper, lower, exp_ind)
    exp_ind += 1
    sixth = analyzer(exp5_left, exp5_right, upper, lower, exp_ind)
    exp_ind += 1
    seventh = analyzer(exp6_left, exp6_right, upper, lower, exp_ind)
    exp_ind += 1
    eighth = analyzer(exp7_left, exp7_right, upper, lower, exp_ind)

    # print first, second, third, fourth, fifth, sixth, seventh, eighth
    print "\nMeter total value:",
    print first + second + third + fourth + fifth + sixth + seventh + eighth,
    print "litres"

if __name__ == '__main__':
    main()
