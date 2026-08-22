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

# Example --> we will use it in chats servers like WhatsAap
