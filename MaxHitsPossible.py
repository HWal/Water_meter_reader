# COUNT NUMBER OF 1s IN EACH TEMPLATE FILE

def main():

    # Digit templates with fixed size
    template_columns = 40
    template_rows = 68

    # List of all digit templates
    template_files = ["zeros.txt  ", "0_40x68.txt", "1_40x68.txt", "2_40x68.txt",
                      "3_40x68.txt", "4_40x68.txt", "5_40x68.txt",
                      "6_40x68.txt", "7_40x68.txt", "8_40x68.txt",
                      "9_40x68.txt", "ones.txt   "]

    # Count and report the number of digit ones in each template
    for p in range(12):
        Ones = 0
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
                if template_arr[y][x] == 1:
                    Ones += 1
        template_reader.close()
        
        print "Ones in template ", template_files[p], ":", "%4d"%Ones


if __name__ == '__main__':
    main()
