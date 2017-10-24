# Programming Exercise 5-12
#
# Program to find the greater of two integers.
# This program accepts two integers,
# passes them to a function that compares them,
# and displays which one is greater.

# define the main function

    # Define local variables to hold two integers

    # prompt the user for the first integer
    
    # prompt the user for the second integer

    # print the return value from calling a function to find the greater of two integers
    # the two integers are passed as arguments
 
# Define a function to compare integer values.
# This function accepts two integer parameters,
# compares them,
# and returns the value of the greater.

	# if the first integer is greater, return the first integer

	# else, return the second integer

# Call the main function to start the program

def main():
    integer_one = 0
    integer_two = 0
    integer_one, integer_two = prompt_user()
    greater_value = compare_integers(integer_one, integer_two)
    print(greater_value)

def prompt_user():
    integer_one = int(input("What is the first integer? "))
    integer_two = int(input("What is the second integer? "))
    return integer_one, integer_two

def compare_integers(integer_one, integer_two):
    if integer_one > integer_two:
        print("The first integer is bigger.", integer_one, ">", integer_two)
        return integer_one
    else:
        print("The second integer is bigger.", integer_two, ">", integer_one)
        return integer_two
    
main()


