
# string methods:

word = "Hello , Shivam Yadav is great!"
#1. #len()
print(len(word))#length of string

#2. upper()
print(word.upper())#convert string in upper case

#3. lower()
print(word.lower())#convert string in lower case

#4. count()
print(word.count('a'))

#5. find()
print(word.find('H'))

#6. split()
print(word.split(','))
print(word.split())

#7 . replace()
#print(word.replace('old_value','new_value'))
print(word.replace('Shivam','Pushpa'))

#8.title()
print(word.title())

#9.strip()
word2 = "   hello world  "
print(len(word2))
print(word2.strip())

#j10.oin()
zwords = ("Hello" , "shivam" , "is", "good!")
print(' '.join(zwords))
print('-'.join(zwords))