***Week 4: Strings, Lists and Dictionaries***<br>
<br>

1. [Strings](#strings)

# Strings

1. [What is a String?](#what-is-a-string)
1. [The Parts of a String](#the-parts-of-a-string)
1. [Creating New Strings](#creating-new-strings)

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

### Creating New Strings
