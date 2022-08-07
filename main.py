# While Loops
name = str(input("Enter your name: "))

count = 0

while count <= 10:
    product = count * len(name)
    print(str(len(name)) + " x " + str(count) + " = " + str(product))
    count = count + 1
