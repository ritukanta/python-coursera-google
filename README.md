**_Week 5: Object-oriented Programming_**
<br>

# Object-oriented Programming

1. [Object-oriented Programming](#object-oriented-programming)
1. [Classes and Methods](#classes-and-methods)
1. [Code Reuse](#code-reuse)

### What is Object-oriented Programming?

1. [What is OOP?](#what-is-object-oriented-programming)
1. [OOP Defined](#oop-defined)
1. [Classes and Objects](#classes-and-objects)
1. [Defining New Classes](#defining-new-classes)

- _Imagine you have to describe an apple to someone has no idea what it is. You might start off by saying that an apple is a type of fruit or you might explain how how there are also a bunch of different kinds of apples exist, each with its own color, flavor, and name. Well, it's time to explain such concepts to your computer, you have to describe them by using programs and scripts as your computer doesn't even know what a fruit can be._

- _To make it easier for computers to understand these real world concepts, Python uses a programming pattern called **Object-oriented Programming**, which models such concepts using **classes** and **objects**. This is a flexible, powerful paradigm where classes represent and define concepts, while objects are instances of classes._

- _In our apple example, we can define a class called apple that will describe the properties of an apple, and we would have a number of instances of the apple class. We'll also learn about **attributes** and **methods**. The attributes are characteristics associated to a type and the methods are the functions associated to a type. In the apple, example, the attributes can be color, flavor or name of apples. And what would methods be? Well, it depends on what we're going to do with the apple._

### OOP Defined

- _In Object-oriented Programming, concepts are modeled as classes and objects. An idea is defined using a class, and an instance of the class is called an object. Almost everything in Python is an object, including integers, strings, lists, floats, dictionaries. When we create a list in Python, we're creating an object which is an instance of the list class, which represents the concepts of a list._

### Classes and Objects

- _Remember when we use the type() function, Python tells us which class the given value or variable belongs to. And since it is a class, it can have a bunch of attributes and methods. Let's take the string class for example, the content of a string is the only attribute here and there're a bunch of methods such as upper(), isnumeric() and a lot more. Similarly different classes have a bunch of different attributes and methods. So we use the <code>dir()</code> function, this gets the interpreter print to the screen a list of methods, and special methods, those start with double underscores and ends as well._

```Python
>>> dir("")
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>>
>>>
>>> dir({})
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```

- _The **dir()** function gives the list methods and special methods of a class but it doesn't tell us how can we use them. This is where the <code>help()</code> really helps in that._

```Python
>>> help([])
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |
 |  Built-in mutable sequence.
 |
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return key in self.
 |
 |  __delitem__(self, key, /)
 |      Delete self[key].
-- More  --
```

- _Python comes with a lot of predefined classes but the power of OOP is that we can also define our own classes with their own attributes and methods._

### Defining New Classes

- _Let's take our apple example, to define a basic Apple class._

```Python
>>> class Apple:
...    pass
...
>>>
```

_Sure it is too short but with these two lines we defined our first class. Talk about the syntax, we use the **class** keyword to define a new class, followed by a name, then a colon. The Python style guidelines recommend that class names should start with an uppercase apha letter, so we do. Class definitions follow the same pattern of other blocks like defining functions, loops or conditional branches. So the body of the class intended to the right. We've not added much to the current class. The **pass** keyword tells us that the class body is exiting._

- _As we called out before, we can add attributes to the class, so:_

```Python
>>> class Apple:
...    color = ""
...    flavor = ""
...
>>>
```

_So here we define two attributes as variables called **color** and **flavor**. We defined them as strings because that's what we expect the attributes to be in this Apple class, and left them as empty strings as we don't what values they can have._

- _Let's see our apple in action!_

```Python
>>> class Apple:
...    color = ""
...    flavor = ""
...
>>> jonagold = Apple()
>>> jonagold.color = "red"
>>> jonagold.flavor = "sweet"
>>> print(jonagold.color)
red
>>> print(jonagold.flavor)
sweet
```

_After defining the attributes to the Apple class, we assigned a variable called **jonagold**, a sort of apple, to create a new instance, using the Apple class as a function. Then we find the color and flavor of **jonagold**, using the **dot notation**. Dot notation lets you access any of the abilities that the object might have, called methods or information that it might store called attributes._

- _The attributes and methods of some objects can be other objects and can have attributes and methods of their own. For example, the attributes color is string so we use string methods as well, like this_

```Python
>>> print(jonagold.color.upper())
RED
```

- _Now we can can create new instances of the Apple class with different attributes._

```Python
>>> golden = Apple()
>>> golden.color = "Yello"
>>> golden.flavor = "Soft"
```

_Both **jonagold** and **golden** are the instances of the **Apple** class, and they have same attributes **color** and **flavor** with different values_

- _Can you solve the following?_

```Python
class ___:
  color = 'unknown'

rose = Flower()
rose.color = ___

violet = ___
___

this_pun_is_for_you = ___

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you)
```

# Classes and Methods

1. [Instance Methods](#instance-methods)
1. [Special Methods](#constructors-and-other-special-methods)
1. [Documenting with Docstrings](#documenting-with-docstrings)
1. [Jupyter Notebook](#about-jupyter-notebook)

### Instance Methods

- _The key to understand a method is this; methods are functions that operate on the attributes of a specific instance of a class. When we call the append method on a list, we're adding an element to the end of of that specific list and not to other lists. Let's define our own method, for that we need to define a class first_

```Python
>>> class Piglet:
...     def speak(self):
...         print("oink oink")
...
>>>
```

_You can see here that we start defining a method with the def keyword just like we would for a function, and see how the line with the def keyword is indented to the right inside the Piglet class? That's how we define a function as a method of the class. This function is receiving a parameter called self. This parameter represents the instance that the method is being executed on. Let's try this out and see what happens._

```Python
>>> class Piglet:
...     def speak(self):
...         print("oink oink")
...
>>> hamlet = Piglet()
>>> hamlet.speak()
oink oink
```

- _This works, but this makes the piglet say the same thing for all instances of the class. Umm doesn't seem so interesting! Let's try something different_

```Python
>>> class Piglet:
...      name = ""
...      def speak(self):
...          print("Oink! I'm {}! Oink!".format(self.name))
...
>>> hamlet = Piglet()
>>> hamlet.name = "Hamlet"
>>> hamlet.speak()
Oink! I'm Hamlet! Oink!
```

_If you look closely at how we wrote the **speak()** method, it is using the parameter **self**. And the **self.name** is accessing the attribute **name** from the current instance._

- _Let's see another example by creating a new instance of the same **Piglet** class._

```Python
>>>
>>> petunia = Piglet()
>>> petunia.name = "Petunia"
>>> petunia.speak()
Oink! I'm Petunia! Oink!
```

- _Now we've created two instances of the **Piglet** class each of them with their own name. When calling the speak method, each of them prints their name not the other. Variables that have different values for different instances of the same class are called **instance variables**, just like the attribute name._

### Constructors and Other Special Methods

- _Instead of creating classes with empty or default values, we can set these values when we create the instance. This ensures that we don't miss an important value and avoids a lot of unnecessary lines of code. To do this, we use a special method called a constructor. Below is an example of an Apple class with a constructor method defined._

```Python
>>> class Apple:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor
```

- _When you call the name of a class, the constructor of that class is called. This constructor method is always named **init**. You might remember that special methods start and end with two underscore characters. In our example above, the constructor method takes the self variable, which represents the instance, as well as color and flavor parameters. These parameters are then used by the constructor method to set the values for the current instance. So we can now create a new instance of the Apple class and set the color and flavor values all in go:_

```Python
>>> jonagold = Apple("red", "sweet")
>>> print(jonagold.color)
Red
```

- _In addition to the **init** constructor special method, there is also the **str** special method. This method allows us to define how an instance of an object will be printed when it’s passed to the print() function. If an object doesn’t have this special method defined, it will wind up using the default representation, which will print the position of the object in memory. Not super useful. Here is our Apple class, with the **str** method added:_

```Python
>>> class Apple:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor
...     def __str__(self):
...         return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
...
```

- _Now, when we pass an Apple object to the print function, we get a nice formatted string:_

```Python
>>> jonagold = Apple("red", "sweet")
>>> print(jonagold)
This apple is red and its flavor is sweet
```

- _This apple is red and its flavor is sweet. It's good practice to think about how your class might be used and to define a **str** method when creating objects that you may want to print later._

### Documenting with Docstrings

- _The Python help function can be super helpful for easily pulling up documentation for classes and methods. We can call the help function on one of our classes, which will return some basic info about the methods defined in our class:_

```Python
>>> class Apple:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor
...     def __str__(self):
...         return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
...
>>> help(Apple)
Help on class Apple in module __main__:

class Apple(builtins.object)
 |  Methods defined here:
 |
 |  __init__(self, color, flavor)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __str__(self)
 |      Return str(self).
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
```

- _We can add documentation to our own classes, methods, and functions using docstrings. A docstring is a short text explanation of what something does. You can add a docstring to a method, function, or class by first defining it, then adding a description inside triple quotes. Let's take the example of this function:_

```Python
>>> def to_seconds(hours, minutes, seconds):
...     """Returns the amount of seconds in the given hours, minutes and seconds."""
...     return hours*3600+minutes*60+seconds
...
```

- *We have our function called to_seconds on the first line, followed by the docstring which is indented to the right and wrapped in triple quotes. Last up is the function body. Now, when we call the help function on our to_seconds function, we get a handy description of what the function does:*

```Python
>>> help(to_seconds)
Help on function to_seconds in module __main__:

to_seconds(hours, minutes, seconds)
    Returns the amount of seconds in the given hours, minutes and seconds.
```

- _Docstrings are super useful for documenting our custom classes, methods, and functions, but also when working with new libraries or functions. You'll be extremely grateful for docstrings when you have to work with code that someone else wrote!_

### About Jupyter Notebook

- _We've aimed to make our Jupyter notebooks easy to use. But, if you get stuck, you can find more information [here](https://www.coursera.support/s/article/360004995312-Solve-problems-with-Jupyter-Notebooks?language=en_US) and [here](https://jupyter.org/install)._

# Code Reuse

1. [Object Inheritance](#object-inheritance)
1. [Object Composition](#object-composition)
1. [Modules](#python-modules)

### Object Inheritance

- _In object-oriented programming, the concept of inheritance allows you to build relationships between objects, grouping together similar concepts and reducing code duplication. Let's create a custom Fruit class with color and flavor attributes:_

```Python
>>> class Fruit:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor
...
```

- _We defined a Fruit class with a constructor for color and flavor attributes. Next, we'll define an Apple class along with a new Grape class, both of which we want to inherit properties and behaviors from the Fruit class:_

```Python
>>> class Apple(Fruit):
...     pass
...
>>> class Grape(Fruit):
...     pass
...
```

- _In Python, we use parentheses in the class declaration to have the class inherit from the Fruit class. So in this example, we’re instructing our computer that both the Apple class and Grape class inherit from the Fruit class. This means that they both have the same constructor method which sets the color and flavor attributes. We can now create instances of our Apple and Grape classes:_

```Python
>>> granny_smith = Apple("green", "tart")
>>> carnelian = Grape("purple", "sweet")
>>> print(granny_smith.flavor)
tart
>>> print(carnelian.color)
purple
```

- _Inheritance allows us to define attributes or methods that are shared by all types of fruit without having to define them in each fruit class individually. We can then also define specific attributes or methods that are only relevant for a specific type of fruit. Let's look at another example, this time with animals:_

```Python
>>> class Animal:
...     sound = ""
...     def __init__(self, name):
...         self.name = name
...     def speak(self):
...         print("{sound} I'm {name}! {sound}".format(
...             name=self.name, sound=self.sound))
...
>>> class Piglet(Animal):
...     sound = "Oink!"
...
>>> class Cow(Animal):
...     sound = "Moooo"
...
```

- _We defined a parent class, Animal, with two animal types inheriting from that class: Piglet and Cow. The parent Animal class has an attribute to store the sound the animal makes, and the constructor class takes the name that will be assigned to the instance when it's created. There is also the speak method, which will print the name of the animal along with the sound it makes. We defined the Piglet and Cow classes, which inherit from the Animal class, and we set the sound attributes for each animal type. Now, we can create instances of our Piglet and Cow classes and have them speak:_

```Python
>>> hamlet = Piglet("Hamlet")
>>> hamlet.speak()
Oink! I'm Hamlet! Oink!
...
>>> class Cow(Animal):
...     sound = "Moooo"
...
>>> milky = Cow("Milky White")
>>> milky.speak()
Moooo I'm Milky White! Moooo
```

- _We create instances of both the Piglet and Cow class, and set the names for our instances. Then we call the speak method of each instance, which results in the formatted string being printed; it includes the sound the animal type makes, along with the instance name we assigned._

### Object Composition

- _You can have a situation where two different classes are related, but there is no inheritance going on. This is referred to as composition -- where one class makes use of code contained in another class. For example, imagine we have a Package class which represents a software package. It contains attributes about the software package, like name, version, and size. We also have a Repository class which represents all the packages available for installation. While there’s no inheritance relationship between the two classes, they are related. The Repository class will contain a dictionary or list of Packages that are contained in the repository. Let's take a look at an example Repository class definition:_

```Python
>>> class Repository:
...      def __init__(self):
...          self.packages = {}
...      def add_package(self, package):
...          self.packages[package.name] = package
...      def total_size(self):
...          result = 0
...          for package in self.packages.values():
...              result += package.size
...          return result
```

- _In the constructor method, we initialize the packages dictionary, which will contain the package objects available in this repository instance. We initialize the dictionary in the constructor to ensure that every instance of the Repository class has its own dictionary._

- _We then define the add_package method, which takes a Package object as a parameter, and then adds it to our dictionary, using the package name attribute as the key.__

- _Finally, we define a total_size method which computes the total size of all packages contained in our repository. This method iterates through the values in our repository dictionary and adds together the size attributes from each package object contained in the dictionary, returning the total at the end. In this example, we’re making use of Package attributes within our Repository class. We’re also calling the values() method on our packages dictionary instance. Composition allows us to use objects as attributes, as well as access all their attributes and methods._

### Python Modules

- *Python modules are separate files that contain classes, functions, and other data that allow us to import and make use of these methods and classes in our own code. Python comes with a lot of modules out of the box. These modules are referred to as the Python Standard Library. You can make use of these modules by using the import keyword, followed by the module name. For example, we'll import the random module, and then call the randint function within this module:*
```Python
>>> import random
>>> random.randint(1,10)
8
>>> random.randint(1,10)
7
>>> random.randint(1,10)
1
```

- *This function takes two integer parameters and returns a random integer between the values we pass it; in this case, 1 and 10. You might notice that calling functions in a module is very similar to calling methods in a class. We use dot notation here too, with a period between the module and function names.*

- *Let's take a look at another module: datetime. This module is super helpful when working with dates and times.*
```Python
>>> import datetime
>>> now = datetime.datetime.now()
>>> type(now)
<class 'datetime.datetime'>
>>> print(now)
2019-04-24 16:54:55.155199
```

- *First, we import the module. Next, we call the now() method which belongs to the datetime class contained within the datetime module. This method generates an instance of the datetime class for the current date and time. This instance has some methods which we can call:*
```Python
>>> print(now)
2019-04-24 16:54:55.155199
>>> now.year
2019
>>> print(now + datetime.timedelta(days=28))
2019-05-22 16:54:55.155199
```

- *When we call the print function with an instance of the datetime class, we get the date and time printed in a specific format. This is because the datetime class has a __str__ method defined which generates the formatted string we see here. We can also directly call attributes and methods of the class, as with now.year which returns the year attribute of the instance.*

- *Lastly, we can access other classes contained in the datetime module, like the timedelta class. In this example, we’re creating an instance of the timedelta class with the parameter of 28 days. We’re then adding this object to our instance of the datetime class from earlier and printing the result. This has the effect of adding 28 days to our original datetime object.*