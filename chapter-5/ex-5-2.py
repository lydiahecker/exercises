# Programming Exercise 5-2
#
# Program to calculate final purchase details.
# This program takes a purchase amount from a user,
# then calculates state tax, county tax and total tax,
# 	and passes them to a function to be totaled
# and displayed

# Global constants for the state and county tax rates

# define the main function

    # Define local float variables for purchase, state tax and county tax

    # Get the purchase amount from the user
    
    # Calculate the state tax using the global constant for state tax rate

    # Calculate the county tax using the global constant for county tax rate

    # Call the sale details function, passing the purchase, state tax and county tax

# define a function to display purchase details
# this function accepts purchase, stateTax, and countyTax as arguments,
# calculates the total tax and sale total,
# then displays the purchase details

    # Define local float variables for total tax and sale total

	# Calculate the total tax

	# Calculate the total sale

    # Display the purchase details, including purchase, state tax, county tax,
    #	total tax, and sale total, each on a line.  Format floats to 2 decimal places.

# Call the main function to start the program.

state_tax = .07
county_tax = .06
def function_purchase_amount():
    purchase_amount = float(input("What was the purchase amount? "))
    county_tax_amount = purchase_amount * county_tax
    state_tax_amount = purchase_amount * state_tax
    function_sale_details(purchase_amount, county_tax_amount, state_tax_amount)

def function_sale_details(purchase_amount, county_tax_amount, state_tax_amount):
    total_tax = state_tax_amount + county_tax_amount
    sale_total = total_tax + purchase_amount
    print("The subtotal is", format(purchase_amount, '.2f'))
    print("The county tax amount is", format(county_tax_amount, '.2f'))
    print("The state tax amount is", format(state_tax_amount, '.2f'))
    print("The total tax is", format(total_tax, '.2f'))
    print("The total sale is", format(sale_total, '.2f'))

function_purchase_amount()