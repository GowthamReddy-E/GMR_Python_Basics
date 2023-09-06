listOne=[1,2,3,4,5,6,7,8,9,10]



# method one specific-Portion

listOne[:4]=[1,2,3,4,5,6,7,8,9,10]
# here we slice 0:4 values and replace those values into right hand side it will replace those left hand side values
# left hand side values are two to three values and right hand side values are more than three, it will also replace all right hand side values into left hand side values



# method two  increment by 2 or 3 
listOne=[1,2,3,4,5,6,7,8,9,10]

listOne[0::5]=[1,2,3,3,4,5,6]    # thrown an error

print(listOne)

# in this scenario  the LHS!=RHS that why we can not replace those values
# we can achieve by using the loops 

# method three 



listOne=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
n=2
for val in range(0,listOne.__len__(),n):
    listOne[val]=1

print(listOne)