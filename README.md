***Week 4: Strings, Lists and Dictionaries***<br>
<br>

1. [Strings](#strings)
1. [Lists](#lists)

# Strings

1. [What is a String?](#what-is-a-string)
1. [The Parts of a String](#the-parts-of-a-string)
1. [String Indexing and Slicing: Recap](#string-indexing-and-slicing-recap)
1. [Creating New Strings](#creating-new-strings)
1. [Basic String Methods](#basic-string-methods-recap)
1. [More String Methods](#more-string-methods)
1. [Formatting Strings](#formatting-strings)
1. [Formatting Strings: Recap](#formatting-strings-recap)
1. [String Reference Cheat Sheet](#string-reference-cheat-sheet)
1. [Formatting Expressions Cheat Sheet](#formatting-expressions-cheat-sheet)
1. [Practice Quiz](#practice-quiz-strings)

### What is a String?

- *By now, we've used strings in a lot of examples, but we haven't spent time in the nitty-gritty though.*

- *A string is a data type in Python that's used to represent a piece of text. It's written between quotes, either double quotes(" ") or single quotes(' ').*

- *But mixing up double quotes and single quotes will return a <code>SyntaxError</code>, telling us it couldn't find the end of the string. Like this;*
```Python
>>> var = "Green'
  File "<stdin>", line 1
    var = "Green'
          ^
SyntaxError: unterminated string literal (detected at line 1)
>>>
```

- *A string can also be as short as zero characters, called an empty string.*

- *We've also learned building longer strings with two or more short strings using <code>+</code> operator , this action is called concatenating.*
```Python
>>> name = "Sasha"
>>> color = "green"
>>>
>>> print("Name: " + name + " and " + " favourite color: " + color)
Name: Sasha and  favourite color: green
```

- *A string can also be lengthened by multiplying integers, like this;*
```Python
>>> "example" * 3
'exampleexampleexample'
```

- *To know the length of string, <code>len()</code> function is used, as we've already used. The <code>len()</code> function tells us the number of characters or letters contained in the string.*
```Python
>>> print(len("Committee"))
9
>>>
```

- *We can use strings to represent a lot of different things. They can hold a username, the name of a machine, an email address, the name of a file, and any other text.*

### The Parts of a String

- *For example, we've a text that is too long to display and we want to show just a portion of it. Or if we want to make an acronym by taking the first letter of each word in a phrase . We can do that through an operation called <code>string indexing</code>. This operation lets us access the character in a given position or index using square brackets and the number of the position we want. Bust Python starts counting indexes from 0 not 1, just like it does with the range() function. Like this;*
```Python
>>> name = "Kaylin"
>>> print(name[1])
a
>>> print(name[0])
K
```

- *So what will be the last index of a string? As indexing starts with 0 for the first index of the given string, it's pretty clear that the index last will be one less than the length of the string. In the given example, the length of the string <code>name = "Kaylin"</code> is 6, so index 5 will be the last for character "n" and if we try to access a string that doesn't exist, it will given an <code>IndexError</code>, called <code>string index out of range</code>. Like this;*
```Python
>>> print(name[5])
n
>>> print(name[6])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

- *But what if a string is really longer and we want know its last string. In this situation, we need not to count each character one by one, instead we can define using negative indexing. Using negative indexing, we can access the characters from last of a given string. Lets clear out with this example;*
```Python
>>> string = "She is Ellen and she loves to play badminton"
>>> print(string[-1])
n
```

- *As we can access indexes in a string, we can also access slice. A <code>slice</code> is the portion of a string that can contain more than one character; also sometimes called a <code>substring</code>. This can done by using a range and a colon as separator;*
```Python
>>> color = "Orange"
>>> print(color[1:4])
ran
```
- *The slice above took indexes from 1 to 4. We can even define slices without defining one of the two indexes. Like the following;*
```Python
>>> fruit = "Pineapple"
>>> fruit[:4]
'Pine'
>>> fruit[4:]
'apple'
>>>
```

### String Indexing and Slicing: Recap

- *String indexing allows you to access individual characters in a string. You can do this by using square brackets and the location, or index, of the target character. It's important to remember that Python starts indexes at 0. So to access the first character in a string, you would use the index [0].*

- *If you try to access an index that's larger than the length of your string, you'll get an __IndexError__. This is because you're trying to access something that doesn't exist!*

- *You can also access indexes from the end of the string going towards the start of the string by using negative values. The index[-1] would access the last character of the string, and the index[-2] would access the second-to-last character.*

- *You can also access a portion of a string, called a slice or a substring. This allows you to access multiple characters of a string. You can do this by creating a range, using a colon as a separator between the start and end of the range, in the form [x:y]. This range is similar to the range function we saw previously. It includes the first number, but goes to one less than the last number. For example:*
```Python
>>> fruit = "Mangosteen"
>>> fruit[1:4]
'ang'
```

- *The slice includes the character at index 1, and excludes the character at index 4. You can also easily reference a substring at the start or end of the string by only specifying one end of the range. For example, only giving end of the range:*
```Python
>>> fruit[:5]
'Mango'
```

- *This gave us the characters from the start of the string through index 4, excluding index 5. On the other hand this example gives is the characters including index 5, through the end of the string:*
```Python
>>> fruit[5:]
'steen'
```

- *You might have noticed that if you put both of those results together, you get the original string back!*
```Python
>>> fruit[:5] + fruit[5:]
'Mangosteen'
```

### Creating New Strings

- *Imagine you've a string with a character that's wrong and you want to fix it, like the following. You might try to fix that character by accessing it to give a new value. Lets see how it works:*
```Python
>>> message = "A kong string with a silly typo"
>>> message[2] = "l"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

- *Oops! a <code>TypeError</code>, the current error states that strings in Python are immutable i.e. can not be modified. Or we can say that we can't fix characters in a string by assigning new values to the certain characters. Instead we've to create new string based on the old string. Like this:*
```Python
>>> new_message = message[:2] + "l" + message [3:]
>>> print(new_message)
A long string with a silly typo
```

- *We fixed the typo, using string indexing and slicing. But it doesn't mean that we can not assign the same variable. We can, but it will lose the old value. We can always give a new value to a variable, like this:*
```Python
>>> message = "This is a new string"
>>> print(message)
This is a new string
>>>
>>> message = "Giving a new value with same variable"
>>>
>>> print(message)
Giving a new value with same variable
```

- *But what if we had a longer string with a typo and we didn't know which character to change. Well we can know the position of a certain character using a method called <code>.index</code>. __Method__ is a function associated with a specific <code>class</code>. The current method is applied to a variable. Check out the the following:*
```Python
>>> pets = "Cats, Dogs & Cows"
>>> pets.index("&")
11
```

- *So the index method calculates the position a characters and substrings. This method will give only one value if there more than one same substrings, considering the first one that matches, like this:*
```Python
>>> pets = "Cats, Dogs & Cows"
>>> pets.index("&")
11
>>> pets.index("Dog")
6
>>> pets.index("s")
3
```

- *If we try to find a substring that isn't there, we'll get a <code>ValueError</code> saying __substring not found__. This is obvious. So we can check whether a substring is contained by the string using the keyword <code>in</code>, followed by the variable. Check the following:*
```Python
>>> pets = "Cats, Dogs & Cows"
>>>
>>> "Cats" in pets
True
>>> "&" in pets
True
>>> "s" in pets
True
>>> "x" in pets
False
>>> "Fox" in pets
False
```

- *This will give a Boolean value i.e. True or False depending on whether the substring really exists in the given string in the given variable. It'll be True if the substring is a part of the string, and False if it isn't a part of the string.*

### Basic String Methods: Recap

- *In Python, strings are immutable, it means that they can't be modified. So if we want to fix a typo in a string, we can not simply modify the wrong character. We've to create a new string with that typo corrected. We can also assign a new value to the variable holding our string.*

- *To locate the index of a typo or any other substring, method __.index()__ is used. Like the following:*
```Python
>>> animals = "lions, tigers and bears"
```
*We can locate the index that contains the letter "g" using animals.index("g"):*
```Python
>>> animals.index("g")
9
```

- *If we try to locate a substring that doesn't exist in our string, we'll receive a __ValueError__ explaining that substring was not found.*

- *We can avoid a __ValueError__ by first checking whether the substring exists in the given substring. This can be done by making a conditional using __in__ keyword. It will be either __True__ or __False__. Using the previous __animals__ variable, check the following example:*
```Python
>>> "horses" in animals
False
>>> "bears" in animals
True
```

### More String Methods

- *On top of all this string processing power, the class __string__ provides a bunch of other __methods__ for working with texts. Now, we'll use some of these.*

- *The method __.upper()__ transforms the string text to uppercase while the methods __.lower()__ formats to lower.*
```Python
>>> "Mountains".upper()
'MOUNTAINS'
>>>
>>> "MOUNTAINS".lower()
'mountains'
```
*These methods are really useful while handling user input problems, like this:*
```Python
>>> answer = "YES"
>>> if answer.lower() == "yes":
...     print("User said yes")
...
User said yes
```

- *There's another method called __.strip()__. It is useful to get rid of white spaces, it also removes tabs and new-line characters that we usually don't want in our string:*
```Python
>>> "Henlo       ".strip()
'Henlo'
```
*There are two versions of this method as __lstrip__ and __rstrip__, to remove white spaces just to the left or right of the given string respectively:*
```Python
>>> message = "    How you doing?     "
>>>
>>> message.lstrip()
'How you doing?     '
>>>
>>> message.rstrip()
'    How you doing?'
```

- *The method __.count()__ is used to count how many times a substring occurs within the string:*
```Python
>>> "The number of times e occurs in this string".count("e")
4
```

- *The method __.endswith()__ returns if our string ends with a certain substring:*
```Python
>>> name = "Forest"
>>>
>>> name.endswith("est")
True
>>> name.endswith("x")
False
```

- *The method __.isnumeric()__ returns whether the given string is made up of integers:*
```Python
>>> "Forest".isnumeric()
False
>>> "365".isnumeric()
True
```

- *The method __.join()__ can also be used for concatenating of strings. To use this method, we need to call it on the string that will be used for joining the list of strings. Lets understand with the following samples:*
```Python
>>> " ".join(["She", "was", "there", "in",  "the", "party", "last", "night."])
'She was there in the party last night.'
>>>
>>>
>>> "...".join(["She", "was", "there", "in",  "the", "party", "last", "night."])
'She...was...there...in...the...party...last...night.'
```

- *We can also split a longer string into a list of strings:*
```Python
>>> "So this is another banger".split()
['So', 'this', 'is', 'another', 'banger']
```

### Formatting Strings

- *Up to now, we've been making longer strings using plus sign, str() function, commas, and we call it concatenating. This works, but it's not the ideal. There's a better way to do this using the __format__ method.*

- *Lets see a couple of examples:*
```Python

>>> name = "Montana"
>>> number = len(name)*3
>>>
>>> print("Hello {}, your lucky number is {}".format(name, number))
Hello Montana, your lucky number is 21
```
*First off, we defined two variables called __name__ and __number__, we could also have printed the string using concatenating but we used the __format__ method. Here we've used two __curly brackets {}__ as __place holders__ , for the two variables we first assigned, to show where the variables should be written. We then passed our variables as __parameters__ in the format method.*

- *But one thing to notice here is the variable __name__ is a string while __number__ is an integer, still the format method manages itself in automatic conversions of data types. Remember, in concatenating we had to convert the integer into a string using __str()__ function. Pretty neat right?*

- *The curly brackets __{}__ as place holders aren't always empty. We can use certain expressions inside them. Variables can also be used to re-write our code. Lets define our earlier example in a slightly different way:*
```Python
>>> print("Hello {name}, your lucky number is {number}".format(name="Montana", number=len(name)*3))
Hello Montana, your lucky number is 21
```

- *Checkout a different example:*
```Python
>>> price = 7.5
# tax rate is 9%
>>> tax_rate = 9/100
# calculate new price after applying the tax
>>> with_tax = price + price*tax_rate
>>>
>>> print(price, with_tax)
7.5 8.175
```
*Say we want to output the prices of an item with and without the tax. If the item costs __$7.5__ without any tax, and the tax rate is 9%, then the calculated price of the item with tax is __$8.175__. But want to print the prices with only two decimals after the decimal dot. Here we've to use certain expressions with format method, like this:*
```Python
>>> price = 7.5
>>> tax_rate = 9/100
>>> with_tax = price + price*tax_rate
>>>
>>> print(price, with_tax)
7.5 8.175
>>>
>>> print("Base price is: ${:.2f}, and price with tax is: ${:.2f}".format(price, with_tax))
Base price is: $7.50, and price with tax is: $8.18
```
*Here we've written a formatting expression between the curly brackets, we started with a colon to sepate, then __2f__, which means two floats after the decimal dot.*

- *Look at this example:*
```Python
>>> def to_celsius(x):
...      return (x - 32)*5/9
...
>>> for x in range(0, 101, 10):
...     print("{:>3} F | {:>6.2f}".format(x, to_celsius(x)))
...
  0 F | -17.78
 10 F | -12.22
 20 F |  -6.67
 30 F |  -1.11
 40 F |   4.44
 50 F |  10.00
 60 F |  15.56
 70 F |  21.11
 80 F |  26.67
 90 F |  32.22
100 F |  37.78
>>>
```
*Here we're using the __>__ operator to align text to the right so the output is neatly aligned. In the first curly bracket's expression, we set the numbers to be aligned to the right for total of 3 white spaces. And in the second expression, it to be 6 white spaces to the right with two decimals.*

### Formatting Strings: Recap

- *You can use the format method on strings to concatenate and format in all sort of ways. To do this, we create strings containing curly brackets __{}__, as place holders, to be replaced by format parameters. Then we call format method using string.format() to pass the variables as __parameters__. These variables will then be used to replace the curly bracket place holders. This method automatically handles all conversions between any data types.*

- *If the curly brackets are left empty, they'll be placed with those variables in the order in which they're called. However, you can put the variable names inside them, then use the names in the parameters. This allows for more easily readable code.*

### String Reference Cheat Sheet
#### String Operations

- ***len(string)*** *- returns length of the string*

- ***for x in string*** *- iterates over each character in the string*

- ***substring in string*** *- checks whether the substring is in the given string*

- ***string[i]*** *- accesses the character at index __i__*

- ***string[i:j]*** *- access the substring starting at __i__ and ends at index __j-1__*

#### String Methods

- ***string.lower()*** *- returns in lower case characters*

- ***string,upper()*** *- returns in upeer case characters*

- ***string.strip()*** *- returns without white spaces from both ends*

- ***string.lstrip()*** *- retunrs without left white spaces*

- ***string.rstrip()*** *- returns without any right white space*

- ***string.count(substring)*** *- returns the number of times a substring occurs*

- ***string.isnumeric()*** *- checks if the string is only made up of integers*

- ***string.isalpha()*** *- checks if the string is only of alphabets*

- ***string.split()*** *- returns the list of substrings*

- ***string.replace()*** *- returns a new string where all occurences of old one have been replaced by the new*

> *For more string methods - [Documentation](https://docs.python.org/3/library/stdtypes.html#string-methods)*

### Formatting Expressions Cheat Sheet

- **{:.2f}** *- returns with two decimals*
```Python
>>> "{:.2f}".format(19.8887)
'19.89'
```

- ***{:.2s}** *- returns first two characters*
```Python
>>> "{:.2s}".format("Python")
'Py'
```
> *For more Formatting Expressions - [Documentation](https://docs.python.org/3/library/string.html#format-specification-mini-language)*

### Practice Quiz: Strings

1. ***The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization. Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.***
```Python
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for ___:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if ___:
			new_string = ___
			reverse_string = ___
	# Compare the strings
	if ___:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
```

2. ***Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km", with Y having only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".***
```Python
def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {___} km".___
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
```

3. ***If we have a string variable named Weather = "Rainfall", which of the following will print the substring or all characters before the "f"?***

4. ***Fill in the gaps in the nametag function so that it uses the format method to return first_name and the first initial of last_name followed by a period. For example, nametag("Jane", "Smith") should return "Jane S."***
```Python
def nametag(first_name, last_name):
	return("___.".format(___))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 
```

5. ***The replace_ending function replaces the old string in a sentence with the new string, but only if the sentence ends with the old string. If there is more than one occurrence of the old string in the sentence, only the one at the end is replaced, not all of them. For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc. The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made).***
```Python
def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	if ___:
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = ___
		new_sentence = ___
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"
```

# Lists

1. [What is a List?](#what-is-a-list)
1. [Lists Defined: Recap](#lists-defined-recap)
1. [Modifying the Contents of a List](#modifying-the-contents-of-a-list)
1. [Modifying Lists](#modifying-lists)
1. [Lists and Tuples](#lists-and-tuples)
1. [Tuples](#tuples)
1. [Iterating over Lists and Tuples](#iterating-over-lists-and-tuples)
1. [Iterating over Lists using Enumerate](#iterating-over-lists-using-enumerate)
1. [List Comprehensions](#list-comprehensions)
1. [List Comp. : Recap](#list-comprehensions-recap)
1. [Lists and Tuples Operations Cheat Sheet](#lists-and-tuples-operations-cheat-sheet)
1. [Practice Quiz](#practice-quiz-lists)

### What is a List?

- *So far, we've seen a lot of ready-to-use data types such as __integers__, __strings__, __Boolean__, __floats__ in detail.*

- *Eventually you want to write the code that manipulates collections of items like a list of strings or a list of integers. This is where the __list__ data type comes in handy.*

- *In Python, we use square brackets __[ ]__ to indicate where a list starts and ends. Lets checkout an example:*
```Python
>>> x = ["Now", "we", "are", "cooking!"]
>>> print(x)
['Now', 'we', 'are', 'cooking!']
>>>
>>> type(x)
<class 'list'>
>>>
```
*Here we've assigned a variable __x__ with the value as a list of strings.*

- *Like in strings, we use __len()__ function to find out how many elements the given list has:*
```Python
>>> len(x)
4
```

- *When calling __len()__ for a list, it does not matter how long each string is on its own, what matters is how many elements it contains. To check whether a certain element in there in the list, the keyword __in__ is used:*
```Python
>>> "Now" in x
True
>>> "Then" in x
False
>>> "cooking!" in x
True
>>> "Hello!" in x
False
```

- *We can also use indexing to access individual elements depending on their position in the list. To do that, we use the square brackets __[ ]__ and the index we want to access, exactly like we did with strings.*
```Python
>>> print(x[0])
Now
>>> print(x[3])
cooking!
>>> print(x[4])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

- *We can also use the indexes to create a slice of the list. You guessed, right? Exactly like we did slicing in strings.*
```Python
>>> print(x[1:3])
['we', 'are']
```

- *If all this sounds really familiar to what we said about strings, then this lesson is working as intended. That's because, __strings__ and __lists__ are very similar data types and are both examples of __sequences__ in Python.*

- *They both share a bunch of operations like iterating over them using for loops, indexing, slicing, len(), concatenating using plus operator, to verify if a certain element is there using the keyword "in".*
```Python
>>> for y in x:
...     print(y)
...
Now
we
are
cooking!
```

### Lists Defined: Recap

- *Lists in Python are defined using square brackets __[ ]__, with elements stored inside it by commas __,__:*
```Python
>>> a = ["This", "is", "a", "rainbow"]
>>>
>>> b = [3,7, 11, 5, 13]
>>>
>>> type(a)
<class 'list'>
>>> type(b)
<class 'list'>
```

- *The __len()__ function is used to return the number of elements a list contains:*
```Python
>>> len(a)
4
>>> len(b)
5
```

- *We can also use the keyword __in__ to check if a specific element occurs in the list and return a __Boolean__ value: __True__ or __False__.*

- *Similar to strings, lists can also use indexing to access certain elements in a list based on their position:*

- *In Python, lists and strings are both examples of sequences of data. And these sequences have some similar properties: __i)__ being able to iterate over using __for-loops__ ; __ii)__ support indexing and slicing; __iii)__ using Len to measure the length of the sequence; __iv)__ using __+__ operator in order to concatenate; __v)__ using __in__, to check if a specific element or substring is there.*

### Modifying the Contents of a List

- *One of the differences between lists and strings is that lists are __mutable__, and strings aren't. This means we can __add__, __remove__, or __modify__ elements in a list.*

- *We'll start with the simplest chnage: adding elements to a given list using __append__ method. Check this out:*
```Python
>>> fruits = ["Pineapple", "Mango", "Banana", "Apple"]
>>>
>>> fruits.append("Kiwi")
>>> print(fruits)
['Pineapple', 'Mango', 'Banana', 'Apple', 'Kiwi']
```
*The __append__ method adds new elements at the end of the list, it does not matter how long the list is. Even you could start an empty list, then add elements using __append__.*

- *But to add an element in a specific position instead of at the end of the list, the __insert__ method is used:*
```Python
>>> fruits.insert(2, "Orange")
>>> print(fruits)
['Pineapple', 'Mango', 'Orange', 'Banana', 'Apple', 'Kiwi']
```

- *The __insert__ method takes an __index__ as first parameter and a new element as second parameter. It adds that element at the given index position in our list.*

- *In lists, even if we use an index that exceeds its length as first parameter using __insert__ method, there will be no error. Instead the element will be added at the end of list:*
```Python
>>> fruits.insert(25, "Peach")
>>> print(fruits)
['Pineapple', 'Mango', 'Orange', 'Banana', 'Apple', 'Kiwi', 'Peach']
```

- *Like that we use __remove__ method to remove an element from our list:*
```Python
# Let's remove "Banana"
>>> fruits.remove("Banana")
>>> print(fruits)
['Pineapple', 'Mango', 'Orange', 'Apple', 'Kiwi', 'Peach']
```

- *But what happens when we try to remove a element that isn't there in the list:*
```Python
>>> fruits.remove("Pear")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```
*Oops! got a __ValueError__, telling us the element doesn't exist in the list.*

- *Another way we can remove elements is by using __pop__ method, which receives indexes:*
```Python
>>> fruits.pop(1)
'Mango'
>>> print(fruits)
['Pineapple', 'Orange', 'Apple', 'Kiwi', 'Peach']
```
*The __pop__ method returns the element that was removed at the index that was passed.*

- *In the last way to modify the contents of a list is to change an item by assigning something else at that position:*
```Python
>>> fruits[3] = "Strawberry"
>>> print(fruits)
['Pineapple', 'Orange', 'Apple', 'Strawberry', 'Peach']
# "Kiwi" got replaced by "Strawberry"
```

### Modifying Lists

- *While lists and strings are both sequences, a big difference between them is that lists are __mutable__, unlike strings. You can add, remove, or modify elements in a list.*

- *New elements can be added to the end of a list using the __append__ method. You can call this method on a list using __dot notation (.)__ and pass in the element to be added as a parameter.*
```Python
>>> languages = ["Python", "JavaScript", "Java", "C++", "SQL", "PHP"]
>>> languages.append("C#")
>>>
>>> print(languages)
['Python', 'JavaScript', 'Java', 'C++', 'SQL', 'PHP', 'C#']
```

- *If you want to add an element to a list in a specific position, you can use the method __insert__. This method takes __two__ parameters: the first specifies the index in the list, and the second in the element to be added at that index. If you specifies an index that's larger than length of the list, the element will simply be added to end of the list.*
```Python
>>> languages.insert(3, "Rust")
>>> print(languages)
['Python', 'JavaScript', 'Java', 'Rust', 'C++', 'SQL', 'PHP', 'C#']
>>>
>>> languages.insert(9832176676376, 'Bootstrap')
>>> print(languages)
['Python', 'JavaScript', 'Java', 'Rust', 'C++', 'SQL', 'PHP', 'C#', 'Bootstrap']
```

- *Elements can be removed from a list using the __remove__ method. If the elememt isn't found in the list, you will get a __ValueError__ explaining that the element was not found in the list.*
```Python
>>> languages.remove('JavaScript')
>>> print(languages)
['Python', 'Java', 'Rust', 'C++', 'SQL', 'PHP', 'C#', 'Bootstrap']
>>>
>>> languages.remove('Kotlin')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```

- *You can also remove elements from a list using the __pop__ method. This method differs from the __remove__ method in that it takes an index as a parameter, and returns the element that was removed. This can be useful if you don't know whhat the value of the element is, but you know where it's located.*
```Python
>>> languages.pop(6)
'C#'
>>> print(languages)
['Python', 'Java', 'Rust', 'C++', 'SQL', 'PHP', 'Bootstrap']
```

- *Finally, you can change an element in a list using indexing to overwrite the value stored at the specified index.*
```Python
>>> languages[2] = 'XML'
>>> print(languages)
['Python', 'Java', 'XML', 'C++', 'SQL', 'PHP', 'Bootstrap']
```

### Lists and Tuples

- *As we called out before, there are a number of data types in Python that are all sequences.*<br>

***Strings:*** *Strings are sequences of characters, and are __immutable__.*<br>
***Lists:*** *Lists are sequences of elements of any type, and are __mutable__.*

- *There'a a third data type that is also a sequence and closely related to lists called __tuples__. ___Tuples:___ Tuples are sequences of elements of any type, and are **immutable**. Tuples are written parentheses **( )** instead of square brackets **[ ]**. For example:*
```Python
>>> full_name = ('Grace', 'M', 'Hopper')
>>> type(full_name)
<class 'tuple'>
```

- *We've the list data type then why tuples? There are cases when we want to make sure an element in a certain position or index and will not change. In these situations, lists won't help us. In other words, when using tuples, the position of elements inside them have meaning.*

- *Tuples are used for a lot of different things in Python. One common example is the return values of a function. When a function returns more than one values. it's actually returning a tuple. Remember the function to convert seconds to hours, mitutes and seconds that we saw a while back:*
```Python
>>> def convert_seconds(seconds):
...     hours = seconds//3600
...     minutes = (seconds - hours*3600)//60
...     remaining_seconds = seconds - hours*3600 - minutes*60
...     return hours, minutes, remaining_seconds
...
>>> result = convert_seconds(700)
>>> print(result)
(0, 11, 40)
>>> type(result)
<class 'tuple'>
```
*This function return three values or we can say, it returns a tuple of three elements.*

### Tuples

- *Tuples are like lists, since they are exaples of sequences and can contain elements of any type. But unlike lists, tuples are immutable. They are specified using parentheses instead of square brackets.*

- *Tuples can be useful when we need to ensure that an element is in a certain position and won't change.*

- *Since lists are mutable, the order of elements can be changed on us. Since the order of elements in a tuple can not be changed, the position of elements can have meaning.*

### Iterating over Lists and Tuples

- *When we looked at __for__ loops, we found that they iterate over a sequence of elements. For example iterating over a list:*
```python
>>> animals = ['Lion', 'Zebra', 'Dolphin', 'Monkey']
>>> chars = 0
>>> for animal in animals:
...     chars += len(animal)
...
>>> print("Total character: {}, Average length: {}".format(chars, chars/len(animals)))
Total character: 22, Average length: 5.5
```
*In this script, we're iterating over a list called __animals__. For each of the elements, we find its length and add it to the total amount of characters. At the end, we print the total characters and the average length which is the characters divided by the legth of list. We're using the len() twice here, once to take length of each string then for total length of the given list.*

- *We can use the range() function and use the indexing to access the elements or we can just use the <code>enumerate</code> function. For example:*
```Python
>>> winners = ['Ashley', 'Dylan', 'Reese']
>>> for index, person in enumerate(winners):
...     print("{} - {}".format(index + 1, person))
...
1 - Ashley
2 - Dylan
3 - Reese
```

- *The <code>enumerate()</code> function returns a tuple for each element in the list. The first value in the tuple is the index of the element in the sequence, second value in the tuple is the element in the sequence, and so on.*

- *Let's use all of this now to solve a slightly more interesting problem. Say we've a list of tuples containing two elements each. The first string is an __email address__ and the second is the __full name__ of the person associated with that email. And you want to write a function that creates a new list containing one string per person including their name then email address between angled brackets, like this:*
```Bash
My Name <me@example.com>
```
*We'll define a function that receives a list of people,*
```Python
>>> def full_emails(people):
...     value = []
...     for email, name in people:
...         value.append("{} <{}>".format(name, email))
...     return value
...
>>> print(full_emails([('alex75@outlook.com', 'Alex Diego'),
...       ('shay@gmail.com', 'Shay Brandt')]))
['Alex Diego <alex75@outlook.com>', 'Shay Brandt <shay@gmail.com>']
```
*Yes, this worked as expected.*

### Iterating over Lists Using Enumerate

- *










### List Comprehensions

### List Comprehensions: Recap

### Lists and Tuples Operations Cheat Sheet

### Practice Quiz: Lists
