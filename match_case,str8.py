# ********match...case*****
# Syntax-->
# match <variable>:
#     case <constant>:
#         =====
#         =====
#     case <constant>:
#         =====
#         =====
#     case _:
#         ====
#         ====

# i = int(input("Enter Day:"))
# match i:
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case _:
#         print("Invalid Day")

# ********or******

# i = int(input("Enter Day:"))
# match i:
#     case "Maruti Alto":
#         print("1450000")
#     case "Maruti Ciaz":
#         print("price 13000000")
#     case _:
#         print("Invalid Day")

# *******Strings*****
# - It is a collection in python.
# - strings are immutabe in nature (it can't be changed), we can't do any changes in same memory of a variable.
# - It support various operators like
#     *n repeat string n times
#     + concatinate --> it is worst in coding.
#     >,<,>=,<=,==,!=
#     in, not in
# - support indexing and slicing

# ****immutable**
# x="Tajmahal"
# print(x)
# print(x[2])
# # x[2]="p" #error
# x=x+"is in Agra"
# print(x)
# automatic garbage collection --> That location whose address is not pointed by any variable.
# Rule for immutable --> jo memory immutable hoti hai uske ghar(memory) me kabhi changes nahi kar payenge

# ***various operator
# x="Amit"
# y="Amar"
# t=x>y #--> overloaded operator
# print(t)

# **************
# x="Amit"
# y="Z"
# t=x>y #--> overloaded operator
# print(t)

# ******slicing******to slipe something in a string.
# x[[si]:[ei-1]:[diff]] #star index, end index, difference.

# x="mumbai"
# print(x[0])
# print(x[-1]) #circular
# print(x[-2])

# # slicing--
# x="mumbai"
# print(x[1:5])
# print(x[1:])
# print(x[:])
# print(x[:4])

# print(x[::]) # by default diff --> +1
# print(x[::2])
# print(x[::-1])

# ****************
# x="mumbai city"
# # print(x[7:3]) #it will not run
# print(x[7:3:-1]) 

# *******************
for p in ["9301579572","9301598764","9301554322"]:
    T=("X"*6)+p[6:]
    print(T)

# ******Methods of strings******
