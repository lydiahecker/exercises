file = open("names.txt", 'w')
stuff = file.read(4)
print(stuff) # ""
file.write("I")
file.close()

line = file.readline()
while line != "":
    line = file.readline()

for line in file.readlines():
    print(line)