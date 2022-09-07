**_Quizzes and Questions,_**<br>
**_With Solutions:_**<br>
_In each Module or Week, each topic has 5 Questions and there're 10 Questions in each module graded assessment_
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

1. **_What is a computer program?_**<br>
   _ans._ _A list of instructions that the computer has to follow to reach a goal._

2. **_What is the syntax of a language?_**<br>
   _ans._ _The rules of how to express things in that language._

3. **_What is the difference between a program and a script?_**<br>
   _ans._ _There's not much difference, but scripts are usually simpler and shorter._

4. **_Which scenarios good candidates choose for automation? Write down._**<br>
   _ans._ _Generating a sales report, split by region and product type, Copying a file to all computers in a company, Sending personalized emails to subscribers of your website._

5. **_What are semantics when applied to programming and pseudocode?_**<br>
   _ans._ _The effect the programming instructions have._
   <br>
   <br>
   <br>

## Intro to Python

1. **_Fill in the correct Python command to put "My first Python Program" onto the screen._**<br>

```Python
___("My first Python program")
```

_ans._

```Python
# As have to print the message onto the screen, we use print() function

print("My first Python Program")
```

2. **_Python is an example of what type of programming langauge?_**<br>
   _ans._ _General purpose scripting language_

3. **_Convert this Bash command into Python:_**

```Bash
echo "Have a nice day"
```

_ans._

```Python
print("Have a nice day")
```

4. **_Fill in the correct Python commands to put "This is fun!" onto the screen 5 times._**

```Python
for i in __:
  ___("This is fun!")
```

_ans._

```Python
for i in range(5):
print("This is fun!")
```

5. **_Select the Python code snippet that corresponds to the following Javascript snippet:_**

```JavaScript
for (let i = 0; i < 10; i++) {
        console.log(i);
    }
```

_ans._

```Python
for i in range(10):
  print(i)
```

<br>
<br>
<br>

## Hello World

1. **_What are functions in Python?_**<br>
   _ans._ _Functions are pieces of code that perform a unit of work._

2. **_What are keywords in Python?_**<br>
   _ans._ _Keywords are reserved words that are used to construct instructions._

3. **_What does the print function do in Python?_**<br>
   _ans._ _The print function outputs messages to the screen._

4. **_Output a message that says, "Programming in Python is fun!" to the screen._**<br>
   _ans._

```Python
print("Programming in Python is fun!")
```

5. **_Replace the \_\_\_ placeholder and calculate the Golden ratio: (1 + √5)/2._**<br>
   **_Tip: to calculate the square root of a number x, you can use x\*\*(1/2)._**

```Python
ratio = ___
print(ratio)
```

_ans._

```Python
ratio = (1 + 5**(1/2))/2
print(ratio)
```

<br>
<br>
<br>

## Module 1 Graded Assessment

1. **_What is a computer program?_**<br>
   _ans._ _A step-by-step recipe of what needs to be done to complete a task, that gets executed by the computer._

2. **_What is automation?_**<br>
   _ans._ _The process of replacing a manual step with one that happens automatically._

3. **_Which things can be done using Automation? Write down._**<br>
   _ans._ _Creating a report of how much each sales person has sold in the last month, Setting the home directory and access permissions for new employees joining your company, Designing the new webpage for your company, Populating your company's e-commerce site with the latest products in the catlog._

4. **_What are some characteristics of the Python progreamming language?_**<br>
   _ans._ _Python programs are easy to write and understand, We can practice Python using wen interpreter or codepads as well as executing it locally._

5. **_How does Python compare to other programming languages?_**<br>
   _ans._ _Each programming language has its advantages and disadvantages, learning a second programming language seems easier after learning the first._

6. **_Write a python script that outputs "Automating with Python is fun!" to the screen._**
   _ans._

```Python
print("Automating with Python is fun!")
```

7. **_Fill in the blank so that the code prints "Yellow is the color of sunshine"._**<br>

```Python
color = ___
thing = ___
print(color + " is the color of " + thing)
```

