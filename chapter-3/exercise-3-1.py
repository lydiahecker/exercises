# Programming Exercise 3-1
#
# Program to display the name of a week day from its number.
# This program prompts a user for the number (1 to 7)
# and uses it to choose the name of a weekday
# to display on the screen.

# Variables to hold the day of the week and the name of the day.
# Be sure to initialize the day of the week to an int and the name as a string.

# Get the number for the day of the week.
# be sure to format the input as an int

# Determine the value to assign to the day of the week.
# use a set of if ... elif ... etc. statements to test the day of the week value.

# use the final else to display an error message if the number is out of range.

# display the name of the day on the screen.

day_one = int(1)
monday = str("Monday")
day_two = int(2)
tuesday = str("Tuesday")
day_three = int(3)
wednesday = str("Wednesday")
day_four = int(4)
thursday = str("Thursday")
day_five = int(5)
friday = str("Friday")
day_six = int(6)
saturday = str("Saturday")
day_seven = int(7)
sunday = str("Sunday")

day_number = input("Pick a number from 1 to 7: ")
i_day_number = int(day_number)

if i_day_number == day_one:
    print("The day of the week is", monday,)
elif i_day_number == day_two:
    print("The day of the week is", tuesday)
elif i_day_number == day_three:
    print("The day of the week is", wednesday)
elif i_day_number == day_four:
    print("The day of the week is", thursday)
elif i_day_number == day_five:
    print("The day of the week is", friday)
elif i_day_number == day_six:
    print("The day of the week is", saturday)
elif i_day_number == day_seven:
    print("The day of the week is", sunday)
else:
    print("Error, value picked is out of range.")