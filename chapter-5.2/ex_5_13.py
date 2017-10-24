from tables import print_two_column_header
# Programming Exercise 5-13
#
# Program to display a table of times and falling distances for a specific range in seconds.
# This program accepts no input,
# but uses a loop to pass a range of times in seconds to a function
# 	that returns the falling distance for that amount of time,
# and displays the results as a table.

# define the main function

    # define a local float variable to hold distance

    # Set up results chart, printing time and falling distance separated by a tab
    # include a separator line made with a row of underscores
    
    # loop through a range of time values (in seconds)

        # pass the time to a falling distance function and assign result to distance

		# print the time and distance formatted to two places, separated by a tab

# Define a function to calculate the falling distance for a time in seconds
# The function accepts a time in seconds as a parameter,
# computes the distance,
# and returns the distance it has fallen in that time

	# define a local float variable to hold falling distance
	
	# compute the falling distance using a formula and the time
	
	# return the falling distance

# Call the main function to start the program

def main():
    distance = 0.0
    print_two_column_header("Time","Distance")
    for seconds in range(0, 10):
        distance = falling_distance(seconds)
        print(seconds,"\t",distance)

def falling_distance(seconds):
    distance = seconds * seconds * 9.8 * .5 
    return distance

print(__name__)
main()