# open() 
# -  will open a file in various modes 

# - types of modes
#     "w" write --> will create a new file and open it into write mode
#     "r" read
#     "a" append
#     "wb" write bytes (image/audio/video/text)
#     "rb" read bytes
#     "ab" append bytes
#     "w+" read/write
#     "r+" read/writew
#     "a+" append/read

# syntax --> 
#   F=open("filename","mode")

# F=open("emp.db","w") # --> it means that in this case it will create a new file and open it into write mode.
# F is a file object which holds the address of specified file.

# function --->
# write(data) --> write data in File
# read() --> read all data from File
# read(bytes) --> read n bytes from a file
# readline()---> read a single line 
# readline(bytes) --> read n bytes 
# close()---> close the open file

F=open("emp.db","a")
while(True):
    id=input("Enter Employee Id:")
    name=input("Enter Employee Name:")
    age=input("Enter Age:")
    gender=input("Enter gender:")
    salary=input("Enter salary:")
    ch=input("Add More Employee Yes/No?")
    F.write(f"{id},{name},{age},{gender},{salary}\n")
    if(ch.lower()=="no"): break
F.close()