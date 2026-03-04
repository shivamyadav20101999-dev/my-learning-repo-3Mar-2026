age=int(input("Enter your Age: "))
if age<0 or age>100:
    print("Invalid Age enter")
elif age>=18:
    print("You are eligible to vote")
else:
    print("Yor are not eligible to vote")