***Week 4: Strings, Lists and Dictionaries***<br>
<br>

1. [Strings](#strings)

# Strings

1. [What is a String?](#what-is-a-string)
1. [The Parts of a String](#the-parts-of-a-string)
1. [String Indexing and Slicing: Recap](#string-indexing-and-slicing-recap)
1. [Creating New Strings](#creating-new-strings)
1. [Basic String Methods](#basic-string-methods-recap)
1. [More String Methods](#more-string-methods)

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