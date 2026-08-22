
F = open(r"C:\Users\Asus\Desktop\Python\filehand40-41\Student\student.db", "r")
print("------Main Menu-----")
print("1.Roll number\n2.Name\n3.Gender\n4. Physics Marks\n5.Chemistry Marks\n6.Maths Marks")
ch=int(input("Enter How u want to Search:"))
match ch:
    case 1:
        rn=input("Enter Student Roll Number:")
        while(True):
            data=F.readline()
            if(data==""):break 
            L=data.split(",")
            L[5]=L[5].rstrip("\n")
            if(L[0]==rn):
                print(L)

    case 2:
        name=input("Enter Student Name:")
        while(True):
            data=F.readline()
            if(data==""):break 
            L=data.split(",")
            L[5]=L[5].rstrip("\n")
            if(name.title() in L[1]):
                print(L)

    case 3:
        gender=input("Enter Employee Gender:")
        while(True):
                data=F.readline()
                if(data==""):break 
                L=data.split(",")
                L[5]=L[5].rstrip("\n")
                if(L[2]==gender.title()):
                    print(L)
    case 4:
        p1=input("Enter Student's Minimum Physics Marks:")
        p2=input("Enter Student's Maximum Physics Marks:")
        while(True):
            data=F.readline()
            if(data==""):break 
            L=data.split(",")
            L[5]=L[5].rstrip("\n")
            if(L[3]>=p1 and L[3]<=p2):
                print(L)
    case 5:
            c1=input("Enter Student's Minimum Chemistry Marks:")
            c2=input("Enter Student's Maximum Chemistry Marks:")
            while(True):
                data=F.readline()
                if(data==""):break 
                L=data.split(",")
                L[5]=L[5].rstrip("\n")
                if(L[4]>=c1 and L[4]<=c2):
                    print(L)

    case 6:
            m1=input("Enter Student's Minimum Maths Marks:")
            m2=input("Enter Student's Maximum Maths Marks:")
            while(True):
                data=F.readline()
                if(data==""):break 
                L=data.split(",")
                L[5]=L[5].rstrip("\n")
                if(L[5]>=m1 and L[5]<=m2):
                    print(L)
    case _:
          print("Wrong input...")
F.close()