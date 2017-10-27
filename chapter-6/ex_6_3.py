# Programming Exercise 6-3
#
# Program to open a file and display its contents with line numbers.
# This program prompts the user for a file name,
# reads the file until it ends
# then displays each line with its line number before closing the file.

# define the main function

    # Define local variables for line and filename (strings) and counter (int)

    # Prompt the user for a file name

    # Open the specified file for reading

    # use a for loop to loop through all the lines

        # increment the counter

        # print the current line number without carriage return
       
        # Strip the '\n' from the end of the line

        # display the line (should be on same line as line number)

    # Close file

# Call the main function to start the program

def main():
    line = ''
    file_name = ''
    counter = 0
    file_name = input("Which file? ")
    file = open(file_name, 'r')
    for line in file:
        counter += 1
        line = line.strip('\n')
        print(line, counter)
    file.close()

main()