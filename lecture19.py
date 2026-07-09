# l=[[6,7],[5,9,3,3],[6,8,9],[3,7,8,9]]
# r=[]
# for i in range(len(l)):
#     c=sum(l[i])
#     r.insert(c)
# print(r)

# **********or***********

# l=[[6,7],[5,9,3,3],[6,8,9],[3,7,8,9]]
# r=[]
# for i in l:
#     r.append(sum(i))
# print(r)

# ***********************

# l=['red','yellow','green','red','blue','red','green']
# for i in l:
#     if(i=='red'):
#         l.remove('red')
# print(l)

# **********or*******
# l=['red','yellow','green','red','blue','red','green']
# for i in range(l.count('red')):
#         l.remove('red')
# print(l)

# **************

# l=[]
# for i in range(5):
#     l.append(int(input("Enter value:")))
# print(l)

# *****************

l=[[],[],[]]
for i in range(3):
        x=input("Enter name:")
        y=int(input("Enter mm:"))
        z=int(input("Enter cm:"))
        a=int(input("Enter pm:"))
        l.append([x,y,z,a])
print(l)