#main
    #prompt
    #choose
    #display

from geometry import circle
from geometry import rectangle

AREA_OF_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

def main():

    choice = 0

    while choice != QUIT_CHOICE:
        display_menu()
        choice = int(input("Enter your choice: "))
        output = handle_choice(choice)
        print(output)

def display_menu():
    print(" MENU")
    print("1) Area of a circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    print("5) Quit")

def handle_circle_area():
    radius = float(input("Enter the circle's radius: "))
    return "The area is" + str(circle.area(radius))

def handle_circle_circumference():
    radius = float(input("Enter the circle's radius: "))
    return "The circumference is" + str(circle.circumference(radius))

def handle_rectangle_area():
    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))
    return "The area is" + str(rectangle.area(width,length))

def handle_rectanlge_perimeter():
    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))
    return "The perimeter is" + str(rectangle.perimeter(width,length))

def handle_choice(choice):
    if choice == AREA_OF_CIRCLE_CHOICE:
        return handle_circle_area()
    elif choice == CIRCUMFERENCE_CHOICE:
        return handle_circle_circumference()
    elif choice == AREA_RECTANGLE_CHOICE:
        return handle_rectangle_area()
    elif choice == PERIMETER_RECTANGLE_CHOICE:
        return handle_rectanlge_perimeter()
    elif choice == QUIT_CHOICE:
        return "Exiting the program..."
    else:
        return "Error: Invalid selection."

main()