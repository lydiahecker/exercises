# Programming Exercise 5-4
#
# Program to compute monthly and annual auto expenses.
# This program prompts a user for several auto monthly expense amounts,
# then passes them to a function to total the values, annualize them,
# and display the details and totals on the screen.

# define the main function

    # Define local float variables for loan, insurance, gas, oil, tires and maintenance

    # Get the amount of the monthly loan payment from the user.

    # Get the amount of the monthly insurance from the user.

    # Get the amount of the monthly gas from the user.

    # Get the amount of the monthly oil from the user.

    # Get the amount for monthly tire wear from the users.

    # Get the amount for monthly maintenance from the user.
    
    # Call the function to summarize car expenses,
    # passing the loan, insurance, gas, oil, tires and maintenance as arguments.

# Define a function to summarize car expenses,
# it accepts loan, insurance, gas, oil, tires, and maintenance as arguments,
# calculates a monthly total and an annual total,
# and displays these totals.

    # Define local float variables for monthly total and annual total

    # calculate the monthly total
    
    # calculate the annual total
    
    # Print monthly and annual information, formatting float value to 2 decimal places.

# Call the main function to start the program

def function_monthly_expenses():
    loan = float(input("What is the monthly loan payment? "))
    insurance = float(input("What is the monthly insurance cost? "))
    gas = float(input("What is the monthly gas cost? "))
    oil = float(input("What is the monthly oil cost? "))
    tire = float(input("What is the monthly tire wear cost? "))
    maintenance = float(input("What is the monthly maintenance cost? "))
    function_car_expenses(loan, insurance, gas, oil, tire, maintenance)

def function_car_expenses(loan, insurance, gas, oil, tire, maintenance):
    monthly_total = loan + insurance + gas + oil + tire + maintenance
    annual_total = monthly_total * 12
    print("The monthly total is", format(monthly_total, '.2f'))
    print("The annual total is", format(annual_total, '.2f'))

function_monthly_expenses()