# Programming Exercise 5-3
#
# Program to compute recommended insurance to carry on an item.
# This program accepts a replacement cost from a user,
# calculates a minimum recommended insurance to carry from a global constant,
# then passes these values to a function to be displayed

# Global constant for the percent of replacement cost to insure

# Define the main function

    # Define local float variables for replacement cost and minimum insurance

    # Get the replacement cost from the user

    # Calculate the minimum insurance amount using the global constant

    # Call the function to display the insurance details, 
    # passing the replacement cost and minimum insurance to the function
      
# Define a function to display the insurance details
# This function accepts the replacement cost and minimum insurance as parameters,
# uses the global constant to calculate percent insured,
# and displays the insurance details.

	# display the replacement cost, formatting the value to 2 decimal places

    # display the percent insured, formatting the value to 2 decimal places

	# display the minimum insurance, formatting the value to 2 decimal places

# Call the main function to start the program

replacement_cost_insured = .8

def function_replacement_cost():
    replacement_cost = float(input("What is the replacement cost? "))
    minimum_insurance_amount = replacement_cost * replacement_cost_insured
    function_insurance_details(replacement_cost, minimum_insurance_amount)
    
def function_insurance_details(replacement_cost, minimum_insurance_amount):
    print("The replacement cost is", format(replacement_cost, '.2f'))
    print("The percent insured is", format(replacement_cost_insured, '.2f'))
    print("The minimum insurance is", format(minimum_insurance_amount, '.2f'))

function_replacement_cost()