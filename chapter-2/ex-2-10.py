#Exercize 2-10

#Recipe calls for these ingredients:
#1.5 cups of sugar
#1 cup of butter
#2.75 cups of flour
#Produces 48 cookies. Ask the user how many cookies they want and 
#display the amount of ingredients they will need.

sugar = 1.5
butter = 1
flour = 2.75
cookies = 48

sugar_for_one = sugar / cookies
butter_for_one = butter / cookies
flour_for_one = flour / cookies

number_cookies = input("How many cookies would you like to make? ")
f_number_cookies = float(number_cookies)

amount_sugar = f_number_cookies * sugar_for_one
amount_butter = f_number_cookies * butter_for_one
amount_flour = f_number_cookies * flour_for_one

print("To make", format(f_number_cookies, '.0f'), "you will need", format(amount_sugar, '.2f'), "cups of sugar")
print("To make", format(f_number_cookies, '.0f'), "you will need", format(amount_butter, '.2f'), "cups of butter")
print("To make", format(f_number_cookies, '.0f'), "you will need", format(amount_flour, '.2f'), "cups of flour")