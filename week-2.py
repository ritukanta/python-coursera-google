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


# 3 # Commented 'cause of Module 2 Graded Ass. Q no. 7
#word1 = "How"
#word2 = "do"
#word3 = "you"
#word4 = "like"
#word5 = "Python"
#word6 = "so"
#word7 = "far?"
#print(word1, word2, word3, word4, word5, word6, word7)


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

# 5


def calculate_storage(filesize):
    block_size = 4096
    full_blocks = filesize//block_size
    partial_block_remainder = filesize % block_size
    if partial_block_remainder > 0:
        return 4096 * (full_blocks+1)
    return 4096


print(calculate_storage(1))
print(calculate_storage(4096))
print(calculate_storage(4097))
print(calculate_storage(6000))


# Module 2 Graded Assessment
# 1
def color_translator(color):
    if color == "red":
        hex_color = "#ff0000"
    elif color == "green":
        hex_color = "#00ff00"
    elif color == "blue":
        hex_color = "0000ff"
    else:
        hex_color = "unknown"
    return hex_color


print(color_translator("blue"))
print(color_translator("yellow"))
print(color_translator("red"))
print(color_translator("black"))
print(color_translator("green"))
print(color_translator(""))

# 2
print("big" > "small")

# 4


def exam_grade(score):
    if score > 95:
        grade = "Top Score"
    elif score >= 60:
        grade = "Pass"
    else:
        grade = "Fail"
    return grade


print(exam_grade(65))
print(exam_grade(55))
print(exam_grade(60))
print(exam_grade(95))
print(exam_grade(100))
print(exam_grade(0))

# 5
print(11 % 5)

# 6


def format_name(first_name, last_name):
    string = "Name: " + first_name + ", " + last_name
    if first_name == "":
        return "Name: " + last_name
    elif last_name == "":
        return "Name: " + first_name
    elif first_name == "" and last_name == "":
        return ""
    else:
        return string


print(format_name("Ernest", "Hemingway"))
print(format_name("", "Madonna"))
print(format_name("Voltaire", ""))
print(format_name("", ""))


# 7
def longest_word(word1, word2, word3):
    if len(word1) >= len(word2) and len(word1) >= len(word3):
        word = word1
    elif len(word2) >= len(word1) and len(word2) >= len(word3):
        word = word2
    else:
        word = word3
    return word


print(longest_word("chair", "couch", "table"))


# 8
def sum(x, y):
    return x + y


print(sum(sum(1, 2), sum(3, 4)))

# 9
print(((10 >= 5*2) and (10 <= 5*2)))

# 10


def fractional_part(nume, deno):
    fraction = nume/deno - nume//deno
    if nume == deno:
        return 0
    elif nume == 0:
        return 0
    elif deno == 0:
        return 0
    elif nume != deno:
        return fraction


print(fractional_part(5, 5))
print(fractional_part(5, 4))
print(fractional_part(5, 3))
print(fractional_part(5, 2))
#print(fractional_part(5, 0))
print(fractional_part(0, 5))
