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


# Modifying Lists: Recap
# append
languages = ['Python', 'JavaScript', 'Java', 'C++', 'SQL', 'PHP']
languages.append('C#')
print(languages)


# insert
languages.insert(3, 'Rust')
print(languages)

languages.insert(9832176676376, 'Bootstrap')
print(languages)


# remove
languages.remove('JavaScript')
print(languages)

# languages.remove('Kotlin')
print(languages)

# pop
languages.pop(6)
print(languages)


# modify or assign new values to elements
languages[2] = 'XML'
print(languages)


# Tuples
full_name = ('Grace', 'M', 'Hopper')
print(type(full_name))

print(full_name)


# function returning more than one value, is actually returning a tuple of elements
def convert_seconds(seconds):
    hours = seconds//3600
    minutes = (seconds - hours*3600)
    remaining_seconds = seconds - hours*3600 - minutes*60
    return hours, minutes, remaining_seconds


result = convert_seconds(700)
print(result)

print(type(result))


# Iterating over Lists
animals = ['Lion', 'Zebra', 'Dolphin', 'Monkey']
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))


# another example
winners = ['Ashley', 'Dylan', 'Reese']
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))


# another
def full_emails(people):
    value = []
    for email, name in people:
        value.append("{} <{}>".format(name, email))
    return value


print(full_emails([('alex75@outlook.com', 'Alex Diego'),
      ('shay@gmail.com', 'Shay Brandt')]))
