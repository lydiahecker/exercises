try:
    open("file.txt")
except ZeroDivisionError:
    print("Can't divide by zero.")
except FileNotFoundError as e:
    print(e.filename, "does not exist.")
