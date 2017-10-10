# Programming Exercise 4-1
#
# Program to total the values of five integers.
# This program the user for an integer five times,
# and totals them up,
# then displays the total entered on the screen.

# Initialize variables for bugs collected and total bugs.
# be sure to initialize them as integers


# Get the number of bugs collected from the user
# use a for loop to get the number of bugs exactly five times, once for each day


	# input bugs collected on this day and convert it to an int

    
    # add bugs collected to total bugs


# Display the total number of bugs collected for all five days.

total = 0

for num in [1,2,3,4,5]:
    num_bugs = input("How many bugs were collected? ")
    i_num_bugs = int(num_bugs)
    total += i_num_bugs

print(total, "bugs were collected in five days.")