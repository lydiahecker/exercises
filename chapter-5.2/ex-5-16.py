import random
# Programming Exercise 5-16
#
# Program to compare the proportion of odd and even random integers.
# This program accepts no input.
# It uses a loop and the random library to generate 100 random integers,
# counts the number of odd and even results,
# and displays the total of each.

# To use the random integer function, import the random library

# define the main function

    # define local int variable for number, odd and even totals

    # define a constant to hold how many numbers to compare (100)

    # loop through the range of numbers to compare

        # get a random integer from the random library function

        # if the check for even function returns true, increment even counter

        # else increment odd counter.

    # display the results on the screen

# Define a function to check for even numbers
# This function accepts one integer parameter,
# uses the mod operater to see if can be evenly divided by two,
# and return true if it can, false it cannot

    # if dividing the number by two yields no remainder, return true

    # else return false

# Call the main function to begin the program
def main():
    MIN = 0
    MAX = 100
    number = 0
    number_odd = 0
    number_even = 0
    number_compare = 100
    for num in range(0, number_compare):
        number = random.randint(MIN, MAX)
        number_even, number_odd = even_check(number, number_even, number_odd)
    print("There were", number_even, "even numbers.")
    print("There were", number_odd, "odd numbers.")


def even_check(number, number_even, number_odd):
    if number % 2 == 0:
        number_even += 1
        number_odd = number_odd
        return number_even, number_odd
    else:
        number_odd += 1
        number_even = number_even
        return number_odd, number_even

main()