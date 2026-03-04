#String slicing:
#syntax: string_name[start:stop:step]
name="Shivam"
#012345
print(name[0:2]) #sh ,default step is 1
print(name[0:5:2])#sia ,step is 2
print(name[0:5:3])#sv ,step is 3
print(name[0:2])#first two characters
print(name[:3:])#first three characters
print(name[:4:])#first four characters
print(name[:5:])#first five charactersl
print(name[1:5])#second to fifth characters
print(name[4:6])#last two characters

print("==============================\n")
#negative indexing:
print(name[-1])#last character of string
print(name[-2])#second last character of string
print(name[-3])#third last character of string
print(name[0:5:2])#every second character from the str
print(name[0::2])#by default string length
print(name[:])#all characters of string
print(name[::])#all characters of string
#interview Question:
#reverse a string:
print(name[::-1])
print(name[0:2])#first two characters
print(name[0:3])#first 3 characters
print(name[2:5])#third to fifth characters
print(name[1:4])#seond to fourth characters
print(name[-1])#last character of string
print(name[5])#last character of string
#name = shivam 012345:
print(name[-2])#last two character of string
print(name[-3])#last three character of string
#shivam=>012345
print(name[-6])#s print hoga
print(name[0::2])#every second character from the string//sia
print(name[0::3])#every third character from the striing //sv