_ans._

```Python
color = "Yellow"
thing = "sunshine"
print(color + " is the color of " + thing)
```

8. **_Keeping in mind there are 86400 seconds per day, write a program that calculates how many seconds there are in a week, if a week is 7 days. Print the result on the screen._**<br>
   _ans._

```Python
seconds_per_day = 86400
# there are 7 days in a week so,
seconds_per_week = 7*86400
print(seconds_per_week)
```

9. **_Use Python to calculate how many different passwords can be formed with 6 lower case English letters. For a 1 letter password, there would be 26 possibilities. For a 2 letter password, each letter is independent of the other, so there would be 26 times 26 possibilities. Using this information, print the amount of possible passwords that can be formed with 6 letters._**<br>
   _ans._

```Python
# there are 26 possibilities for a letter and there are 6 letters so,
print(26**6)
```

10. **_Most hard drives are divided into sectors of 512 bytes each. Our disk has a size of 16 GB. Fill in the blank to calculate how many sectors the disk has._**<br>
    **_Note: Your result should be in the format of just a number, not a sentence._**

```Python
disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = ___

print(sector_amount)
```

_ans._

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

1. **_In this scenario, two friends are eating dinner at a restaurant. The bill comes in the amount of 47.28 dollars. The friends decide to split the bill evenly between them, after adding 15% tip for the service. Calculate the tip, the total amount to pay, and each friend's share, then output a message saying "Each person needs to pay: " followed by the resulting number._**<br>

```Python
bill = ___
tip = bill * ___
total = bill + ___
share = ___
print("")
```

_ans._

```Python
bill = 47.28
tip = bill * (15/100)
total = bill + tip
share = total/2
print("Each person needs to pay: " + str(share))
```

2. **_This code is supposed to take two numbers, divide one by another so that the result is equal to 1, and display the result on the screen. Unfortunately, there is an error in the code. Find the error and fix it, so that the output is correct._**<br>

```Python
numerator = 10
denominator = 0
result = numerator / denominator
print(result)
```

_ans._

```Python
numerator = 10
denominator = 0
result = numerator / (denominator+10)
print(int(result))
```

3. **_Combine the variables to display the sentence "How do you like Python so far?" _**

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

_ans._

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

4. **_This code is supposed to display "2 + 2 = 4" on the screen, but there is an error. Find the error in the code and fix it, so that the output is correct._**

```Python
print("2 + 2 = " + (2 + 2))
```

_ans._

```Python
print("2 + 2 = " + str(2 + 2))
```

5. **_What do you call a combination of numbers, symbols, or other values that produce a result when evaluated?_**<br>
   _ans._ _An expression_
   <br>
   <br>
   <br>

## Functions

1. **_This function converts miles into kilometers. (1) Complete the function to return the result of the conversion, (2) Call the function to convert the trip distance from miles to kms, (3) Fill in the blank to print the result of the conversion and (4) Calculate the round-trip in kms by doubling the result, and fill in the blank to print the result._**

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

_ans._

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

2. **_This function compares two numbers and returns them in increasing order. Fill in the blank, so the print statement displays the result of the function call in order. Hint: if a function returns multiple values, do not forget to store these values in multiple variables._**<br>

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

_ans._

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

3. **_What are the values passed into functions as input called?_**<br>
   _ans._ _Parameters or Arguments._

4. **_Let's revisit our lucky_number function. We want to change it, so that instead of printing the message, it returns the message. This way, the calling line can print the message, or do something else with it if needed. Fill in the blanks to complete the code to make it work._**

```Python
def lucky_number(name):
  number = len(name) * 9
  ___ = "Hello " + name + ". Your lucky number is " + str(number)
  ___

print(lucky_number("Kay"))
print(lucky_number("Cameron"))
```

_ans._

```Python
def lucky_number(name):
  number = len(name) * 9
  result = "Hello " + name + ". Your lucky number is " + str(number)
  return result

print(lucky_number("Kay"))
print(lucky_number("Cameron"))
```

