#Exercise 2-7

#Calculate the miles per gallon
#of a trip

#Inputs
distance = input("How many miles did you drive? ")
gallons = input("How many gallons did you use? ")

#Processing
f_distance = float(distance)
f_gallons = float(gallons)
miles_per_gallon = f_distance / f_gallons

#Output
print(miles_per_gallon)