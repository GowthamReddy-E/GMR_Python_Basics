# dic={"name":"gowtham","age":27}

# print(dic)
# print(dic["name"])


# print("approach one")
# list1=["name","age"]
# print(type(list1))
# list2=["gowtham",27]
# print(type(list2))

# dic1=dict(zip(list1,list2))
# print(dic1)
# print(type(dic1))

# print("approach two")
# list1=["name","age","village"]
# print(list1)
# print(type(list1))
# list2=["gowtham",27]
# print(list2)
# print(type(list2))

# dic1=dict(zip(list1,list2))
# print(dic1)
# print(type(dic1))


# print("approach three")
# list1=["name","age"]
# print(list1)
# print(type(list1))
# list2=["gowtham",27,9381729345,108,100]
# print(list2)
# print(type(list2))

# dic1=dict(zip(list2,list1))
# print(dic1)
# print(type(dic1))


print("approach four")
tuple1=("name","age","village")
print(tuple1)
print(type(tuple1))
tuple2=("gowtham",27)
print(tuple2)
print(type(tuple2))

dic1=dict(zip(tuple1,tuple2))
print(dic1)
print(type(dic1))
