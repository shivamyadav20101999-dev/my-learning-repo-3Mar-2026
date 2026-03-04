#String in Python
#sting = character in single or double and triple quotes.
name="Shivam"
print(name)    #creating a string
#print("Hello Shivam")
print(type(name)) # checking data type

print('Hello World')

# interpeter confuse this case
#print('It's Easy')
print("It's Easy")

#======================================
print("key-word-double Quotes")
#print(""key-word-double Quotes"")
#1.Method
print('''"kw-double Quotes"''')
#2.Method
print("\"kw-double Quotes\"")

#======================================
#Formatted String
#1. Old style formatting - % operator
name="Shivam"
age=28
print("My name is %s and  I am %d years old."%(name,age))
# %s , %d are placeholders for string and int .
#==========================================================:
#2.Formatted String - str.format() method 
#str.format() method:
#In python 3 ,the format() method is more powerful and flexible than the 
#old-style % formatting 
#syntax:
#       "string {}".format(value)
#example:
name="Shivam"
age=28
print("My name is {} and I am {} years old.".format(name,age))
#You can also reference the variables by index and keyword.
print("My name is {0} and I am {1} years older.".format(name,age))
print("My name is {1} and I am {0} years older.".format(name,age))
print("My name is {name} and I am {age} years older.".format(name="Ram", age=28))
print("My name is {age} and I am {name} years older.".format(name="Ram", age=28))

#=============================================================
#3. Formatted String - F-strings(Python 3.6+)
#F-Strings(Formatted String Literals):
#In python 3.6 , F-strings are the most concise and efficient way to format
#strings. You prefix the string with an f or F,and variables are or expressions
#are embedded  directly within the curly braces{}.
#syntax:
#     f"string {variable}"
# Example:
name="Shivam yadav111-p"
age=27
print(f"My name is {name} and I'm {age} years old.")
#You can also perform experession inside placeholders 
print(f"In 5 years, I will be {age + 5} years olds.")
print(F"My name is {name} and I'm {age} years old.")

#Escape Characters 
# Escape character in Python are special characters used in strings to
#represent ,whitespace,symbols or control characters that would otherwise
#be difficult to include , an escape character is a backslash \ followed by
#the character you want to be insert.

#Example:
print('hello\nworld!') #for \n  new line
print("Hello\tworld!") #for \t tab space
print("\"Quotes\" and 'single quotes' can be used trickily")
print("\'single quotes\'")

#Sting Operators in Python.
a="Hello"
b="World"
print(a+b) #Concatenation
print(a*4) #Repetition

# [] -slice, [:] - range -- scroll below
a="Hello"

if "H" in a:
    print("Yes")
else:
    print("No")

if "H" not in a:
    print("yes")
else:
    print("no")


    # print("Hello\nWorld")
    print(r"Hello\nWorld") #raw string - it treats backslash as a literal character
    #raw string:suppress the escape character

    #practice
    print("\"kw-double Quotes\"");
    name="Yadav"
    # age=28
    # print("my name is %s and i am %d years old. " %(name,age))

    print("My name is {} and I am {} years old.".format(name,age))
    print("My name is {0} and I am {1} years olders." .format(name,age))
    print("My name is {name} and I am {age} years olders." .format(name="Shiva", age="Infinite"))

    #f-string
    name1="devi"
    age1=23
    print(f"Name is {name1} and age is {age1}")
    print(F"Name is {name1} and age is {age1}")

    #Escape characters
    print("\"kw-double Quotes\"")
    print('''"kw-double and single Quotes"''')

    print(" 'single quotes' ")

    print(" \'kw-sigle Quotes\' ")

    print("Hello\nWorld")
    print(r"Hello\nWorld")

    print("Hello\tworld")

    #String Operators
    a="abc"
    b="123"
    print(a+b)
    print(a*3)

    if "a" in a:
        print("Yess")
    else:
        print("Nooo")

if "a" not in b:
            print("Yesss")
else:print("Nooo")
    


