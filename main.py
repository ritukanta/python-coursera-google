# While Loops
name = str(input("Enter your name: "))

count = 0

while count <= 10:
    product = count * len(name)
    print(str(len(name)) + " x " + str(count) + " = " + str(product))
    count = count + 1

# Another example;
x = 0

while x < 5:
    print("Not there yet, x = " + str(x))
    x += 1


# An infinite while loop
def number(num):
    x = 2
    while num % x == 0:
        print("The remainder is " + str(num % x))
        break


number(8)


# for loop
for x in range(7):
    print(x)


# another
friends = ["Taylor", "Alex", "Mat"]
for name in friends:
    print("Hi " + name)


# another
values = [23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print("Total sum: " + str(sum) + " - Average: " + str(int(sum/length)))


# a nested for loop
# the dominoes game
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
        print()
