***Week 2; Basic Python Syntax***
1. [Expressions & Variables](#expressions-and-variables)
2. [Functions](#functions)


# Expressions and Variables
1. [Basic Python Syntax](#basic-python-syntax-introduction)
1. [Data Types](#data-types)
1. [Varibles](#variables)
1. [Expres., Nos., Coversions](#expressions-numbers-and-type-conversions)
1. [Implicit vs Explicit Conversion](#implicit-vs-explicit-conversion)
1. [Practice Quiz](#practice-quiz-data-types-and-variables)

### Basic Python Syntax Introduction

- *In this module, we'll dive deeper into some basic building blocks of Python syntax, things like variables, expressions, functions, and conditional blocks.*

- *As you go through next lessons, keep in mind our main goal is to learn the langiage's syntax.*

### Data Types

- *Earlier we called the texts written between double quotes are called strings e.g. "Hello, World!", "7", "a+b".*

- *In programming terminology, a string is known as a __data type__ and a string is only kind of data type found in Python.*

- *There are bunch of others; __integer__ which represents whole numbers without a fraction like 1, 29, 598 etc, __float__ which are real numbers with fractional part, or in other words irrational numbers such as 2.5, 1.33333333, 4/7. For an example; consider __1__ and __1.0__. Here __1__ is an integer data type of <code>__int__</code> class while __1.0__ is of <code>__float__</code> class.*

- *Complex numbers or Imaginary numbers are written in the form, <code>x + yj</code>, where <code>x</code> is the real part and </code>y</code> is the imaginary part. This comes under <code>__complex__</code> class*

- *Generally, computer doesn't know how mix different data types, for example adding two integers makes perfect sense to computer, or two strings also makes sense; like this;*
```Python
>>> print(7+8)
15
>>> print("How" + " was" + " your" + " day?")
How was your day?
>>>
```

- *But our computer doesn't know what to make of it; adding different data types;*
```Python
>>> print(7+"8")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

- *So there you go, your __first error__ in this course so far, which says it's a <code>TypeError</code>, and an <code>int</code> and a <code>str</code> data type can not be added. Here 7 is an integer while "8" is a string, remember 8 isn't a string but "8" is.*

- *Python gives you a handy way to find out what data type the given value is. For example;*
```Python
>>> print(type(7))
<class 'int'>
>>> print(type("7"))
<class 'str'>
>>> print(type(7.0))
<class 'float'>
>>> print(type(7+8j))
<class 'complex'>
```

### Variables

- *Variables are the names that we give to certain values in our programms.*

- *Think of variables as containers for data. When you create a variable in your code, your computer reserves a chunk of its own memory to store that value. The process of storinga value inside a variable is called assignment.*

- *For example, let us calculate the area of a rectangle by giving names of variables and storing certain data or values inside them;*
```Python
>>> length = 25
>>> width = 15
>>> area = length * width
>>>
>>> print(area)
375
```

- *Here we assigned the __length__ variable with the value of 25, __width__ variable with the value of 15, __area__ with the expression of length times of width and our Python interpreter understood the assignment.*

- *An expression is a combination of numbers, symbols or other variables that produce a result when evaluated. Clearly here area is an expression.*

- *As we saw we can name a variable and give it value using <code>=</code> sign i.e. variable = value. But there are certain rules and restrictions to name a variable.*

#### Variable Naming Restrictions

1. ***Don't use keywords(discused in week 1) or functions that Python reserves for its own.***

2. ***Don't use spaces in between.***

3. ***Must start with alphabetical letter or an underscore(<code>_</code>)***

4. ***Must be made up of only letters, integers and underscores.***

5. ***For example; <code>i_am_a_var</code> is a valid, <code>i_am_a_var5</code> is also a valid variable. But <code>1_is_a_no</code> is invalid as it begins with an integer, <code>apples_&_oranges</code> is also invalid 'cause it uses the special character &.***

6. ***Keep in mind, Python variables are case sensitive, so capitalization matters. Lowercase names, Uppercase names and all Caps names are all valid.***

### Expressions, Numbers and Type Conversions

- *Previously we saw arithmatic operators can not be used between a string and an integer, but what happens when we add an integer with a float? Let us see;*
```Python
>>> print(34+78.4)
112.4
>>>
```

- *Sure they are different data types but behind the scenes the computer is busy automatically converting our integer 34 into a float i.e. 34.0 so that to floats(34.0 and 78.4) can be operated arithmatically. This is called __Implicit Conversion__, where the interpreter automatically converts one data type into another.*

- *So is it possible to add a string with an integer or float? Sure it is. By manually converting the data type, called __Explicit Conversion__. Have a look on the next example carefully;*
```Python
>>> height = 8
>>> base = 6
>>> area = (1/2)*height*base
>>> print("The area of the Triangle is:" + str(area))
The area of the Triangle is:24.0
```

- *In this case, we coverted area expression to string data type*

### Implicit vs Explicit Conversion

- ***Implicit conversion is where the interpreter helps us out and automatically converts one data type into another, without having to explicitly tell it to do so.***

- ***By contrast, explicit conversion is where we manually convert from one data type to another by calling the relevant function for the data type we want to convert to. As in last example converted the data type(area) into a string using <code>str()</code> function.***

### Practice Quiz; Data Types and Variables

1. ***In this scenario, two friends are eating dinner at a restaurant. The bill comes in the amount of 47.28 dollars. The friends decide to split the bill evenly between them, after adding 15% tip for the service. Calculate the tip, the total amount to pay, and each friend's share, then output a message saying "Each person needs to pay: " followed by the resulting number. Given;***
```Python
bill = ___
tip = bill * ___
total = bill + ___
share = ___ 
print("")
```

2. ***This code is supposed to take two numbers, divide one by another so that the result is equal to 1, and display the result on the screen. Unfortunately, there is an error in the code. Find the error and fix it, so that the output is correct.***
```Python
numerator = 10
denominator = 0
result = numerator / denominator
print(result)
```

3. ***Combine the variables to display the sentence "How do you like Python so far?"***
```Python
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(___)
```

4. ***This code is supposed to display "2 + 2 = 4" on the screen, but there is an error. Find the error in the code and fix it, so that the output is correct.***
```Python
print("2 + 2 = " + (2 + 2))
```

5. ***What do you call a combination of numbers, symbols, or other values that produce a result when evaluated?***

# Functions
1. [Defining Functions](#defining-functions)

### Defining Functions