***Week 2; Basic Python Syntax***
1. [Expressions & Variables](#expressions-and-variables)
2. [Functions](#functions)
3. [Conditionals](#conditionals)


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
1. [Returning Values](#returning-values)
1. [Returning Values Recap](#returning-values---recap)
1. [Principles of Code Reuse](#principles-of-code-reuse)
1. [Code Style](#code-style-refactoring-and-commenting)
1. [Practice Quiz](#practice-quiz-functions)

### Defining Functions

1. *We've been through some of built-in functions on Pythoon such as, the <code>print()</code>, <code>type()</code>, <code>str()</code> etc, but now we're going to see how to define our own functions to tell the computer to do things that the language is built-in functions don't.*

2. *To define a function by you, start it with the <code>def</code> keyword which is already reserved by Python(saw this on Week 1), followed by the name we want to give our function alike we name a variable.*

3. *After the name of function, we have <code>parameters</code> or <code>arguments</code> which are enclosed in parentheses <code>()</code>. Remember a parameter shouldn't start with an ineger*

4. *A function can have no parameter or argument or it can have multiple parameters or arguments.*

- *Parameters allow us to call a function and pass it data, with the data being available inside the function as variables with the same name as the parameters. Lastly, we put a colon <code>:</code> at the end of the line.*

5. *After the colon <code>:</code>, the function body starts.*

6. *It’s important to note that in Python the function body is delimited by indentation. This means that all code indented to the right following a function definition is part of the function body. The first line that’s no longer indented is the boundary of the function body. It’s up to you how many spaces you use when indenting -- just make sure to be consistent. So if you choose to indent with four spaces, you need to use four spaces everywhere in your code.*

- *Let us define a function with an example, that will explain the above points;*
```Python
>>> def greet_her(name):
...     print("Hey, how u been? Long time no see, " + name)
...
>>> greet_her("Milli")
Hey, how u been? Long time no see, Milli
>>>
```

- *As per point 2, we defined the above example's function with <code>def</code> keyword, followed by the function name, here I named it <code>greet_her</code>. This is totally upto you what you name but the same rules apply for function as we name variables*

- *After the function name, here comes parameter or argument as <code>name</code>, enclosed by parenthesis and ended with a colon <code>:</code>, after the colon, the function body starts where you can use another function like <code>print()</code>. In the function body you can define as many line as you can*

- *As per point 6, you must start the function body to the right as <code>print("Hey, how u been? Long time no see, " + name)</code>. Remember if you lengthen the body to more lines, all should start with the same space.*

- *Let's clear this with the following example;*
```Python
>>> def greet_them(name1, name2, name3, name4):
...    print("hey yo bro! " + name1)
...    print("how u doing, angel, " + name2)
...    print("yikes! " + name3)
...    print("hell ya, cogy posy " + name4)
...
>>> greet_them("Lisa", "Jisoo", "Jennie", "Rosie")
hey yo bro! Lisa
how u doing, angel, Jisoo
yikes! Jennie
hell ya, cogy posy Rosie
```

### Returning Values

- *We've seen how we can pass values into a function as parameters by passing values like in defining functions, but what about getting values out oof a function? This is where concept of <code>return values</code> comes to play.*

- *The work that functions do can produce new results. Sure, we can print the results on the screen, but what if we wanted to use those results later in our script or didn't want to print them at all?*

- *Imagine we need to calculate this value several times in our code. It would be useful to have a function that does this for us. Check out how this would look. We use the keyword return to tell Python that this is the return value of a function.*

- *For example;*
```Python
>>> def area_of_triangle(length, width):
...     return length*width/2
...
>>> area_of_1st_tri = area_of_triangle(16, 9)
>>> area_of_2nd_tri = area_of_triangle(10, 6)
>>> sum = area_of_1st_tri + area_of_2nd_tri
>>> print("Sum of areas of the 2 triangles is " +  str(sum))
Sum of areas of the 2 triangles is 102.0
```

- *In the above sample, we had to calculate the area of two triangles so here the return value determined length multiplied with width devided by 2 which is the area of a triangle. With <code>return</code> value statement we don't use parenthesis or colon.*

- *This shows the power of the return statement. It allows us to combine calls to functions and to more complex operations which makes your code more reusable.*

- *Another example;*
```Python
>>> def convert_seconds(seconds):
...     hours = seconds//3600
...     minutes =  (seconds-hours*3600)//60
...     remaining_secs = seconds-hours*3600-minutes*60
...     return hours, minutes, remaining_secs
...
>>> hours, minutes, seconds = convert_seconds(80)
>>> print(hours, minutes, seconds)
0 1 20
```

- *It is also possible to return no value, see this example;*
```Python
>>> def greet(name):
...     print("Welcome, " + name)
...
>>> result = greet("Christine")
Welcome, Christine
>>> print(result)
None
```

- *<code>None</code> is a special data type in Python used to indicate that things are empty or that they returned nothing.*

### Returning Values - Recap

- *Sometimes we don't want a function to simply run and finish. We may want a function to manipulate data we passed it and then return the result to us. This is where the concept of return values comes in handy. We use the return keyword in a function, which tells the function to pass data back. When we call the function, we can store the returned value in a variable. Return values allow our functions to be more flexible and powerful, so they can be reused and called multiple times.*

- *Functions can even return multiple values. Just don't forget to store all returned values in variables! You could also have a function return nothing, in which case the function simply exits.*

### Principles of Code Reuse

- *As we've called out before, functions are powerful because you can create your own. You can use them to organize the code in your scripts into logical blocks, which makes the code you write easier to use and reuse. Check out this example.*
```Python
>>> name = "Jay"
>>> number = len(name)*7
>>> print("Hey, " + name + ", your lucky number is " + str(number))
Hey, Jay, your lucky number is 21
```

- *First off, we defined the variable <code>name</code>, in the second line the <code>number</code> variable reused the code of variable "name". <code>len()</code> or length function is used to calculate length of words. Here we defined lucky number of name "Jay". What's your lucky number though?*

### Code Style; Refactoring and Commenting

- *Although styling code doesn't make a big difference in code accuracy or errornous but poor code style can mess up with regular programmers or system admins when it's need to make changes or read the code. Even bad style can give the author headache. Imagine you are having mess with your own code, that you had written before 6 months.*

- *On the flip side, good style can make a script look almost like natural human language. It can make the scripts intent and construction immediately clear to the reader.*

- *There are no certain rules or practices to style the code. First off, you need write code self-documenting as more as possible, write in a way that is readable and doesn't hide its intent.*

- *See the example, which is really messy to look at;*
```Python
>>> def calculate(r):
...     q=3.14
...     z=q*(r**2)
...     print(z)
...
>>> calculate(6)
113.04
```

- *In programming, re-writing and self-documenting the code is called <code>refactoring</code>. So let's refactor this code, so that it will be more understandable;*
```Python
>>> def circle_area(radius):
...     pi = 3.14
...     area = pi * (radius**2)
...     print(area)
...
>>> circle_area(6)
113.04
```

- *Moreover refactoring and self-documenting, some times you can add a bit explanatory texts to the code. You can do this by adding that we call a <code>comment</code>, which starts with a hash <code>#</code>. When your computer sees a hash character and understands that it should ignore everything that comes after that character on that line. Check out how this looks.*
```Python
# How comments look like in Python
```
- *When your computer sees a hash character and understands that it should ignore everything that comes after that character on that line. Check out how this looks.*

### Practice Quiz; Functions

1. ***This function converts miles to kilometers (km).***
```Python
# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = ___

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + ___)

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + ___)
```

2. ***This function compares two numbers and returns them in increasing order.***
***Hint: if a function returns multiple values, don't forget to store these values in multiple variables***
```Python
# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
___, ___ = order_numbers(100, 99)
print(smaller, bigger)
```

3. ***What are the values passed into functions as input called?***

4. ***Let's revisit our lucky_number function. We want to change it, so that instead of printing the message, it returns the message. This way, the calling line can print the message, or do something else with it if needed. Fill in the blanks to complete the code to make it work.***
```Python
def lucky_number(name):
  number = len(name) * 9
  ___ = "Hello " + name + ". Your lucky number is " + str(number)
  ___
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))
```

5. ***What is the purpose of the def keyword?***

# Conditionals
1. [Comparing Things](#comparing-things)

### Comparing Things

- *Python can also compare values; such <code>smaller than</code>, <code>greater than</code> and <code>equals to</code>, using the arithmatic operators <code><</code>, <code>></code> and <code>==</code> respectively.*

- *Upon comparing values, your interpreter will state True or False, known as Boolen. <code>Boolean</code> is one of the two possible states: either<code>True</code> or <code>False</code>.*

- *Check out the following examples;*
```Python
