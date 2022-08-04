# The code that I have provided in the lessons, README, that are all of Python Interpreter and the current code was made with VSCode
# Python as Calculator
print(8+9)  # addition

print("How " + "was " + "your " + "day?")  # addition of strings

print(8**9)  # exponents

print("The value of pi is " + str(22/7))  # integer division

print(19//5)  # the integer part of division of 19 by 5; as 3 times of 5 is 15 so the integer part will be 3 here and so the result this print statement

# the remainder part of a division; 19 - 15 = 4 so the remainder part is 4
print(19 % 5)


# Type function
print(type(8))  # a int data type

print(type("8"))  # a string(str)

print(type(8.0))  # a float

print(type(8 + 9j))  # a complex data type


# Vars
# define variables
# lets calculate the area of the circle whose radius is 34
radius_of_circle = 34  # defined the var as radius
pi = 22/7  # the value of Pi
# as per the formula of area of a circle, so area_of_circle is an expression
area_of_circle = pi * (radius_of_circle**2)

print("The area of the circle whose radius is 34, is " + str(area_of_circle))

# another example of var
n1 = 3  # var n1
n2 = 5  # var n2
n3 = 7  # var n3

n4 = (n1 + n3)**n2
print("The sum of n1 and n3 is " + str(n1 + n3))
print("The power n2 of n1 + n2 is " + str((n1 + n3)**n2))


# Defining functions and Returning Values
# Let us define and call a function
# we define a function using def keyword, folllowed by the function name, here cube and then a parameter of argument within the () and last off a :
# the function body starts from here, # here we don't convert "num" to string because, here num isn't int data type but a parameter or argument
# U can define any number of lines inside the function body using vars and different functions as print()
def cube(num):
    ans = num**3
    print("The Cube of The Number is " + str(ans))


cube(5)
cube(6)
# Remember never ever miss the colon after the parameter while defining a function
# Even u can not add comments in function body, that will end up with an error


# Returning values
# Resurn statement is useful when it's time to call the function multiple times
# It is also possible that the function can return nothing
def square_area(diagonal):
    side = diagonal/2**(1/2)
    area = side**2
    return area


square_1 = square_area(9)
square_2 = square_area(13)
square_3 = square_area(8)
sum = square_1 + square_2 + square_3

print("The Sum of the Areas of Three Given Squares is, " + str(sum))


# Conditionals
# Comparing thnings
# This statement will throw a boolean as True 'cause "D" comes after "C", so it goes in the alphabetical order
print("A Dog" > "A Cat")

# this is also True because in Python, Uppercases are supposed to be smaller than lowercases
print("DOG" < "dog")

print(not "Dog" < "dog")  # Boolean is False as the given statement is true


# If statements
def logarithm(input, base):
    if input == 1:
        print("The value of the given logarithm is " + str(0))
    elif input == base:
        print("The value of the given logarithm is " + str(1))
    elif base <= 0 and base == 1:
        print("Logarith isn't defined")
    else:
        print("The logarithm is determined.")


logarithm(5, 7)
logarithm(1, 1)
