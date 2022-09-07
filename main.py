#!/usr/bin/env python3

# dir function
# help function

# int class
import datetime
import random


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


# Another example
# Defining a class of Furniture
class Furniture:
    color = ""
    material = ""


# there's an instance for a brown wood table
table = Furniture()
table.color = "brown"
table.material = "wood"

# there is an instance for red leather couch
couch = Furniture()
couch.color = "red"
couch.material = "leather"

# defining function for class Furniture


def describe_furniture(piece):
    return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))


print(describe_furniture(table))
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch))
# Should be "This piece of furniture is made of red leather"


# Methods
class Piglet:
    name = ""

    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))


hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()


# __init__ and __str__
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)


jonagold = Apple("red", "sweet")
print(jonagold.color)
print(jonagold)


# Documenting with Docstrings
def to_seconds(hours, minutes, seconds):
    """Returns the amount of seconds in the given hours, minutes and seconds."""
    return hours*3600 + minutes*60 + seconds


help(to_seconds)

# Inheritance


class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


# Define child classes using inheritance of class Frut

class Apple(Fruit):
    pass


class Grape(Fruit):
    pass


granny_smiht = Apple("green", "tart")
carnelian = Grape("purple", "sweet")

print(granny_smiht.flavor)

print(carnelian.flavor)


# Another example of Inheritance
class Animal:
    sound = ""

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("{sound} I'm {name}! {sound}".format(
            name=self.name, sound=self.sound))


class Piglet(Animal):
    sound = "Oink!"


hamlet = Piglet("Hamlet")
hamlet.speak()


class Cow(Animal):
    sound = "Moooo"


milky = Cow("Milky White")
milky.speak()

# Object Composition


class Repository:
    def __init__(self):
        self.packages = {}

    def add_package(self, package):
        self.packages[package.name] = package

    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result


# Python Modules
# Randint returns random integer
print(random.randint(1, 10))

print(random.randint(1, 10))

now = datetime.datetime.now()
print(type(now))

# returns current time
print(now)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)


# time delta for future time
print(now + datetime.datetime(days=28))
