# Programming Exercise 5-15
#
# Program to find the average of five scores and output the scores and average with letter grade equivalents.
# This program prompts a user for five numerical scores,
# calculates their average, and assigns letter grades to each,
# and outputs the list and average as a table on the screen.

# define the main function

    # define local variables for average and five scores

    # Get five scores from the user

    # find the average by passing the scores to a function that returns the average

    # display grade and average information in tabular form
    # as score, numeric grade, letter grade, separated by tabs
    
    # display a line of underscores under this header
    
    # print data for all five scores, using the score,
    # with the result of a function to determine letter grade

    # display a line of underscores under this table of data

    # display the average and the letter grade for the average

# Define a function to return the average of 5 grades.
# This function accepts five values as parameters,
# computes the average,
# and returns the average.

    # define a local float variable to hold the average
    
    # calculate the average
    
    # return the average

# Define a function to return a numeric grade from a number.
# This function accepts a grade as a parameter,
# Uses logical tests to assign it a letter grade,
# and returns the letter grade.

    # if score is 90 or more, return A
    
    # 80 or more, return B
    
    # 70 or more, return C
    
    # 60 or more, return D
    
    # anything else, return F

# Call the main function to start the program


def main():
    average = 0
    score_total = 0
    score = 0
    print("Number Grade", "Letter Grade", sep = '\t')
    print("----------------------------")
    for test in range(0,5):
        score = int(input("What is the score? "))
        score_total += score
        letter_grade = calculate_letter_grade(score)
        print(score, letter_grade, sep = '\t')
    average = calculate_average(score_total)
    letter_grade = calculate_letter_grade(average)
    print(average, letter_grade, sep = '\t')
    
def calculate_average(score_total):
    average = score_total / 5
    return average
    
def calculate_letter_grade(score):
    if score >= 90:
        letter_grade = "A"
        return letter_grade
    elif score >= 80:
        letter_grade = "B"
        return letter_grade
    elif score >= 70:
        letter_grade = "C"
        return letter_grade
    elif score >= 60:
        letter_grade = "D"
        return letter_grade
    else:
        letter_grade = "F"
        return letter_grade

main()