***Week 5: Object-oriented Programming***
<br>

# Object-oriented Programming

### What is Object-oriented Programming?

- *Imagine you have to describe an apple to someone has no idea what it is. You might start off by saying that an apple is a type of fruit or you might explain how how there are also a bunch of different kinds of apples exist, each with its own color, flavor, and name. Well, it's time to explain such concepts to your computer, you have to describe them by using programs and scripts as your computer doesn't even know what a fruit can be.*

- *To make it easier for computers to understand these real world concepts, Python uses a programming pattern called __Object-oriented Programming__, which models such concepts using __classes__ and __objects__. This is a flexible, powerful paradigm where classes represent and define concepts, while objects are instances of classes.*

- *In our apple example, we can define a class called apple that will describe the properties of an apple, and we would have a number of instances of the apple class. We'll also learn about __attributes__ and __methods__. The attributes are characteristics associated to a type and the methods are the functions associated to a type. In the apple, example, the attributes can be color, flavor or name of apples. And what would methods be? Well, it depends on what we're going to do with the apple.*

### OOP Defined

- *In Object-oriented Programming, concepts are modeled as classes and objects. An idea is defined using a class, and an instance of the class is called an object. Almost everything in Python is an object, including integers, strings, lists, floats, dictionaries. When we create a list in Python, we're creating an object which is an instance of the list class, which represents the concepts of a list.*

### Classes and Objects

- *Remember when we use the type() function, Python tells us which class the given value or variable belongs to. And since it is a class, it can have a bunch of attributes and methods. Let's take the string class for example, the content of a string is the only attribute here and there're a bunch of methods such as upper(), isnumeric() and a lot more. Similarly different classes have a bunch of different attributes and methods. So we use the <code>dir()</code> function, this gets the interpreter print to the screen a list of methods, and special methods, those start with double underscores and ends as well.*
```Python
>>> dir("")
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>>
>>>
>>> dir({})
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```

- *The __dir()__ function gives the list methods and special methods of a class but it doesn't tell us how can we use them. This is where the <code>help()</code> really helps in that.*
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

- *Python comes with a lot of predefined classes but the power of OOP is that we can also define our own classes with their own attributes and methods.*

### Defining New Classes

- *Let's take our apple example, to define a basic Apple class.*
```Python
>>> class Apple:
...    pass
...
>>>
```
*Sure it is too short but with these two lines we defined our first class. Talk about the syntax, we use the __class__ keyword to define a new class, followed by a name, then a colon. The Python style guidelines recommend that class names should start with an uppercase apha letter, so we do. Class definitions follow the same pattern of other blocks  like defining functions, loops or conditional branches. So the body of the class intended to the right. We've not added much to the current class. The __pass__ keyword tells us that the class body is exiting.*

- *As we called out before, we can add attributes to the class, so:*
```Python
>>> class Apple:
...    color = ""
...    flavor = ""
...
>>>
```
*So here we define two attributes as variables called __color__ and __flavor__. We defined them as strings because that's what we expect the attributes to be in this Apple class, and left them as empty strings as we don't what values they can have.*

- *Let's see our apple in action!*
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
*After defining the attributes to the Apple class, we assigned a variable called __jonagold__, a sort of apple, to create a new instance, using the Apple class as a function. Then we find the color and flavor of __jonagold__, using the __dot notation__. Dot notation lets you access any of the abilities that the object might have, called methods or information that it might store called attributes.*

- *The attributes and methods of some objects can be other objects and can have attributes and methods of their own. For example, the attributes color is string so we use string methods as well, like this*
```Python
>>> print(jonagold.color.upper())
RED
```

- *Now we can can create new instances of the Apple class with different attributes.*
```Python
>>> golden = Apple()
>>> golden.color = "Yello"
>>> golden.flavor = "Soft"
```
*Both __jonagold__ and __golden__ are the instances of the __Apple__ class, and they have same attributes __color__ and __flavor__ with different values*

- *Can you solve the following?*
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