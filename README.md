***Week 3; Loops***
1. [While Loops](#while-loops)
1. [For Loops](#for-loops)

# While Loops
1. [Introduction to Loops](#introduction-to-loops)
1. [What's a while loop?](#what-is-a-while-loop)
1. [Anatomy of a while loop](#anatomy-of-a-while-loop)
1. [Why Initializing Variables Matters](#why-initializing-variables-matters)
1. [Infinite Loops and How to Break Them](#infinite-loops-and-how-to-break-them)
1. [Practice Quiz](#practice-quiz-while-loops)

### Introduction to Loops

- *In this module we'll learn how to get computers to do repetitive tasks, which is another cornerstone of programming. As we've called out before computers are great at repeating the same task over and over. They never get bored or make a mistake. You could ask a computer to do the same calculation a thousand times in the first result would be just as accurate as the last, which isn't something we can say about us humans.*

- *Have you ever tried to do something at thousand times in a row, it be enough to drive you loopy, which is why in this course, we're going to learn how to leave the loops up to the computer.*

- *In this module, we'll explore three techniques for automating repetitive tasks. These are while loops, for loops, and recursion.*

### What is a while loop?

- *First off, we'are going to talk about <code>while loops</code>. While loops work in a similar way to branching <code>if</code> statements. The only different is that the body of the block can be executed multiple times instead of just once.*

- *Check out the following;*
```Python
>>>
>>> x = 0
>>>
>>> while x < 5:
...       print("Not there yet, x = " + str(x))
...       x = x + 1
...
Not there yet, x = 0
Not there yet, x = 1
Not there yet, x = 2
Not there yet, x = 3
Not there yet, x = 4
>>> print("x = " + str(x))
x = 5
```

- *In the first line we're assigning the variable "x". We call this action <code>initializing</code>, to give an initial value to the variable.*

- *After that line we'are beginning a while loop using <code>while</code> keyword, followed by the condition that x needs to be smaller than 5. As we've initialized the variable as x = 0, the condition is currently <code>True</code>*

- *In the next two lines we've the body of the block that is intended to the right. This is the body of the while loop. In the second line of loop's body, we increment the value of x by 1 and assigning this value back to x.*

- *Because this is a loop, the computer doesn't just continue executing with the next line in the script. Instead, it loops back around to re-evaluate the condition for the while loop. And because 1 here is still smaller than 5, it executes the body of the loop again. It then prints the message and once more increments x by 1. So the x is now 2. The computer will keep doing this until the condition isn't true anymore.*

### Anatomy of a While Loop

- *A <code>while</code> loop will continuously execute code depending on the value of a condition. It begins with the keyword <code>while</code>, followed by a comparison to be evaluated, then a <code>colon</code>. On the next line is the code block to be executed, indented to the right. Similar to an <code>if</code> statement, the code in the body will only be executed if the comparison is evaluated to be <code>true</code>. What sets a while loop apart, however, is that this code block will keep executing as long as the evaluation statement is true. Once the statement is no longer true, the loop exits and the next line of code will be executed.*

### More While Loop Examples

- *We looked at a basic syntax of the loop and how it works. Let's now apply this knowledge to a similar example, but this time with a while loop inside a function.*
```Python
>>> def attempts(n):
...     x = 0
...     while x <= n:
...           print("Attempts " + str(x))
...           x += 1
...     print("Done.")
...
>>> attempts(2)
Attempts 0
Attempts 1
Attempts 2
Done.
>>> attempts(7)
Attempts 0
Attempts 1
Attempts 2
Attempts 3
Attempts 4
Attempts 5
Attempts 6
Attempts 7
Done.
```

- *In this example, we've initialized a variable x to the value 0, followed by the while loop with condition x is smaller than or equal to the parameter. The loop's body contains the incremental x += 1 i.e. x = x + 1. So the loop's body's print function will be executed until x becomes greater than the parameter n.*

### Why Initializing Variables Matters

- *The most common mistake people make while writing a loop is forgetting to initialize the variable to a correct value which leads to a common <code>NameError</code> "variable is not defined". Check out the following example;*
```Python
>>> while a > 3:
...       print("Increasing by " + str(a))
...       a += 1
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
```

- ***You'll want to watch out for a common mistake: forgetting to initialize variables. If you try to use a variable without first initializing it, you'll run into a NameError. This is the Python interpreter catching the mistake and telling you that you’re using an undefined variable. The fix is pretty simple: initialize the variable by assigning the variable a value before you use it.***

- ***Another common mistake to watch out for that can be a little trickier to spot is forgetting to initialize variables with the correct value. If you use a variable earlier in your code and then reuse it later in a loop without first setting the value to something you want, your code may wind up doing something you didn't expect. Don't forget to check older variables and initialize new variables before using them!***

### Infinite Loops and How to Break Them

- *So far you may know that <code>while loops</code> use the condition to check when to exit. The loop's body needs to check the condition being checked will change. If it doesn't, the loop may never finish and an <code>infinite loop</code> is formed, __a loop that keeps executing and never stops__.*

- *Check out this example;*
```Python
def number(num):
    x = 2
    while num % x == 0:
        print("The remainder is " + str(num % x))


number(8)
```

- *This will keep executing and will end never as x = 2 devides every even integer with 0 remainder. But a programmer will never wish a program to spam infinitely, infinite loops may make your computer dizzy. To break the current loop, we can set a value of x so that the loop's body will stop checking whether it's true and stops there.*
```Python
def number(num):
    x = 2
    while num % x == 0:
        print("The remainder is " + str(num % x))
        x += 1


number(8)
```

### Practice Quiz; While Loops

1. ***What are while loops in Python?***

2. ***Fill in the blanks to make the print_prime_factors function print all the prime factors of a number. A prime factor is a number that is prime and divides another without a remainder.***
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

3. ***The following code can lead to an infinite loop. Fix the code so that it can finish successfully for all numbers.***

***Note: Try running your function with the number 0 as the input, and see what you get!***
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

4. ***Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. A divisor is a number that divides into another without a remainder.***
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

5. ***The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5. An additional requirement is that the result is not to exceed 25, which is done with the break statement. Fill in the blanks to complete the function to satisfy these conditions.***
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

# For Loops
1. [What is a For Loop?](#what-is-a-for-loop)
1. [Recap](#for-loops-recap)
1. [More for Loop Examples](#more-for-loop-examples)
1. [A Closer Look at the range() Function](#a-closer-look-at-the-range-function)
1. [Nested for Loops](#nested-for-loops)
1. [Commom Errors in for Loops](#common-errors-in-for-loops)
1. [Loops Cheat Sheet](#loops-cheat-sheet)
1. [Practice Quiz](#practice-quiz-for-loops)

### What is a For Loop?

- *A <code>for loop</code> iterates over a sequence of values. A very simple example of a <code>for loop</code> is to iterate over a sequence of numbers as follow:*
```Python
for x in range(5):
    print(x)
```

- *In for loops, we use the distinguishing keyword <code>for</code>, and between the <code>for</code> keyword and <code>in</code> keyword, we have the name of the variable <code>x</code>. This variable will take each of the values in the sequence that loop iterates through.*

- *So in this example, it'll iterate through a sequence of numbers generated using the <code>range()</code> function*

- *There are two different things that you should know about this <code>range</code> function. First, in Python and a lot of other programming language, a range of numbers will start with the value zero by default. Second, the list of numbers generated will be one less than the given value. That means the above for loop will iterate the values of numbers from 0 to 5.*
```Python
>>> for x in range(5):
...     print(x)
...
0
1
2
3
4
```

- *So there, we saw a very basic for loop. Here the variable x iterates at each element of the sequence. As the range function starts with the value of zero, so for the range of 5, it iterates the values from 0 to 4.*

- *We can use a for loop to iterate over a sequence of values of any type, not just a range of numbers. Such as list of strings:*
```Python
friends = ["Taylor", "Alex", "Mat", "Elie"]
for name in friends:
    print("Hi, " + name)
```

- *We'll talk a lot more about lists later on. But for now, you only need to know that we can construct lists using square brackets, and separate the elements in them with commas.*

- *The sequence that the for loop iterates over could contain any type of element, not just strings, numbers.*

- *For example;*
```Python
values = [23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print("Total sum: " + str(sum) + " - Average: " + str(int(sum/length)))
```

- *Here we're defining a list of values, after that we're initializing two variables, sum and lenght, that will update in the body of the for loop. In the for loop, we're iterating over each of the values in the list, adding the current value of the sum of values, and then also adding 1 to length, which calculates how many elements there are in the list. Once we've gone through the whole list, we print out the sum and the average.*

- *For loops are useful in various ways. For example, you might them to copy files to machines, process the contents of files, automatically install software, and a lot more.*

- *If you're wondering when to use <code>for</code> loops and when to use <code>while</code> loops, there's a way to tell. __Use <code>for</code> loops when there's a sequence of elements that you want to iterate.__ __Use <code>while</code> loops when you want to repeat an action until a condition changes.__*

### For Loops Recap

- *Similar to if statements and while loops, for loops begin with the keyword for with a colon at the end of the line. Just like in function definitions, while loops and if statements, the body of the for loop begins on the next line and is indented to the right. But what about the stuff in between the for keyword and the colon? In our example, we’re using the range() function to create a sequence of numbers that our for loop can iterate over. In this case, our variable x points to the current element in the sequence as the for loop iterates over the sequence of numbers. Keep in mind that in Python and many programming languages, a range of numbers will start at 0, and the list of numbers generated will be one less than the provided value. So range(5) will generate a sequence of numbers from 0 to 4, for a total of 5 numbers.*

- *Bringing this all together, the range(5) function will create a sequence of numbers from 0 to 4. Our for loop will iterate over this sequence of numbers, one at a time, making the numbers accessible via the variable x and the code within our loop body will execute for each iteration through the sequence. So for the first loop, x will contain 0, the next loop, 1, and so on until it reaches 4. Once the end of the sequence comes up, the loop will exit and the code will continue.*

- *The power of for loops comes from the fact that it can iterate over a sequence of any kind of data, not just a range of numbers. You can use for loops to iterate over a list of strings, such as usernames or lines in a file.*

- *Not sure whether to use a for loop or a while loop? Remember that a while loop is great for performing an action over and over until a condition has changed. A for loop works well when you want to iterate over a sequence of elements.*

### More for Loop Examples

- *We talked about the range function, how it generates a sequence of numbers starting with zero. Sometimes, though, we don't want to start with zero. For these situations, we can also specify the first element of the list to generate. For example;*
```Python
product = 1
for n in range(1, 10):
    product = product * n

print(product)
```

- *We've calculated the product of all numbers from 1 to 10, here it is important to start with 1 not 0, as multiplying zero would give the result as zero.*

### A Closer Look at the range() Function

- *Previously we had used the <code>range()</code> function by passing a single parameter, and it generated a sequence of numbers from 0 to one less than we specified. But the <code>range()</code> function can do much more than that.*

- *We can also pass in two parameters in it: the first specifying our starting point, the second specifying the end point. Such as <code>range(1, 10)</code>. Don't forget that the sequence generated will not contain the last element; it will stop one before the parameter specified.*

- *The <code>range()</code> function can take a third parameter, too. This third parameter lets you alter the size of each step. So instead of creating a sequence of numbers incremented by 1, you can generate a sequence of numbers that are incremented by the third parameter.*

- *__A Quick Recap of <code>range()</code> Function:__*
> - *One parameter will create a sequence, one-by-one, from zero to one less than the parameter.*
> - *Two parameters will create a sequence, one-by-one, from the first parameter to one less than the second parameter.*
> - *Three parameters will create a sequence, starting with the first parameter and stoping before the second parameter, but this time increasing each step by the third parameter.*

### Nested for Loops

- *So far we've seen loops such as while and for loops. But how about a loop inside a loo, called nested for loop.*
```Python
# the Dominoes game
>>> for left in range(7):
...    for right in range(left, 7):
...      print("[" + str(left) + "|" + str(right) + "]", end=" ")
...    print()
...
[0|0] [0|1] [0|2] [0|3] [0|4] [0|5] [0|6]
[1|1] [1|2] [1|3] [1|4] [1|5] [1|6]
[2|2] [2|3] [2|4] [2|5] [2|6]
[3|3] [3|4] [3|5] [3|6]
[4|4] [4|5] [4|6]
[5|5] [5|6]
[6|6]
```

- *In this code, there's a new parameter that we passed to the print function. This parameter is called <code>end</code>. Normally, once print has taken the content we passed and written it to the screen, then it writes a special character that creates a new line called newline character. If you want to print to write something else instead of the newline character, we use the end parameter, like we see in this example. Notice how the second for loop iterates over a different number of elements each time it's called as the value of left changes.*

### Common Errors in for Loops

- *We can not iterate integers in for loops;*
```Python
>>> for i in 34:
...    print(i)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
```

- *There is a TyeError called integers are not iterable. To solve it we can use range function or as a list which iterates only "34";*
```Python
# in range() function
>>> for i in range(0,25):
...    print(i)
...
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24


# in list
>>> list = ["34"]
>>> for i in list:
...   print(i)
...
34
```

- *Unlike integers, strings are iterable;*
```Python
>>> for x in "Taylor":
...    print(x)
...
T
a
y
l
o
r
>>>
```

- *But it seems quite not right to iterate strings like this when we want to iterate the string not its each letter characters, to fix it, use list format;*
```Python
>>> for x in ["Taylor"]:
...    print(x)
...
Taylor
```

### Loops Cheat Sheet

#### While Loops

- *We already know that, a while loop executes the body of the loop while the condition remains True. Its general syntax;*
```Python
while condition:
      body
```

- *Failure to initialize variables: Always make sure all the variables used in the loop's condition are initialized before the loop.*

- *Unintended Infinite Loops: Make sure the body of the loop modifies the variables used in the condition, so that the loop will eventually end __for all possible values of the variables.__*

- *While loops are mostly used when there's an unknown number of operations to be performed, and a condition needs to be checked at each iteration.*

#### For Loops

- *A for loop iterates over a sequence of elements, executing the body of the loop for each element in the sequence. Its general syntax;*
```Python
for variable in sequence:
    body
```    
***The range() Function:***
- *range() function iterates a sequence of integers, it can take one, two or three parameters:*
> - *__range(x):__ 0, 1, 2, 3, 4 ........... x-1*

> - *__range(x, y):__ x, x+1, x+2, x+3 ........... y-1*

> - *__range(x, y, z):__ x, x+z, x+2z, x+3z ........ y-1 (if it is a valid increment)*

***Common Pitfalls:***

- *The range() function never includes the __upper limit__, but one less than it.*

- *Integers are not iterable while strings are, letter by letter, but that might not be what you want. So use list format.*

- *For loops are mostly used when there is a pre-defined sequence or range of integers or strings (commonly elements) to iterate.*

***Break or Continue:***

- *You can break or interrupt both while and for loops using the <code>break</code> keyword. We normally do this to break a unintended infinite loop.*

- *You can the <code>continue</code> keyword to skip the current iteration and continue with the next one. This is typically used to jump ahead when some of the elements of the sequence are not relevant.*

### Practice Quiz; For Loops

1. ***How are while loops and for loops different in Python?***

2. ___Fill in the blanks to make the factorial function return the factorial of n. Then, print the first 10 factorials (from 0 to 9) with the corresponding number. Remember that the factorial of a number is defined as the product of an integer and all integers before it. For example, the factorial of five (5!) is equal to <code>1* 2* 3* 4* 5=120</code>. Also recall that the factorial of zero (0!) is equal to 1.___
```Python
def factorial(n):
    result = 1
    for x in range(1,___):
        result = ___ * ___
    return ___

for n in range(___,___):
    print(n, factorial(n+___))
```  

3. ___Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.___
```Python
for __ in range(__,__):
  print(__)
```

4. ***Write a script that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7.***

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