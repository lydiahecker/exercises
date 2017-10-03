# Programming Exercise 3-2
#
# Program to find which of two rectangles has the greater area.
# This program will get two sets of lengths and widths from a user,
# use them to calculate and compare two area values,
# and display a message comparing those areas

# Local variables
# you need length, width and area for A and for B
# initialize these as floats

# Get length A from the user and convert it to a float

# Get width A from the user and convert it to a float

# Get length B from the user and convert it to a float

# Get width B from the user and convert it to a float

# Calculate area A

# Calculate area B

# Print each area, formatting the values to 2 decimal places

# if area A is greater, print "A is greater" message.

# else if area B is greater, print "B is greater" message.

# else print "A and B are equal" message.

length_a = input("What is the first rectangle's length? ")
f_length_a = float(length_a)
width_a = input ("What is the first rectangle's width? ")
f_width_a = float(width_a)
area_a = f_length_a * f_width_a

length_b = input("what is the second rectangle's length? ")
f_length_b = float(length_b)
width_b = input("what is the second rectangle's width? ")
f_width_b = float(width_b)
area_b = f_length_b * f_width_b


print("The first rectangle's area is", format(area_a, '.2f'))
print("The second rectangle's area is", format(area_b, '.2f'))

if area_a > area_b:
    print("The first rectangle is bigger.")
elif area_a < area_b:
    print("The second rectangle is bigger.")
else:
    print("The two rectangles are the same size.")