5. **_What is the purpose of the <code>def</code> keyword?_**<br>
   _ans._ _Used to define a new function_
   <br>
   <br>
   <br>

## Conditionals

1. **_What is the value of this Python expression: (2\*\*2)==4?_**<br>
   _ans._ _True_

```Python
>>> print((2**2)==4)
True
```

2. **_Complete the script by filling in the missing parts. The function receives a name, then returns a greeting based on whether or not that name is "Taylor"._**<br>

```Python
def greeting(name):
  if ___ == "Taylor":
    return "Welcome back Taylor!"
  ___:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))
```

_ans._

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

3. **_What's the output of this code if number equals 10?_**

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

_ans._

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

4. **_Is "A dog" smaller than "A mouse"? Is 9999+8888 smaller or larger than 100\*100? Replace the sign in the following code to let Python check it for you and then answer._**

```Python
print("A dog" + "A mouse")
print(9999+8888 + 100*100)
```

_ans._

```Python
>>> print("A dog" < "A mouse")
True
>>>
>>> print(9999+8888 > 100*100)
True
```

5. **_If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096\*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?_**

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

_ans._

```Python
      def calculate_storage(filesize):
          block_size = 4096
          # Use floor division to calculate how many blocks are fully occupied
          full_blocks = filesize // block_size
          # Use the modulo operator to check whether there's any remainder
          partial_block_remainder = filesize % block_size
          # Depending on whether there's a remainder or not, return
          # the total number of bytes required to allocate enough blocks
          # to store your data.
          if partial_block_remainder > 0:
            return 4096 * (full_blocks + 1)
          return 4096

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192
```

## Module 2 Graded Assessment

1. **_Complete the function by filling in the missing parts. The color_translator function receives the name of a color, then prints its hexadecimal value. Currently it only supports the three additive primary colors: red, green, blue, so it returns for all other colors._**

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

_ans._

```Python
      def color_translator(color):
            if color == "red":
	            hex_color = "#ff0000"
	      elif color == "green":
		      hex_color = "#00ff00"
	      elif color == "blue":
		      hex_color = "#0000ff"
	      else:
		      hex_color = "unknown"
	      return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown
```

2. **_What's the value of this Python expression: "big" > "small"?_**<br>
   _ans. False_

3. **_What is the elif keyword used for?_**<br>
   _ans. Two handle more than two comparison cases_

4. **_Students in a class receive their grades as Pass/Fail. Scores of 60 or more(out of 100) mean that the grade is "Pass". For lower scores, the grade is "Fail". In addition, scores above 95(not included) are graded as "Top Score". Fill in this function so that it returns the proper grades._**

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

_ans._

```Python
      def exam_grade(score):
	      if score > 95:
		      grade = "Top Score"
	      elif score >= 60:
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

5. **_What's the value of this Python expression: 11 % 5?_**<br>
   _ans. 1_

6. **_Complete the body of the format_name function. This function receives the first_name and last_name parameters and then returns a properly formatted string._**<br>
   **_Specificaly:_**<br>
   **_If both the last_name and the first_name parameters are supplied, the funtion should return like so;_**

```Python
print(format_name("Ella", "Fitzgerald"))
Name: Fitzgerald, Ella
```

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

_ans._

```Python
def format_name(first_name, last_name):
    string = "Name: " + first_name + ", " + last_name
    if first_name == "":
        return "Name: " + last_name
    elif last_name == "":
        return "Name: " + first_name
    elif first_name == "" and last_name == "":
        return ""
    else:
        return string


print(format_name("Ernest", "Hemingway"))
print(format_name("", "Madonna"))
print(format_name("Voltaire", ""))
print(format_name("", ""))
```

7. **_The longest_word function is used to compare 3 words. It should return the word with the most number of characters (and the first in the list when they have the same length). Fill in the blank to make this happen._**

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

_ans._

```Python
      def longest_word(word1, word2, word3):
      	if len(word1) >= len(word2) and len(word1) >= len(word3):
      		word = word1
      	elif len(word2) >= len(word1) and len(word2) >= len(word3):
      		word = word2
      	else:
      		word = word3
      	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))
