# Programming Exercise 3-5
#
# Program to convert a value in kilograms to Newtons, then check whether it is in range.
# This program will prompt a user for a mass in kilograms,
# convert it to Newtons and use constants to check if the weight is within range,
# then display the weight and a range message.


# Global constants for minimum, maximum and mass multiplier values


# Variables for weight and mass initialized as floats   


# Get mass from user and convert it to a float


# Calculate weight using the mass multiplier constant


# Display the weight

# If weight > maximum or < than minimum display an appropriate message


newton = 9.81
minimum = 0
maximum = 100000000000

mass = input("What is the mass in kilograms? ")
f_mass = float(mass)

weight_newtons = f_mass * newton

print("The weight is", weight_newtons, "newtons.")

if weight_newtons < minimum:
    print("The weight is too small.")
elif weight_newtons > maximum:
    print("The weight is too big.")
else:
    print("The weight is juuuuuuust right.")
