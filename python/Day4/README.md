# Day04 : Task in Python
# Strings in python:Part-1
1.String & Example
2.Formatted Strings
3.Escape Characters
4.String Operators

# Status:

Notes:
1.#Strings:A String is a sequence of character.In Python,string are enclosed within single(') or double(") or triple(""") quotation marks.

#Example:
1.print('Hello World')
2.print("Won't give up!")
3.print('''"Quotes" and 'single quotes' can be trick.''')
4.print("\"Quotes\" and 'single quotes' can be trick.")

# use type() to check data type.

# 2.Formatted Strings:
A formatted string in a python is a way to insert variables or expressions
inside a string.It allows you to format the output in a readable and controlled way.

# There are multiple ways to format string in python:
1.Old style formatting(% operator)
2.str.format() method
3.F-strings(formatted string literals)

# Formatted String - Operator %
#Old-style formating(% operator):
This approch use the % 

# Strings in python:Part-2
# 1.String indexing: Positive & Negative index
=>You can access individual characters in a string using their index.
Python uses zero-base indexing , meaning the first character has an index of 0
# index:Position of the characters
Example: name="SHIVAM"
                                 S   H   I   V   A   M
=>index (positive) :start=>      [0] [1] [2] [3] [4] [5]  
=>index (negative)               [-6] [-5] [-4] [-3] [-2] [-1]    <=Start

# 2.String Slicing:
=> Slicing in python is feature that enables accessing part of the squence.
=> String Slicing allows you to get subset of characters from a string using a
specified ranges of indices

# syntax: string[start : end : step]
1.start: the index to start slicing[inclusive]. Default value is 0.
2.end: the index to stop slicing[exclusive].Default value is length of string.
3.step: how much to increment the index after each character.Default value is 1.
Example:
name="Shivam"
print(name[0:2])#Sh is print
print(name[0:5:2])Sia

# String Method:
=> Method    :                   Description
1.len()    =>: Returns the length of a string(the numbers of characters).
2.upper()  =>: Converts a string into upper case.
3.lower()  =>: Converts a string into lower case.
4.strip()  =>: Removes any leading and trailing whitespace(including any spaces,tabs or newline characters)
5.count()  =>: Return the number of times a specified value occurs in a string
6.find()   =>: Search the string for a specified value and returns the position of where it was found
7.title()  =>: Convert the first character for each word to upper case
8.splite() =>: splite the string at the speicified separator,and returns a list
9.replace(old,new) =>: replace all occurrences of substring with a new substring