```

8. **_What's the output of this code?_**<br>

```Python
def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))
```

_ans 10_

9. **_What's the output of this Python expression: ((10 >= 5 * 2) and (10 <= 5 * 2))?_**<br>
   _ans. True_

10. **_The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1). Complete the body of the function so that it returns the right number.
    Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division._**

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

_ans._

```Python
def fractional_part(nume, deno):
    fraction = nume/deno - nume//deno
    if nume == deno:
        return 0
    elif nume == 0:
        return 0
    elif deno == 0:
        return 0
    elif nume != deno:
        return fraction



print(fractional_part(5, 5))
print(fractional_part(5, 4))
print(fractional_part(5, 3))
print(fractional_part(5, 2))
#print(fractional_part(5, 0))
print(fractional_part(0, 5))
```

# Week 3; Loops

## While Loops

1. **_What are while loops?_**<br>
   _ans. While loops let the computer execute a set of instructions while a condition is true._

2. **_Fill in the blanks to make the print_prime_factors function print all the prime factors of a number. A prime factor is a number that is prime and divides another without a remainder._**

```Python
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = ___
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == ___:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      ___
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT
```

_ans._

```Python
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT
```

3. **_The following code can lead to an infinite loop. Fix the code so that it can finish successfully for all numbers. Note: Try running your function with the number 0 as the input, and see what you get!_**

```Python
def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False


print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False
```

_ans._

```Python
def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0 and n != 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False


print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False
```

4. **_Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. A divisor is a number that divides into another without a remainder._**

```Python
def sum_divisors(n):
  sum = 0
  # Return the sum of all divisors of n, not including n
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
```

_ans._

```Python
def sum_divisors(n):
  x = 1
  sum = 0
  # Return the sum of all divisors of n, not including n
  while x < n:
    if n % x == 0:
      sum += x
      x += 1
    else:
        x += 1
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
```

5. **_The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5. An additional requirement is that the result is not to exceed 25, which is done with the break statement. Fill in the blanks to complete the function to satisfy these conditions._**

```Python
def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = ___
		# What is the additional condition to exit out of the loop?
		if ___ :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		___ += 1

multiplication_table(3)
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5)
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)
# Should print: 8x1=8 8x2=16 8x3=24
```

_ans._

```Python
def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = number * multiplier
		# What is the additional condition to exit out of the loop?
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3)
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5)
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)
# Should print: 8x1=8 8x2=16 8x3=24
```

## For Loops

1. ***How are while loops and for loops different in Python?***<br>
*ans. While loops iterate while a condition is true, for loops iterate through a sequence of elements.*

2. ___Fill in the blanks to make the factorial function return the factorial of n. Then, print the first 10 factorials (from 0 to 9) with the corresponding number. Remember that the factorial of a number is defined as the product of an integer and all integers before it. For example, the factorial of five (5!) is equal to 1 * 2 * 3 * 4 *5=120. Also recall that the factorial of zero (0!) is equal to 1.___
```Python
def factorial(n):
    result = 1
    for x in range(1,___):
        result = ___ * ___
    return ___

for n in range(___,___):
    print(n, factorial(n+___))
```
*ans.*
```Python
def factorial(n):
    result = 1
    for x in range(1, n):
        result *= x
    return result
for n in range(1, 10):
    print(n, factorial(n+1))
```

3. ___Write a script that prints the first 10 cube numbers (X ** 3), starting with x=1 and ending with x=10.___
```Python
for x in range(1,11):
  print(x**3)
```

4. ***Write a script that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7.***
```Python
for m in range(101):
    if m % 7 == 0:
        print(m)
```

5. ***The retry function tries to execute an operation that might fail, it retries the operation for a number of attempts.  Currently the code will keep executing the function even if it succeeds. Fill in the blank so the code stops trying after the operation succeeded.***
```Python
def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
    ___
    else:
      print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)
```
*ans.*
```Python
def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)
```














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
