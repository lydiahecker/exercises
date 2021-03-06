# Programming Exercise 4-3
#
# Program to check whether spending was within budget.
# This program prompts a user for a budget and amounts of money spent during a month,
# totals the spending and compares it to the budget,
# then displays the results, stating whether spending was within or over budget. 

# Declare variables to store amount spent, budget, total spent, and difference.
# initialize all variables as floats

    
# Get the budget from the user and cast it to a float.


# Use a while loop to get the amounts spent from the user and add them to total spent
# A while loop is preferred because we don't know how many amounts the user will enter.
# End the while loop when the user enters 0 for an amount spent.
# Note: the loop will not run if the amount spent is already zero, so set it to -1.
# 
# while amount spent is not equal to 0 ...

	# prompt the user for the amount spent and cast it to a float

    # add the amount spent to the total spent



# outside the loop, set the difference to hold budget - total spent

# Display a message with the total spent formatted to two decimal places


# if over budget, display a message with the difference formatted to two places.

# else if under budget, display a message with the difference formatted to two places.

# else display message stating that spending and budget were equal.

budget = input("What is the budget? ")
f_budget = float(budget)
amount_spent = -1
total_spent = 0

while amount_spent != 0:
    amount_spent = input("How much was spent? ")
    amount_spent = float(amount_spent)
    total_spent += amount_spent
    
difference = f_budget - total_spent
print("The total spent was", format(total_spent, '.2f'))

if total_spent > f_budget:
    print("You went over your budget by", format(difference, '.2f'))
elif total_spent < f_budget:
    print("You were under your budget by", format(difference, '.2f'))
else:
    print("You spent your budget exactly.")