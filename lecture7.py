# ****ord(char)--> return ascii value of specified character
# x='A'
# print(ord(x))

# x='9'
# print(ord(x))

# x='Arrun'
# print(ord(x)) # it will give error

# ***chr(ascii)--> return character according to given ascii value
# x=65
# print(chr(x))

# x=input("Enter Character:")
# if(ord(x)>=65 and ord(x)<=90):
#     print("Upper case")
# else:
#     print("Not in upper case")

# i=65
# while(i<=90):
#     print(chr(i),end=" ")
#     i=i+1

# *****for loop******
# Syntax-->
# for<var> in <collection>:
#     ===
#     ===
#     ===

# ex-->
# for i in [3,8,12,34]:
#     print(i)

# for i in "Gwalior":
#     print(i)

# for i in [4,5,6,7,12]:
#     print(i)

# for i in [4,5,6,7,12]:
#     print(i*10)

# for i in ["Gwalior","Bhopal",89,56.7,"Indore"]:
#     print(i)

# for i in "Gwalior":
#     print(ord(i))
    
# *****range(min,max-1,[diff])-->[]-->  this stands for optinal.

# k=range(100,200) #by default diff is +1

# for i in range(100,120):
#     print(i,end=' ')

# for i in range(100,200,10):
#     print(i,end=' ')

# for i in range(200,100):
#     print(i,end=' ')  # this will not work

# for i in range(200,100,-1):
#     print(i,end=' ')

# for i in range(10):
#     print(i,end=' ') # by default minimum range is 0

# for i in range(1,5):
#     for j in range(1,6):
#         print(j,end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# for i in range(6,1,-1):
#     for j in range(1,i):
#         print(j,end=' ')
#     print()

# for j in range(1,6):
#     print("x"*j)

# ********************
# sps=10
# for i in range(1,10,2):
#     print(" "*sps,end='')
#     print("*"*i)
#     sps=sps-1

# for i in range(6,1,-1):
#     for j in range(1,i):
#         print(" ",end='')
#     for j in range(1,6):
#         print("*",end='')
#     print()

for i in range(1,6):
    for j in range(1,i+1):
        print(" ",end='')
    for j in range(1,6):
        print("*",end='')
    print()
    