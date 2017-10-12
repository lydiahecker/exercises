# Programming Exercise 5-6
#
# Program to compute calories from fat and carbohydrate.
# This program accepts fat grams and carbohydrate grams consumed from a user,
# uses global constants to calculate the fat calories and carb calories,
# then passes them to a function for formatted display on the screen.

# Global constants for fat calories per gram and carb calories per gram

# define the main function

    # Define local float variables for grams of fat, grams of carbs, calories from fat,
    # and calories from carbs
    
    # Get grams of fat from the user.

    # Get grams of carbs from the user.

    # Calculate calories from fat.

    # Calculate calories from carbs.

    # Call the display calorie detail function, passing grams of fat, grams of carbs,
    # calories from fat and calories from carbs as arguments

# Define a function to display calorie detail.
# This function accepts grams of fat, grams of carbs, calories from fat,
# and calories from carbs as parameters,
# performs no calculations,
# but displays this information formatted for the user.

	# print each piece of information with floats formatted to 2 decimal places.

# Call the main function to start the program

fat_calories_per_gram = 9
carb_calories_per_gram = 4

def function_calories():
    grams_fat = float(input("How many grams of fat? "))
    grams_carbs = float(input("How many grams of carbs? "))
    fat_calories = grams_fat / fat_calories_per_gram
    carb_calories = grams_carbs / carb_calories_per_gram
    calorie_detail(grams_fat, grams_carbs, fat_calories, carb_calories)

def calorie_detail(grams_fat, grams_carbs, fat_calories, carb_calories):
    print("You consumed", format(grams_fat, '.2f'), "grams of fat.")
    print("You consumed", format(grams_carbs, '.2f'), "grams of carbs.")
    print("You consumed", format(carb_calories, '.2f'), "calories from carbs.")
    print("You consumed", format(fat_calories, '.2f'), "calories from fat.")

function_calories()