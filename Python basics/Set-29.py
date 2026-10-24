# *********set********
# - holds unique values
# - it is unordered list
# - element of set are immutable
# - but whole set is mutable
# - does not support indexing and slicing
# - Data hetrogenous in nature (Hetrogenous collection)
# - does not support +(concatination), *(repeat)
# - support for loop to read data from set one by one
#       - support enumarate
# - support
#       ==,<=,>=,<,>
# 

# *****************
# T={78,43,5,65,75}
# for v in T:
#     print(v)

# ****methods****
# add(object) --> add element in the set
# copy(s) --> create deep copy
# discard(element) --> remove specified element.
# pop() --> remove last element (by its memory)
# remove() -->
# union(set) --> merge two set.
# intersection --> return common elements
# difference(set) --> remove all the values which exist in second set
# issubset() --> return true if s1 is subset of s2
# issuperset(set) -->
# isdisjoint() --> 
# update() --> 

# s={42,35,54,64,75,75}
# print(s)
# s.add(100)
# print(s)

# *****************
# s={42,35,54,64,75,75}
# s.discard(35)
# print(s)

# *****************
# s={42,35,54,64,75,75}
# t=s.pop()
# print("deleted:",t)

# s={42,35,54,64,75,75}
# s.remove(54)
# print(s)

# s1={42,35,54,64,75,75}
# s2={100,400,89,67,45,1000,670}
# s3=s1.union(s2)
# print(s3)

# s1={42,35,54,67,75,75}
# s2={100,400,89,67,45,1000,670}
# s3=s1.intersection(s2)
# print(s3)

# s1={42,35,54,64,75,75}
# s2={100,400,89,67,75,1000,670}
# s3=s1.difference(s2)
# print(s3)

# s1={100,500,400,800}
# s2={10,100,500,60,400,77,800,900}
# s3=s1.issubset(s2)
# print(s3)

# s1={100,500,400,800}
# s2={10,100,500,60,400,77,800,900}
# s3=s1.issuperset(s2)
# print(s3)

# s1={100,500,400,800}
# s2={10,60,77}
# s3=s1.isdisjoint(s2)
# print(s3)

# s1={100,500,400,800}
# s2={10,60,77}
# s2.update(s1)
# print(s2)

s1={100,500,400,800}
s2={10,60,77}
print(len(s1))
print(min(s1),max(s1))
print(sorted(s1))