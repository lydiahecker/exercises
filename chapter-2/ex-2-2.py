# Programming Exercise 2-2
#
# Program to compute expected profit from sales.
# This program will prompt a user for a sales projection
# and use it to calculate expected profit from a predefined profit margin
# then display the result.

# Variables to hold the sales total and the profit
# initialize them as float values

# Get the amount of projected sales.
# be sure to convert the input to a float
i_sales_projection = input("What is the sales projection? ")
f_sales_projection = float(i_sales_projection)
# Calculate the projected profit using a 23% profit margin.
profit_margin = (f_sales_projection*.23)
profit = (profit_margin + f_sales_projection)
# Print the projected profit.
# be sure to format the output to two decimal places

print("The total profit is:", format(profit, '.2f'))