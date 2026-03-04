#[1,4,9,16,25,36,49,64,81,100]
#2.Search for a number x in this tuples using for loop
tup=(1,4,9,16,25,36,49,64,81,100,36)#using linear search=>linear search mtlb ek line ke
#ke andar search ek ek kar ke search
x=36
idex=0
for el in tup:
    if(el==x):
       print("number founded ",idex)
      # break//one time found and break
    idex += 1

