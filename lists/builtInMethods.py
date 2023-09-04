list1=[1,2,3,4,5,6,7,8,9]
list2=[30,20]


list1.insert(3, 222)
print(list1)

list1.append(10)
print(list1)

# Extend the list by adding the elements of another list
list1.extend(list2)
print(list1)

# Count the number of occurrences of a specific element in the list
count = list1.count(5)
print(count)
# Get the index of a specific element in the list
index = list1.index(5)
print(index)

# Reverse the order of elements in the list
list1.reverse()
print(list1)



# Sort the list in ascending order
list1.sort()
print(list1)
# Remove an element at a specific index from the list
print(list1.pop(6))


# Insert a number at a specific index in the list
list1.insert(5, 555)
print(list1)
