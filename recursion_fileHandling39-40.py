# Recursion--- Function itself call a fn known as recursion, recursion must be controled by some condition otherwise it will crash the program, recursion is not a loop.
# why recursion? --> use for backtracking...
# recursion use stack memory to memorise the function


# def India():
#     print("In India")
#     Us()
#     print("Again in India")

# def Us():
#     print("In Us")
#     China()
#     print("Again in USA")

# def China():
#     print("In China")

# India()
# print("End")


# ***********************

# def call(n):
#     print("Hello:",n)
#     if(n>=1):
#         call(n-1)
#     print("Bye:",n)

# call(5)
# print("End")

# **********************

# File_Handling --> use to store data permanently in secondry storage device.
# open("filename","mode")

# ****mode****
# w: write (will create new file & open it into write mode)
# a: append
# r:read
# rb:read bytes
# wb: write bytes
# ab: append bytes

# F=open("Student.db","w");
# F is an object which holds the address of file stored in secondary memory 
# write(data) --> write data in a file

F=open("Student.db","w");
F.write("100,harry Singh")
F.close()