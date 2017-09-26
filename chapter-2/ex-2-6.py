# Programming Exercise 2-6
#
# Program to calculate a total sale price using state and local sales tax.
# This program prompts a user for an amount of purchase,
# uses constants to calculate state, county and total sales tax, and a purchase total
# then displays the details of these calculations for the user.

# Variables for purchase amount, state tax, county tax, total tax and total sale
# all initialized as floats


# Constants for the state and county tax rates


# Get the amount of purchase from the user, casting it to a float.


# Calculate the state sales tax.


# Calculate the county sales tax.


# Sum the total tax.


# Calculate the total of the sale.


# Print detailed information about the sale, formatting all values to two decimal places.

state_tax = .07
county_tax = .06

amount = input("What is the amount of your purchase? ")
f_amount = float(amount)

state_sales_tax = f_amount * state_tax
county_sales_tax = f_amount *county_tax
sales_tax = state_sales_tax + county_sales_tax

total = sales_tax + f_amount

print ("The state sales tax is", format(state_sales_tax, '.2f'))
print ("The county sales tax is", format(county_sales_tax, '.2f'))
print ("The total sales tax is", format(sales_tax, '.2f'))
print ("The total cost is", format(total, '.2f'))