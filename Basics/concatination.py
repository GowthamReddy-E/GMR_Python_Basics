# we can concatinate only number with float ,number with boolean ,float with boolean 
# we cant concatinate number with string, boolean with string,float with string
# in python true=1 false=0



# number with float
a=10
b=10.5
print(a+b)

# number with boolean
c=10
d=True
print(c+d)

# float with boolean
e=10.5
f=False
print(e+f)

# string with all
g=10
h=10.5
i=True
j="gowtham"
print(g+j)                  # we can not add the number with string 
print(h+j)                  # we can add only string with string
print(i+j)
print(j+j)