#prompt user to enter number within range
#"Thank you" if in range
#"Sorry, out of range" if out of range - repeat the prompt

def main():
    valid_number = False
    while not valid_number:
        MIN = 0
        MAX = 100
        user_number = input("Pick a number between 0 and 100 ")
        try:
            user_number = int(user_number)
            if user_number > MAX or user_number < MIN:
                print("Sorry, number is out of range. Try again")
            else:
                print("Thank you, your number is", user_number)
                valid_number = True
        except ValueError:
            print(user_number, "is an invalid number")

main()