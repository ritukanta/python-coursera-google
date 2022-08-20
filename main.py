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
