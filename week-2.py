#! /usr/bin/env python3

# expressions and variables
# 1
# bill comes in the amount of $47.28
bill = 47.28
# tip of 15%
tip = bill * (15/100)
total = bill + tip
share = total/2
print("Each person needs to pay: " + str(share))


# 2
numerator = 10
denominator = 0
result = numerator / (denominator+10)
print(int(result))


# 3
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"
print(word1, word2, word3, word4, word5, word6, word7)


# 4
print("2 + 2 = " + str(2 + 2))


# functions
# 1
def convert_distance(miles):
    km = miles * 1.6


my_trip_miles = 55
my_trip_km = my_trip_miles * 1.6
print("The distance in kilometers " + str(int(my_trip_km)))
print("My round-trip in kilometers " + str(int(my_trip_km*2)))

# 2


def order_numbers(number1, number2):
    if number1 < number2:
        return number1, number2
    else:
        return number2, number1


smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)


# 4
def lucky_number(name):
    number = len(name) * 9
    result = "Hello " + name + ". Your lucky number is " + str(number)
    return result


print(lucky_number("Key"))
print(lucky_number("Cameron"))


# Conditionals
# 2
def greeting(name):
    if name == "Taylor":
        return "Welcome back Taylor"
    else:
        return "Hello there, " + name


print(greeting("Taylor"))
print(greeting("John"))

# 3


def numeric(num):
    if num > 11:
        print(0)
    elif num != 10:
        print(1)
    elif num >= 20 or num < 12:
        print(2)
    else:
        print(3)


numeric(10)

# 4
print("A dog" < "A mouse")
print(9999+8888 > 100*100)
