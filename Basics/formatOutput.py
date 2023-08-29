# they are 4 ways we formatting the output

name="gowtham"
age=27
sal=27000.500

# first way
print("first way")
print(name)
print(age)
print(sal)


# second way
print("second way")
print("name is:",name)
print("age is:",age)
print("sal is:",sal)

# third way  %
print("third way")
print("Name:%s age:%d sal:%g"%(name,age,sal))

# fourth way  {}
print("fourth way")
print("Name:{} age:{} sal:{}".format(name,age,sal))


print("Name:{0} age:{1} sal:{2}".format(name,age,sal))


print("Name:{2} age:{2} sal:{2}".format(name,age,sal))