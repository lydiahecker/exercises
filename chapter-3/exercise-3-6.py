# Programming Exercise 3-6
#
# Program to check if a date is 'magic' (day * month = year).
# This program takes a month, day and year from the user as integers,
# Checks to see if each is in range, then checks whether month * day = year,
# then displays an appropriate message depending on the result

# Variables for month, day, year and message
# initialize month, day and year as integers, message as a string


# Get month and cast it to int


# Get day and cast it to int


# Get year and cast it to int


# This problem can be solved with if-else logic by the reducing the problem domain
# if month input is out of range

	# set message to hold "invalid month" message


# else if day input is out of range

    # set message to hold "invalid day" message

# else if  year input is out of range (greater than 99 or less than 0)

    # set message to hold "invalid year" message

# else 

    # set message to hold the date in 00/00/00 form
    
    # if day * month equals year, add " is a magic date" to message
    
    # else add " is not a magic date" to message


# print message for the user

day = input("What day is it? ")
i_day = int(day)
month = input("What month is it? ")
i_month = int(month)
year = input("What year is it? ")
i_year = int(year)
equation = i_day * i_month

if i_month > 12 or i_month < 1:
    print("Invalid month.")
elif i_day > 31 or i_day < 1:
    print("Invalid day.")
elif i_year > 99 or i_year < 0:
    print("Invalid year.")
else:
    print("The date is", i_month,"/",i_day,"/",i_year)
    if equation == i_year:
        print("The date is magic.")
    else:
        print("The date is not magic.")