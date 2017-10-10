# Programming Exercise 4-5
#
# Program to compute total and average monthly rainfall over a span of years.
# This program gets a number of years from a user,
# then uses nested loops to prompt for rainfall for each month in each year
#	and calculate the total and the average monthly rainfall,
# then displays the number of months, total rainfall and average monthly rainfall

# Create float variables for total rainfall, monthly rainfall, average monthly rainfall

# Create int variables for number of years and number of months.



# Get number of years from the user

# Nested loop logic to loop through the years and their months
#
# Outer for loop for the number of years

	# Print the current year message

	# Inner loop for 12 months 

		# Get monthly rainfall for current month from the user
		
		# add monthly rainfall to total rainfall
		
		# increment number of months
		
			
# Calculate the average rainfall using total rainfall and number of months

# print the results on the screen, including details for total months, total rainfall,
#	and average monthly rainfall, formatting any floats to 2 decimal places.

years = input("How many years? ")
i_years = int(years)
months = i_years * 12
total_rainfall = 0
monthly_rainfall = 0

for num in range(i_years):
	for num in range(12):
		monthly_rainfall = input("What was the monthly rainfall this month?")
		monthly_rainfall = float(monthly_rainfall)
		total_rainfall += monthly_rainfall
average_monthly = total_rainfall / months

print("The total rainfall was", format(total_rainfall, '.2f'))
print("The total number of months was", format(months, '.2f'))
print("The average montly rainfall was", format(average_monthly, '.2f'))