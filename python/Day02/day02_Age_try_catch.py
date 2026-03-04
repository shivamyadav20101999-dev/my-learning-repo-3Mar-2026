try:
    age=int(input("Enter your age: "))

    if not(0<=age<=120):
        print("Invalid age")
    elif age>=18:
        print("eligible")
    else:
        print("not eligible")

except ValueError:
  print("invalid value")
