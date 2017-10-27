# Programming Exercise 6-5
#
# Program to total the value of numbers in a text file.
# The program takes no user input, but requires a text file with numbers, one per line,
# which it opens, reads line by line, and totals the numbers in a variable,
# then displays the total on the screen.

# Define the main function.

    # Declare a local string variable for line and two floats for total and current number

    # Open numbers.txt file for reading

    # iterate over the lines in the file

        # get a number from the current line

        # add it to total
        
    # Close file

    # Display the total of the numbers in the file

# Call the main function to start the program.

def main():
    line = ''
    total = 0.0
    current_number = 0.0
    file = open("numbers.txt", 'r')
    line = file.readline()
    while line != '':
        line = line.strip('\n')
        current_number = float(line)
        total += current_number
        line = file.readline()
    file.close()
    print("The total is", total)

main()