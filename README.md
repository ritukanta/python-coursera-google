***Week 3; Loops***
1. [While Loops](#while-loops)

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