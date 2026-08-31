# F=open("emp.db","r")
# data=F.read()
# print(data)
# F.close()

# ******************
F=open("emp.db","r")
while(True):
    data=F.readline()
    if(data==""):break 
    print(data,end="")
F.close()

