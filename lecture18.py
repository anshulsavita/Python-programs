# member functions of tuple-->
# - count(n)--> count specified number
# - index(item,[si],[ei]) -->
# eg --> k=index(10)

# t=[5,6,8,2,3,4,6,7,8]
# j=t.count(6)
# print(j)
# j=t.count(6,j+1)
# print(j)

# list--> 
# - is a collection/sequence use to store hetrogenous data
# - mutable in nature 
#   - means one can append/edit/delete data from list.
# - support indexing and slicing
# - support various operators like
#   - >,<,<=,>=,==,!=
#   - in, not in
#   - +(concatination), *n (repeat n times)
# - one can create list using
#   - []
#   - list()
# - support all collection functions
#   - len(),min(),max(),any(),etc

# l=[5,6,8,2,3,4,6,7,8]
# print(l)
# l[2]=1000
# print(l)
# del l[1]
# print(l)

# l=[5,6,8,2,3,4,6,7,8,[4,50,6]]
# print(l[9][1])

# l=[5,6,8]
# a,b,c=l
# print(a,b,c)

# l=[5,6,8]
# a,b,c=l
# print(l)

# **methods of list
# - append(object)--> add element(object) at the end of the list.
# - insert(pos,object) --> insert object at specified position.
# - index(element,[si],[ei]) --> return position of specified element.
# - count(element) --> count number of elements
# - copy() --> create deep copy. 
# - clear() --> clear all elements.
# - extend(list) --> append all elements in list
# - pop([index]) --> remove the last element also return the deleted element, default last element remove.
# - remove(element) --> remove the specified element.
# - reverse() -->
# - sort() --> this will sort original list, sort in assending order.
# - sorted() --> it will make a new list where sorted elements are placed
# - sort(reverse=true) --> sort in dessending order.


# l=[5,6,7]
# l.append('Gwalior') 
# print(l)
# l.append([4,5,6,7])
# print(l)

# l=[5,6,7,8,9,10]
# l.insert(3,'pune')
# print(l)

# l=[5,6,7,8,9,10,40,30]
# i=l.index(8)
# print(i)

# l=[5,6,7,8,9,10,40,30]
# i=l.count(8)
# print(i)

# l=[5,6,7,8,9,10,40,30] # shelo copy
# t=l
# print(t)
# t[2]=15000 # when we make change in t, changes will happens in l automaticaly cause they are pointer variable.
# print(l)

# l=[5,6,7,8,9,10,40,30] # deep copy
# t=l.copy
# print(t)
# t[2]=15000 # when we perform changes in t, l remains same with no changes cause it is a deep copy.
# print(l)
# print(t)

# l=[5,6,7,8,9,10,40,30]
# l.clear()
# print(l)

# l1=[5,6,7,8,9,10,40,30]
# l2=[23,45,67,89,30]
# l1.extend(l2)
# print(l1)

# l=[5,6,7,8,9,10,20]
# l.pop()
# print(l)

# l=[5,6,7,8,9,10,20]
# r=l.pop()
# print(r,"deleted")

# l=[5,6,7,8,9,10,20]
# r=l.pop(3)
# print(r,"deleted")

# l=[5,6,8,5,8,9,20,40]
# l.remove(8)
# print(l)

# l=[5,6,8,5,8,9,20,40]
# l.reverse()
# print(l)

# l=[5,6,8,5,8,9,20,40]
# l.sort()
# print(l)

# l=[5,6,8,5,8,9,20,40]
# l.sorted()
# print(l)

# Q --> how to take list as input from user.
l=[]
for i in range(5):
    v=int(input(f"Enter value @ {i}:"))
    l.append(v)
print(l)