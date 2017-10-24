import random

# Programming Exercise 5-11
#
# Program to quiz a user with a random addition problem.
# This program uses a random function to generate addends for an addition problem,
#   calls a function to display the problem, passing the operands as arguments,
#   calls a second function to prompt the user for an answer to the problem,
# it calculates the correct answer,
# then passes the user answer and correct answer to a third function to evaluate the results,
#   and display whether the user was correct or not.

# to generate random numbers, import random module

# define the main function

	# Define constant values for min addend and max addend

    # Define local int variables for addend 1, addend 2, user answer and correct answer
    
    # Generate random integers for addend 1 and addend 2, with values from min to max
    # constants defined above 
    
    # Call the function to display addition problem passing addend 1 and addend 2 

    # Assign the user answer to the result of calling the function to prompt for answer

    # Calculate correct answer
    
    # Call the function to evaluate answer, passing correct answer and user answer

# Define a function to display addition problem
# This function accepts two integer parameters, the addends,
# performs no calculations,
# but displays them, one above the other, aligned.

    # print the first number in a field 5 characters wide

	# print a + sign, followed by the second number in a field 4 characters wide

# Define a function to prompt a user for an answer and return it   
# This function take no parameters,
# It prompts the user for an answer and casts it to an int,
# then returns the integer value

    # Define a local variable to hold the user answer
    
    # prompt the user for an answer
    
    # return the user answer
    
# Define a function to evaluate the user's answer and display the evaluation
# This function takes correct answer and user answer as parameters
# if compares them to see if they match
# and displays a success or failure message to the user

	# if correct answer equals user answer, display success message
	
	# else display failure message

# Call the main function to start the program
def main():
    MIN = 0
    MAX = 100
    correct_answer = 0
    number_one = 0
    number_two = 0
    number_one, number_two = generate_random_ints(MIN, MAX)
    correct_answer = calculate_correct_answer(number_one, number_two)
    
    display_addition_problem(number_one, number_two)
    user_answer = prompt_for_answer()
    evaluate_answer(correct_answer, user_answer)
    
def generate_random_ints(min_value, max_value):
    number_one = random.randint(min_value, max_value)
    number_two = random.randint(min_value, max_value)
    return number_one,number_two
    
def calculate_correct_answer(number_one, number_two):
    return number_one + number_two
    
def display_addition_problem(number_one, number_two):
    line1 = format(number_one,'5')
    line2_right = "+"
    line2_left = format(number_two,'4')
    line2 = line2_right + line2_left
    print(line1)
    print(line2)
    
def prompt_for_answer():
    user_answer = int(input("What is the answer? "))
    return user_answer
    
def evaluate_answer(correct_answer, user_answer):
    if user_answer == correct_answer:
        print("Good job, you got it right.")
    else:
        print("Incorrect.")

main()