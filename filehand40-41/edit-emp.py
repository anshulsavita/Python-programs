F=open("emp.db","r")
id=input("Enter Employee Id:")
while(True):
    data=F.readline()
    if(data==""):break 
    L=data.split(",")
    L[4]=L[4].rstrip("\n")
    if(L[0]==id):
        da=int(L[4])*56/100
        hra=int(L[4])*30/100
        L.append(da)
        L.append(hra)
        print(L)
F.close()