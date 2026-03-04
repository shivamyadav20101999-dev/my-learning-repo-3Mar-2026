#Problem 5:Search for a number x in this tuple using a loop:
#tuple={1,4,9,16,25,36,49,64,81,100}.
nums=(1,4,9,16,25,36,49,64,81,100)

# x=36
# i=0

# while i<len(nums):
#     if (nums[i]==x):
#          print("Found at index: ",i,nums[i])
#     else:
#        print("Findinf.............")
#     i += 1

# i=0
# while i<5:
#     if(i==3):
#         print(i)
#         break
#     else:
#      print("finding:...........")
#     i += 1


# print("end of loop")
    


i=0
while i<=5:
    if(i==3):
        i += 1
        continue#skip
    
    print(i)
    i +=1

