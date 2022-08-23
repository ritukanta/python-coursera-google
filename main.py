# String Concatenating
name = "Max"
color = "Purple"
print("His name is " + name + " and his favourite color is " + color + ".")


# String length and multiplication
var1 = "Coommittee"
print(len(var1))

print(var1*4)


# String indexing and slicing
var2 = "Shawn"
print(var2[2])

print(var2[4])


fruit = "Pineapple"
print(fruit[2:3])
print(fruit[:4])
print(fruit[4:])


# Create new strings
var3 = "His neme is Max"
# here's the typo is "neme" > "name"
# can be fixed by creating new strings and concotenating
new_var3 = var3[:5] + "a" + var3[6:]
print(new_var3)


# Index method
var4 = "A really looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong string"
print(var4.index("g"))

print(var4.index("o"))


# Avoid VallueError by:
var5 = "Cards, Dice, Coins, Diamonds, Kings, Queens, Squads"
print("foxes" in var5)

print("Diamonds" in var5)


# Upper and Lower methods
print("tigers".upper())
print("ELEPHANTS".lower())

# another one:
key = "Success"
if key.upper() == "SUCCESS":
    print("The operation accomlished succeeefully!")


# Strip, lstrip and rstrip methods
var6 = "    Hey! we need to talk,   "

print(var6.strip())
print(var6.lstrip())
print(var6.rstrip())


# isnumeric() methods
print("97432632694391437839837K9873349873487".isnumeric())
print("875647467".isnumeric())


# join method
print("___".join(["I", "saw", "him", "last", "night!"]))


# Formatting strings
name1 = "Mabel"
number = len(name1)*3

print("Hello {}, your lucky number is: {}".format(name1, number))


# another  example of formatting strings
price = 7.5
# tax rate is 9%
tax_rate = 0.09
with_tax = price + price * tax_rate

print(price, with_tax)
# or
print("Base price is: ${:.2f}, and the price with tax is: ${:.2f}".format(
    price, with_tax))


# temperature example
def to_celsius(x):
    return (x - 32)*5/9


for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f}".format(x, to_celsius(x)))


# Lists
# defining lists, type
var7 = ["He", "was", "playing", "with", "his", "little", "girl!"]
print(var7)

print(type(var7))


# check if an element is there using keyword "in"
print("was" in var7)
print("today" in var7)


# indexing and slicing
print(var7[0])
print(var7[:4])


# Modifying the contents of a List
# Using append method

fruits = ['Pineapple', 'Mango', 'Banana', 'Apple']
fruits.append('Kiwi')
print(fruits)


# Insert in certain position
fruits.insert(0, 'Orange')
print(fruits)


# if index is larger than length of the list, doesn't matter
fruits.insert(25, 'Peach')
print(fruits)


# remove elements using remove method
fruits.remove('Banana')
print(fruits)


# remove by indexes using pop method
fruits.pop(3)
print(fruits)


# Modify or replace certain elements
fruits[2] = "Strawberry"
print(fruits)
