#!/usr/bin/env python3

# dir function
# help function

# int class
print(dir(1))
# print(help(1))

# float class
print(dir(1.0))
# print(help(1.0))

# str class
print(dir("1"))
# print(help("1"))

# list class
print(dir(["1"]))
# print(help(["1"]))

# dict class
print(dir({}))
# print(help({}))

# Basic class


class Apple:
    pass

# with attributes


class Apple:
    color = ""
    flavour = ""


jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"

print(jonagold.color)
print(jonagold.flavor)

print(jonagold.color.upper())
