# Programming Exercise 2-4
#
# Program to compute a final price for five items with tax.
# This program will prompt a user for a set of five prices,
# sum them to a subtotal and calculate sales tax with tax rate stored in a constant,
# then display the results on the screen.

# Variables to hold the prices of five items, the subtotal, and the total.
# All should be initialized as floats.


# Constant for the sales tax rate.


# Get the price of each item by prompting the user.
# You will need to convert each input to a float.


# Calculate the subtotal by adding up the item prices.


# Calculate the sales tax by multiplying the subtotal by the tax rate.


# Calculate the total by adding the subtotal and tax.


# Print the values for the subtotal, tax and total.
# Label each value, and format them to display with two decimal places. 

tax = .06

price_one = input("What is the first price? ")
f_price_one = float(price_one)
price_two = input("What is the second price? ")
f_price_two = float(price_two)
price_three = input("What is the third price? ")
f_price_three = float(price_three)
price_four = input("What is the fourth price? ")
f_price_four = float(price_four)
price_five = input("What is the fifth price? ")
f_price_five = float(price_five)


subtotal = (f_price_one + f_price_two + f_price_three + f_price_four + f_price_five)
sales_tax = (subtotal * tax)
total = (sales_tax + subtotal)

print("The subtotal is", format(subtotal, '.2f'))
print("The sales tax is", format(sales_tax, '.2f'))
print("The total is", format(total, '.2f'))