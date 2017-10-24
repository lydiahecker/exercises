# Programming Exercise 5-14
#
# Program to compute kinetic energy from mass and velocity.
# This program accepts values for mass and velocity from the user in kilograms and meters per second,
# passes them to a function that returns kinetic energy in joules calculated from those values,
# and displays the result.

# define the main function

    # define local float variables for mass, velocity and kinetic energy

    # Get mass from user

    # Get velocity from user

    # Get kinetic energy in joules from the kinetic energy function

    # Display kinetic energy in joules, formatted to 2 decimal places.

# Define a function to calculate kinetic energy in joules.
# The function accepts two parameters, mass in kilograms and velocity in meters/second,
# uses a formula to calculate the joules of kinetic energy,
# and returns the result

    # Define a local variable for joules of kinetic energy

	# calculate the kinetic energy using the parameters and the conversion formula    

	# return the result

# Call the main function to start the program
def main():
    mass = 0.0
    velocity = 0.0
    kinetic_energy = 0.0
    mass, velocity = prompt_user()
    kinetic_energy = calculate_kinetic_energy(mass, velocity)
    print("The kinetic energy is", format(kinetic_energy, '.2f'))

def prompt_user():
    mass = float(input("What is the mass? "))
    velocity = float(input("What is the velocity? "))
    return mass, velocity

def calculate_kinetic_energy(mass, velocity):
    kinetic_energy = mass * velocity * velocity * .5
    return kinetic_energy

main()