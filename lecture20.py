# x=['abc','xyz','aba','1221']
# c=0
# for v in x:
#     if(len(v)>=2 and v[0]==v[-1]):
#         c+=1
# print(c)

# ***************

# x=[7,8,6,7,6,8,1,4,9]
# l=[]
# for v in x:
#     if(x.count(v)==1):
#         l.append(v)
# print(l)

# *******************

# x=[1,2,3,4]
# y=[1,5,6,7]
# for v in x:
#     if(v in y):
#         print(True)
#         break 

# *******************

# x=['red','green','white','black','pink','yellow']
# for i in [5,4,0]:
#     n=x.pop(i)
#     print("Deleted:",n)
# print(x)

# *****************

# l=[]
# for i in range(3):
#     c=[]
#     for j in range(3):
#         v=int(input(f"Enter number @ {i},{j}:"))
#         c.append(v)
#     l.append(c)
# print(l)

# *******************

t=(33,44,55,77,88,99)
for i,v in enumerate(t):
    print(i,v)