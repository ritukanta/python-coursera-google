***Quizzes and Questions,***<br>
***With Solutions:***<br>
*In each Module or Week, each topic has 5 Questions and there're 10 Questions in each module graded assessment*
<br>

1. [Week 1; Hello Python](#week-1-hello-python)
> - [Intro to Programming](#intro-to-programming)
> - [Intro to Python](#intro-to-python)
> - [Hello World](#hello-world)
> - [Module 1 Graded Assessment](#module-1-graded-assessment)<br>

2. [Week 2; Basic Python Syntax](#week-2-basic-python-syntax)
> - [Expressions and Vars](#expressions-to-variables)
> - [Functions](#functions)
> - [Conditionals](#conditionals)
> - [Module 2 Graded Assessment](#module-2-graded-assessment)<br>

3. [Week 3; Loops](#week-3-loops)
> - [While Loops](#while-loops)
> - [For Loops](#for-loops)
> - [Recursion](#recursionoptional)
> - [Module 3 Graded Assessment](#module-3-graded-assessment)<br>

4. [Week 4; Strings, Lists and Dictionaries](#week-4-strings-lists-and-dictionaries)
> - [Strings](#strings)
> - [Lists](#lists)
> - [Dictionaries](#dictionaries)
> - [Module 4 Graded Assessment](#module-4-graded-assessment)<br>

5. [Week 5;OOP](#week-5-object-oriented-programming)
> - [OOP](#oop)
> - [Classes and Methods](#classes-and-methods)
> - [Code Reuse](#code-reuse)
> - [OOP Graded Assessment](#oop-graded-assessment)<br>

# Week 1; Hello Python
<br>
<br>

## Intro to programming

1. ***What is a computer program?***<br>
*ans.* *A list of instructions that the computer has to follow to reach a goal.*

2. ***What is the syntax of a language?***<br>
*ans.* *The rules of how to express things in that language.*

3. ***What is the difference between a program and a script?***<br>
*ans.* *There's not much difference, but scripts are usually simpler and shorter.*

4. ***Which scenarios good candidates choose for automation? Write down.***<br>
*ans.* *Generating a sales report, split by region and product type, Copying a file to all computers in a company, Sending personalized emails to subscribers of your website.*

5. ***What are semantics when applied to programming and pseudocode?***<br>
*ans.* *The effect the programming instructions have.*
<br>
<br>
<br>

## Intro to Python

1. ***Fill in the correct Python command to put "My first Python Program" onto the screen.***<br>
```Python
___("My first Python program")
```
*ans.*
```Python
# As have to print the message onto the screen, we use print() function

print("My first Python Program")
```

2. ***Python is an example of what type of programming langauge?***<br>
*ans.* *General purpose scripting language*

3. ***Convert this Bash command into Python:***
```Bash
echo "Have a nice day"
```
*ans.*
```Python
print("Have a nice day")
```

4. ***Fill in the correct Python commands to put "This is fun!" onto the screen 5 times.***
```Python
for i in __:
  ___("This is fun!")
  ```
  *ans.*
  ```Python
for i in range(5):
  print("This is fun!")
  ```

5. ***Select the Python code snippet that corresponds to the following Javascript snippet:***
```JavaScript
for (let i = 0; i < 10; i++) {
        console.log(i);
    }
```
*ans.*
```Python
for i in range(10):
  print(i)
  ```
<br>
<br>
<br>

## Hello World

1. ***What are functions in Python?***<br>
*ans.* *Functions are pieces of code that perform a unit of work.*

2. ***What are keywords in Python?***<br>
*ans.* *Keywords are reserved words that are used to construct instructions.*

3. ***What does the print function do in Python?***<br>
*ans.* *The print function outputs messages to the screen.*

4. ***Output a message that says, "Programming in Python is fun!" to the screen.***<br>
*ans.*
```Python
print("Programming in Python is fun!")
```

5. ***Replace the ___ placeholder and calculate the Golden ratio: (1 + √5)/2.***<br>
___Tip: to calculate the square root of a number x, you can use x**(1/2).___
```Python
ratio = ___
print(ratio)
```
*ans.*
```Python
ratio = (1 + 5**(1/2))/2
print(ratio)
```
<br>
<br>
<br>

## Module 1 Graded Assessment

1. ***What is a computer program?***<br>
*ans.* *A step-by-step recipe of what needs to be done to complete a task, that gets executed by the computer.*

2. ***What is automation?***<br>
*ans.* *The process of replacing a manual step with one that happens automatically.*

3. ***Which things can be done using Automation? Write down.***<br>
*ans.* *Creating a report of how much each sales person has sold in the last month, Setting the home directory and access permissions for new employees joining your company, Designing the new webpage for your company, Populating your company's e-commerce site with the latest products in the catlog.*

4. ***What are some characteristics of the Python progreamming language?***<br>
*ans.* *Python programs are easy to write and understand, We can practice Python using wen interpreter or codepads as well as executing it locally.*

5. ***How does Python compare to other programming languages?***<br>
*ans.* *Each programming language has its advantages and disadvantages, learning a second programming language seems easier after learning the first.*

6. ***Write a python script that outputs "Automating with Python is fun!" to the screen.***
*ans.*
```Python
print("Automating with Python is fun!")
```

7. ***Fill in the blank so that the code prints "Yellow is the color of sunshine".***<br>
```Python
color = ___
thing = ___
print(color + " is the color of " + thing)
```
*ans.*
```Python
color = "Yellow"
thing = "sunshine"
print(color + " is the color of " + thing)
```

8. ***Keeping in mind there are 86400 seconds per day, write a program that calculates how many seconds there are in a week, if a week is 7 days. Print the result on the screen.***<br>
*ans.*
```Python
seconds_per_day = 86400
# there are 7 days in a week so,
seconds_per_week = 7*86400
print(seconds_per_week)
```

9. ***Use Python to calculate how many different passwords can be formed with 6 lower case English letters.  For a 1 letter password, there would be 26 possibilities.  For a 2 letter password, each letter is independent of the other, so there would be 26 times 26 possibilities.  Using this information, print the amount of possible passwords that can be formed with 6 letters.***<br>
*ans.*
```Python
# there are 26 possibilities for a letter and there are 6 letters so,
print(26**6)
```

10. ***Most hard drives are divided into sectors of 512 bytes each.  Our disk has a size of 16 GB. Fill in the blank to calculate how many sectors the disk has.***<br>
***Note: Your result should be in the format of just a number, not a sentence.***
```Python
disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = ___

print(sector_amount)
```
*ans.*
```Python
disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = disk_size/sector_size

print(sector_amount)
```
<br>
<br>
<br>
<br>
<br>
<br>

# Week 2; Basic Python Syntax
<br>
<br>
<br>

## Expressions to Variables

1. ***In this scenario, two friends are eating dinner at a restaurant. The bill comes in the amount of 47.28 dollars. The friends decide to split the bill evenly between them, after adding 15% tip for the service. Calculate the tip, the total amount to pay, and each friend's share, then output a message saying "Each person needs to pay: " followed by the resulting number.***<br>
```Python
bill = ___
tip = bill * ___
total = bill + ___
share = ___ 
print("")
```
*ans.* 
```Python
bill = 47.28
tip = bill * (15/100)
total = bill + tip
share = total/2
print("Each person needs to pay: " + str(share))
```

2. ***This code is supposed to take two numbers, divide one by another so that the result is equal to 1, and display the result on the screen. Unfortunately, there is an error in the code. Find the error and fix it, so that the output is correct.***<br>
```Python
numerator = 10
denominator = 0
result = numerator / denominator
print(result)
```
*ans.*
```Python
numerator = 10
denominator = 0
result = numerator / (denominator+10)
print(int(result))
```

3. ***Combine the variables to display the sentence "How do you like Python so far?" ***
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
*ans.*
```Python
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(word1, word2, word3, word4, word5, word6, word7)
```

4. ***This code is supposed to display "2 + 2 = 4" on the screen, but there is an error. Find the error in the code and fix it, so that the output is correct.***
```Python
print("2 + 2 = " + (2 + 2))
```
*ans.*
```Python
print("2 + 2 = " + str(2 + 2))
```

5. ***What do you call a combination of numbers, symbols, or other values that produce a result when evaluated?***<br>
*ans.* *An expression*
<br>
<br>
<br>

## Functions

1. ***This function converts miles into kilometers. (1) Complete the function to return the result of the conversion, (2) Call the function to convert the trip distance from miles to kms, (3) Fill in the blank to print the result of the conversion and (4) Calculate the round-trip in kms by doubling the result, and fill in the blank to print the result.***
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
*ans.*
```Python
# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = my_trip_miles * 1.6

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_km*2))
```

2. ***This function compares two numbers and returns them in increasing order. Fill in the blank, so the print statement displays the result of the function call in order. Hint: if a function returns multiple values, do not forget to store these values in multiple variables.***<br>
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
*ans.*
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
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)
```

3. ***What are the values passed into functions as input called?***<br>
*ans.* *Parameters or Arguments.*

4. ***Let's revisit our lucky_number function. We want to change it, so that instead of printing the message, it returns the message. This way, the calling line can print the message, or do something else with it if needed. Fill in the blanks to complete the code to make it work.***
```Python
def lucky_number(name):
  number = len(name) * 9
  ___ = "Hello " + name + ". Your lucky number is " + str(number)
  ___
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))
```

*ans.*
```Python
def lucky_number(name):
  number = len(name) * 9
  result = "Hello " + name + ". Your lucky number is " + str(number)
  return result
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))
```

5. ***What is the purpose of the <code>def</code> keyword?***<br>
*ans.* *Used to define a new function*
<br>
<br>
<br>

## Conditionals

1. ___What is the value of this Python expression: (2**2)==4?___<br>
*ans.* *True*
```Python
>>> print((2**2)==4)
True
```

2. ***Complete the script by filling in the missing parts. The function receives a name, then returns a greeting based on whether or not that name is "Taylor".***<br>
```Python
def greeting(name):
  if ___ == "Taylor":
    return "Welcome back Taylor!"
  ___:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))
```
*ans.*
```Python
>>> def greeting(name):
...     if name == "Taylor":
...        return "Welcome back Taylor"
...     else:
...         return "Hello there, " + name
...
>>> print(greeting("Taylor"))
Welcome back Taylor
>>> print(greeting("John"))
Hello there, John
```

3. ***What's the output of this code if number equals 10?***
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
*ans.*
```Python
>>> def numeric(number):
...     if number > 11:
...         print(0)
...     elif number != 10:
...         print(1)
...     elif number >= 20 or number < 12:
...         print(2)
...     else:
...         print(3)
...
>>> numeric(10)
2
```

4. ___Is "A dog" smaller than "A mouse"? Is 9999+8888 smaller or larger than 100*100? Replace the sign in the following code to let Python check it for you and then answer.___
```Python
print("A dog" + "A mouse")
print(9999+8888 + 100*100)
```
*ans.*
```Python
>>> print("A dog" < "A mouse")
True
>>>
>>> print(9999+8888 > 100*100)
True
```
## Module 2 Graded Assessment

# Week 3; Loops
## While Loops
## For Loops
## Recursion(Optional)
## Module 3 Graded Assessment

# week 4; Strings, Lists and Dictionaries
## Strings
## Lists
## Dictionaries
## Module 4 Graded Assessment

# Week 5; Object oriented Programming
## OOP
## Classes and Methods
## Code Reuse
## OOP Graded Assessment