details={"name":"gowtham","age":27,"village":"thummalapalli"}


# modify

print("before modifying")
print(details)
details["name"]="gowthamReddy"
print("after modifying")
print(details)


# delete

print("before delete")
print(details)
del details["name"]
print("after delete")
print(details)

# add

print("before add")
print(details)
details["hight"]="6 feet"
print("after add")
print(details)