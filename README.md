***Week 2; Basic Python Syntax***
1. [Expressions & Variables](#expressions-and-variables)
2. [Functions](#functions)
3. [Conditionals](#conditionals)
4. [Module 2 Graded Assessment](#module-2-graded-assessment)


# Expressions and Variables
1. [Basic Python Syntax](#basic-python-syntax-introduction)
1. [Data Types](#data-types)
1. [Varibles](#variables)
1. [Expressions, Numbers, Coversions](#expressions-numbers-and-type-conversions)
1. [Implicit vs Explicit Conversion](#implicit-vs-explicit-conversion)
1. [Practice Quiz](#practice-quiz-data-types-and-variables)

### Basic Python Syntax Introduction

- *In this module, we'll dive deeper into some basic building blocks of Python syntax, things like variables, expressions, functions, and conditional blocks.*

- *As you go through next lessons, keep in mind our main goal is to learn the language's syntax.*

### Data Types

- *Earlier we called the texts written between double quotes are called strings e.g. "Hello, World!", "7", "a+b".*

- *In programming terminology, a string is a __data type__ and a string is one kind of data type found in Python.*

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

- *Python gives you a handy way to find out what data type the given value is, called <code>type()</code> function. For example;*
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

- *Think of variables as containers for data. When you create a variable in your code, your computer reserves a chunk of its own memory to store that value. The process of storinga value inside a variable is called __assignment__.*

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

1. ***Don't use keywords(reserved keywords) or functions that Python reserves for its own.***

2. ***Don't use spaces in between.***

3. ***Must start with alphabetical letter or an underscore(<code>_</code>)***

4. ***Must be made up of only letters, integers and underscores, no special character is allowed.***

5. ***For example; <code>i_am_a_var</code> is a valid, <code>i_am_a_var5</code> is also a valid variable. But <code>1_is_a_no</code> is invalid as it begins with an integer, <code>apples_&_oranges</code> is also invalid 'cause it uses the special character &.***

6. ***Keep in mind, Python variables are case sensitive, so capitalization matters. Lowercase names, Uppercase names and all Caps names are all valid.***

### Expressions, Numbers and Type Conversions

- *Previously we saw that arithmatic operators can not be used between a string and an integer, but what happens when we add an integer with a float? Let us see;*
```Python
>>> print(34+78.4)
112.4
>>>
```

- *Sure they are different data types but behind the scenes the computer is busy automatically converting our integer 34 into a float i.e. 34.0 so that to floats(34.0 and 78.4) can be operated arithmatically. This is called __Implicit Conversion__, where the interpreter automatically converts one data type into another.*

- *So is it possible to add a string with an integer or float? Sure it is, but by manually converting the data type, called __Explicit Conversion__. Have a look on the next example carefully;*
```Python
>>> height = 8
>>> base = 6
>>> area = (1/2)*height*base
>>> print("The area of the Triangle is:" + str(area))
The area of the Triangle is:24.0
```

- *In this case, we coverted area expression to string data type.*

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

1. *We've been through some of built-in functions of Pythoon such as, the <code>print()</code>, <code>type()</code>, <code>str()</code>, but now we're going to see how to define our own functions to tell the computer to do things that the language's built-in functions don't.*

2. *To define a function, start it with the <code>def</code> keyword which is already reserved by Python(saw this on Week 1), followed by the name we want to give to our function like we name a variable.*

3. *After the name of function, we have <code>parameters</code> or <code>arguments</code> which are enclosed in parentheses <code>()</code>. Remember a parameter shouldn't start with an ineger.*

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

- *As per point 2, we defined the above function with <code>def</code> keyword, followed by the function name, here I named it <code>greet_her</code>. This is totally upto you what you name but the same rules apply for function as we name a variable.*

- *After the function name, here comes parameter or argument as <code>name</code>, enclosed by parenthesis and followed by a colon <code>:</code>, after the colon, the function body starts where you can use another function like <code>print()</code>. In the function body you can define as many line as you can*

- *As per point 6, you must start the function body to the right as <code>print("Hey, how u been? Long time no see, " + name)</code>. Remember if you lengthen the body to more lines, all should start with the same space, to the right.*

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

- *We've seen how we can pass values into a function as parameters by passing values like in defining functions, but what about getting values out of a function? This is where concept of <code>return values</code> comes to play.*

- *The work that functions do can produce new results. Sure, we can print the results on the screen, but what if we wanted to use those results later in our script or didn't want to print them at all?*

- *Imagine we need to calculate this value several times in our code. It would be useful to have a function that does this for us. Check out how this would look. We use the keyword <code>return</code> to tell Python that this is the return value of a function.*

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

- ***<code>None</code> is a special data type in Python used to indicate that things are empty or that they returned nothing.***

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

- *Although styling code doesn't make a big difference in code accuracy or errornous but poor code style can mess up with regular programmers or system admins when it's need to make changes or read the code. Even bad style can give the author headache. Imagine you are having mess with your own code, that you had written 6 months before.*

- *On the flip side, good style can make a script look almost like natural human language. It can make the scripts intent and construction immediately clear to the reader.*

- *There are no certain rules or practices to style the code. First off, you need write code __self-documenting__ as more as possible, write in a way that is readable and doesn't hide its intent.*

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
1. [If Statements](#branching-with-if-statements)
1. [Else Statements](#else-statements)
1. [Else Statements Recap](#else-statements-and-modulo-operator)
1. [Elif Statements](#elif-statements)
1. [Elif Statements Recap](#more-complex-branching-with-elif-statements)
1. [Cheat Sheet](#conditionals-cheat-sheet)
1. [Practice Quiz](#practice-quiz-conditionals)

### Comparing Things

- *Python can also compare values; such as <code>smaller than</code>, <code>greater than</code> and <code>equals to</code>, using the arithmatic operators <code><</code>, <code>></code> and <code>==</code> respectively. We use <code>!=</code> operator for that doesn't equal to.*

- *Upon comparing values, your interpreter will state True or False, known as Boolen. <code>Boolean</code> is one of the two possible states: either<code>True</code> or <code>False</code>.*

- *Check out the following examples;*
```Python
>>> print(10 > 4)
True
>>> print("cat" > "dog")
False
>>> print("cat" < "dog") # as "d" comes after "c" alphabetically
True
>>> print("cat" != "dog")
True
>>> print((1 + 78) < 10**5)
True
>>> print((1 + 79) == 80)
True
```

```Python
>>> print(1 < "1")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'int' and 'str' # it is because 1 is an integer while "1" is a string
>>> print(1 == float(1))
True
>>> print(1 == "1")
False
```

- *Although they seem similar to us(1 and "1"), but for Python interpreter, they are totally different entities.*

- ***In alphabets, the words start with Uppercase letter is lesser than the words that start with Lowercase letter. Checkout the following;***
```Python
>>> print("Cat" < "cat")
True
>>>
```

- *Apart of these inequality operators, Python also consists of <code>Logical operators</code>. There operators allow you to connect multiple statements together and perform more complex comparisons. They are <code>and</code>, <code>or</code> and <code>not</code>.*

- ***To evaluate as true, the <code>and</code> operator would need both expressions to be true at the same time.***
```Python
print("CAT" < "Cat" and "dog" > "Dog")
True
```

- ***If we use the <code>or</code> operator, instead, the expression will be true if either of the expressions is true, and false only when both expressions are false.***
```Python
>>> print("CAT" > "Cat" or "dog" < "Dog")
False
```

- ***The <code>not</code> operator inverts the value of the expression that is infront of it. That means, if the given expression is true, the boolean will be false and vice versa.***
```Python
>>> print(not 1 == 1)
False
>>> print(not 1 == 21)
True
```

### Branching with if Statements

- *The ability of a program to alter its execution sequence is known as <code>branching</code>, and it's a key component in making your scripts useful.*

- *In your scripts, you can instruct your computer to make decisions based on outputs. Let's take an IT-based example, in a company, new employees can choose the username they'll use to access the system, and usually, the chosen username needs to fit with a given set of guidelines.*

- *Let's assume that at your company, a valid username has to have atleast three characters and you,ve been asked with writing a program that will tell user if their choices valid or not.*

- *For that, you can call the function as below;*
```Python
>>> def username(name):
...     if len(name) < 3:
...        print("Invalid username! Atleast 3 characters long username is mandatory")
...
>>> username("la")
Invalid username! Atleast 3 characters long username is mandatory
```

- *As usual, we define the function using the <code>def</code> keyword. And the <code>if</code> starts within the function body, followed by a <code>condition</code> is mandatory, ending with a colon <code>:</code>. Then another function starts within its function body, it may be a print() or something else. __If the condition after <code>if</code> keyword throw the boolean as <code>true</code> then the print() function will be executed or it'll be skipped.__*

- *___Recap:___ We can use the concept of branching to have our code alter its execution sequence depending on the values of variables. We can use an __if__ statement to evaluate a comparison. We start with the __if__ keyword, followed by our comparison. We end the line with a __colon__. The body of the if statement is then indented to the right. If the comparison is __True__, the code inside the __if__ body is executed. If the comparison evaluates to __False__, __then the code block is skipped and will not be run.__*

- *Another example;*
```Python
>>> def circle_radii(radius):
...     if radius <= 0:
...        print("The given ciecle is a Point or a Imaginary circle.")
...
>>> circle_radii(-3)
The given ciecle is a Point or a Imaginary circle.
```

### else Statements

- *In the last, we went through a very useful <code>if</code> construct, but we could make our function more powerful. What if the condition of <code>if</code> code block becomes <code>False</code>, it was skipped, right? But what if we introduce a construct <code>else</code>. Like the def, if statements it also uses a colon, followed by another body block; not only a print() but they can also do calculations, modify values, return values and a lot more.*

- *Let,s checkout our last sample;*
```Python
>>> def username(name):
...     if len(name) < 3:
...        print("Invalid username! Atleast 3 charcters long username is mandtory")
...     else:
...         print("It's a valid username!")
...
>>> username("ka")
Invalid username! Atleast 3 charcters long username is mandtory
>>> username("rafla")
It's a valid username!
```

- *We can also retun values in <code>if-else</code> statements;*
```Python
>>> def circle_radii(radius):
...     if radius <= 0:
...        print("It's a Point on the Plane or It's an Imaginary Circle.")
...     else:
...          return (22/3)*(radius)**2
...
>>> circle_radii(-11)
It's a Point on the Plane or It's an Imaginary Circle.
>>> circle_radii(11)
887.3333333333333
```

- *And remember that you can choose to use as many or as few spaces as you want for the indentation, but you always need to indent and you always need to use the same number of spaces.*

- *Let's have another example;*
```Python
>>> def integer(num):
...     if num % 2 == 0:
...         return True
...     else:
...          return False
...
>>> integer(7)
False
>>> integer(198)
True
```

### Else Statements and Modulo Operator

- *We just covered the if statement, which executes code if an evaluation is true and skips the code if it’s false. But what if we wanted the code to do something different if the evaluation is false? We can do this using the else statement. The else statement follows an if block, and is composed of the keyword else followed by a colon. The body of the else statement is indented to the right, and will be executed if the above if statement doesn’t execute.*

### elif Statements

- *The <code>if</code> and <code>else</code> blocks allow us to branch execution depending on whether a condition is true or false. But what if there are more conditions to take into account? This is where the <code>elif</code> statement, which short for else if, comes into play.*

- *Before we know how to use it, we should know why to use it. Let's get back to our company validating usernames example. Assume that a new other condition is introduced by the company; the username shouldn't cross 15 characters. In this case we can use the <code>elif</code> keyword, followed by the given condition;*
```Python
>>> def username(name):
...     if len(name) < 3:
...        print("Invalid username. Atleast 3 characters longer username is mandatory.")
...     elif len(name) > 15:
...        print("Invalid username. Username needs at most 15 characters.")
...     else:
...        print("Valid username.")
...
>>> username("Keihanaikukauakahihulihe")
Invalid username. Username needs at most 15 characters.
```

- *Take a look, the <code>elif</code> statement looks very similar to the <code>if</code> statement, it is followed by a condition and a colon. And a block of code intended to the right that forms the body. The condition must be true for the body of the <code>elif</code> block to be executed.*

- *The main difference between elif and if statements is we can only write an elif block as a companion to an if block. That's because the condition of the elif statement will only be checked if the condition of the if statement wasn't true.*

- *In the above username validation example, if the length of username is less than 3 then the body of <code>if</code> will be executed and the <code>elif</code> construct will be skipped. Finally, if none of the above conditions were met, the program prints a message indicating that the username is valid.*

- *There's no limit to how many conditions can be added to the function using <code>elif</code> keyword. Suppose that the current company introduced another rule that says the username should not contain any integer. You can call the function using every condition. Cool right?*

### More Complex Branching with elif Statements

- *Building off of the if and else blocks, which allow us to branch our code depending on the evaluation of one statement, the elif statement allows us even more comparisons to perform more complex branching. Very similar to the if statements, an elif statement starts with the elif keyword, followed by a comparison to be evaluated. This is followed by a colon, and then the code block on the next line, indented to the right. An elif statement must follow an if statement, and will only be evaluated if the if statement was evaluated as false. You can include multiple elif statements to build complex branching in your code to do all kinds of powerful things!*

### Conditionals Cheat Sheet

#### Comparison Operators/ Comparators

1. *__a__ == __b__   : __a__ is equal to __b__*

2. *__a__ != __b__   : __a__ isn't equal to __b__*

3. *__a__ < __b__    : __a__ is lesser than __b__*

4. *__a__ <= __b__   : __a__ is smaller than or equal to __b__*

5. *__a__ > __b__    : __a__ is greater than __b__*

6. *__a__ >= __b__   : __a__ is greater than or equal to __b__*

#### Logical Operators

1. *__a__ and __b__   : __True__ if both __a__ and __b__ are True, __False__ otherwise.*

2. *__a__ or __b__    : __True__ if either of __a__ or __b__ is True. __False__ if both are False.*

3. *not __a__       : __True__ if a is __False__, __False__ if a is __True__.*

#### Branching blocks

- *In Python, we branch our code using <code>if</code>, <code>else</code> and <code>elif</code>. This is the branching syntax;*
```Python
if condition1:
	if-block
elif condition2:
	elif-block
else:
	else-block
```

### Practice Quiz; Conditionals

1. ___What's the value of this Python expression: (2**) == 4?___

2. ***Complete the script by filling in the missing parts. The function receives a name, then returns a greeting based on whether or not that name is "Taylor".***
```Python
def greeting(name):
  if ___ == "Taylor":
    return "Welcome back Taylor!"
  ___:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))
```

3. ***What's the output of this code if number equals to 10?***
```Python
if number > 11: 
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)
  ```

  4. ___Is "A dog" smaller than "A mouse"? Is 9999+8888 smaller or larger than 100*00? Replace the plus sign in the following code to let Python check it for you and then answer.___

5. ___If a file system has block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2 = 8192 bytes of storage. Knowing this, can you fill the gaps in the calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?___
```Python
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = ___
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = ___
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return ___
    return ___

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192
```

# Module 2 Graded Assessment

1. ***Complete the function by filling in the missing parts. The color_translator function receives the name of a color, then prints its hexadecimal value. Currently, it only supports the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.***
```Python
def color_translator(color):
	if ___ == "red":
		hex_color = "#ff0000"
	elif ___ == "green":
		hex_color = "#00ff00"
	elif ___ == "blue":
		hex_color = "#0000ff"
	___:
		hex_color = "unknown"
	return ___

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown
```

2. ***What's the value of this Python expression: "big" > "small"***

3. ***What is the elif keyword used for?***

4. ***Students in a class receive their grades as Pass/Fail. Scores of 60 or more (out of 100) mean that the grade is "Pass". For lower scores, the grade is "Fail". In addition, scores above 95 (not included) are graded as "Top Score". Fill in this function so that it returns the proper grade.***
```Python
def exam_grade(score):
	if ___:
		grade = "Top Score"
	elif ___:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail
```

5. ***What's the value of this Python expression: 11 % 5?***

6. ***Complete the body of the format_name function. This function receives the first_name and last_name parameters and then returns a properly formatted string.***

***Specially:***

***If both the last_name and the first_name parameters are supplied, the function should return like so:***
```Python
print(format_name("Ella", "Fitzgerald"))
Name: Fitzgerald, Ella
```

***If only one name parameter is supplied (either the first name or the last name) , the function should return like so:***
```Python
print(format_name("Adele", ""))
Name: Adele
```

***or***
```Python
print(format_name("", "Einstein"))
Name: Einstein
```

***Finally, if both names are blank, the function should return the empty string:***
```Python
print(format_name("", ""))
```

***Implement below:***
```Python
def format_name(first_name, last_name):
	# code goes here
	
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
```

7. ***The longest_word function is used to compare 3 words. It should return the word with the most number of characters (and the first in the list when they have the same length). Fill in the blank to make this happen.***
```Python
def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif ___:
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))
```

8. ***What’s the output of this code?***
```Python
def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))
```

9. ___What's the value of this Python expression __((10 >= 5*2) and (10 <= 5*2))__?___

10. ***The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1). Complete the body of the function so that it returns the right number.***

***Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.***
```Python
def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
# keep just the fractional part of the quotient
	return 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
```


***So Module 2(week 2) ends here***<br>
***Revise***<br>
***Attempt all quizzes***<br>