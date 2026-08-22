
F = open(r"C:\Users\Asus\Desktop\Python\filehand40-41\Student\student.db", "r")
rn=input("Enter Student Roll Number:")
while(True):
    data=F.readline()
    if(data==""):break 
    L=data.split(",")
    L[5]=L[5].rstrip("\n")
    if(L[0]==rn):
        t=int(L[3])+int(L[4])+int(L[5])
        per=t/3
        L.append(t)
        L.append(f"{per:.2f}%")
        print(L)
F.close()