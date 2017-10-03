# Programming Exercise 3-4
#
# Program to convert a number from 1 to 10 to a Roman numeral.
# This program will accept an integer from 1 to 10 from the user
# and use it to choose an appropriate Roman numeral
# to display on the screen.

# Variables to hold a number and a numeral.
# initialize the number as an int and the numeral as a string.

# Get number from user and convert it to an int

# Set numeral to a Roman numeral value based on the value of number
# use a set of if ... elif .... etc. statements.

# use a final else to display an error if number is out of range.

# display the numeral on the screen.

number = input("Pick a number from 1 to 10: ")
i_number = int(number)

one = str("i")
two = str("ii")
three = str("iii")
four = str("iv")
five = str("v")
six = str("vi")
seven = str("vii")
eight = str("viii")
nine = str("ix")
ten = str("x")

if i_number == 1:
    print(one)
elif i_number == 2:
    print(two)
elif i_number == 3:
    print(three)
elif i_number == 4:
    print(four)
elif i_number == 5:
    print(five)
elif i_number == 6:
    print(six)
elif i_number == 7:
    print(seven)
elif i_number == 8:
    print(eight)
elif i_number == 9:
    print(nine)
elif i_number == 10:
    print(ten)
else:
    print("Error, value is out of range.")