# CONVERT WATER METER DIAL TO DIGITS

def main():
    from PIL import Image, ImageOps
    import os

    # Use a grayscale single band version of the meter disc image
    meter_disc_gr  = "meter_face_gray.png"
    meter = Image.open(meter_disc_gr,"r")

    # Common values for defining the digit areas
    upper = 269 # Upper horizontal line
    lower = 371 # Bottom horizontal line
    width = 50  # Wider than the digit templates

    # Digit templates with fixed size
    template_columns = 40
    template_rows = 68

    # Digit fields naming: exp0 = litres, ..., exp7 = 10000000 litres
    # Define left and right borders of the number areas to be analyzed
    exp0_left = 623
    exp0_right = exp0_left + width
    exp1_left = 543
    exp1_right = exp1_left + width
    exp2_left = 464
    exp2_right = exp2_left + width
    exp3_left = 387
    exp3_right = exp3_left + width
    exp4_left = 307
    exp4_right = exp4_left + width
    exp5_left = 229
    exp5_right = exp5_left + width
    exp6_left = 150
    exp6_right = exp6_left + width
    exp7_left = 73
    exp7_right = exp7_left + width


    # Function for analyzing digit areas against digit templates
    def analyzer(left, right, upper, lower, exp_ind):

        # File for temporary saving each digit area
        out_exp = "exp" + str(exp_ind) + ".txt"

        # Get grayscale value for each pixel in digit area (0=black, 255=white)
        # Then write pixel values represented by 0 or 1 to text file exp_.txt
        # The files can be used for fine tuning of the results
        with open(out_exp, "w") as txt_file:
            for y in range(upper, lower, 1):
                for x in range(left, right, 1):
                    coordinate = x, y
                    pix_color = (meter.getpixel(coordinate))
                    if pix_color < 120:
                        val = 1
                    if pix_color >= 120:
                        val = 0
                    txt_file.write(str(val))
                txt_file.write("\n")
        txt_file.close()

        # Open the recently saved .txt file
        in_exp = "exp" + str(exp_ind) + ".txt"
        exp_reader = open(in_exp, "r")

        # Initialize exp array with zeros
        exp_arr = [[0] * (right - left) for z in range(lower - upper)]

        # Read characters in each line including EOL character
        # Put characters into array - excluding EOL character
        for y in range(lower - upper):
            line = exp_reader.read(right - left + 1)
            for x in range(right - left):
                exp_arr[y][x] = int(line[x])
        exp_reader.close()

        # Remove file exp_.txt
        os.remove("exp" + str(exp_ind) + ".txt")

        # List of all digit templates
        template_files = ["0_40x68.txt", "1_40x68.txt", "2_40x68.txt",
                          "3_40x68.txt", "4_40x68.txt", "5_40x68.txt",
                          "6_40x68.txt", "7_40x68.txt", "8_40x68.txt",
                          "9_40x68.txt"]

        Ones_in_each_template = [1188, 876, 943,
                                 925, 1023, 1041,
                                 1080, 828, 1195,
                                 1088]

        # Container variables for Max hits and Found digit
        Match_max = 0
        Digit = 0

        # Test each number area agains all digit templates
        for p in range(10):
            # Create array from template file - template has fixed size
            template = template_files[p]
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
            for k in range(width - template_columns): # Along a row
                for z in range(lower - upper - template_rows): # Along a column
                    match = 0
                    for m in range(template_rows):
                        for n in range(template_columns):
                            if template_arr[m][n] == 1 and exp_arr[m + z][n + k] == 1:
                                match = match + 1
                    if match > match_max:
                        match_max = match
                        digit = p

            # For debug
            # print match_max,

            # Keep the found digit - Accept only 0.4 * number of 1s in the template
            if (match_max > Match_max) and (match_max > int(Ones_in_each_template[p] * 0.4)):
                Match_max = match_max
                Digit = p

            # On the meter in use here it is not easy to decode the rightmost digit properly,
            # so we set it to zero.
            if exp_ind == 0:
                Digit = 0

        print "Hits:", "%4d"%Match_max, "(", "%4d"%Ones_in_each_template[Digit], ")",
        print ",", "Found digit:", Digit, ", Position: 10 ^", exp_ind
        return Digit * (10 ** exp_ind)
    # ------------------------------- End of analyzer function --------------------------------

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

    print "\nMeter total value:",
    print eighth + seventh + sixth + fifth + fourth + third + second + first,
    print "litres"

if __name__ == '__main__':
    main()
