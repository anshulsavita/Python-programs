# ******************
# F=open("emp.db","r")
# gender=input("Enter Gender:")
# while(True):
#     data=F.readline()
#     if(data==""):break 
#     L=data.split(",")
#     L[4]=L[4].rstrip("\n")
#     if(L[3]==gender.title()):
#         print(L)
# F.close()

# ***************************
F=open("emp.db","r")
print("------Main Menu-----")
print("1.Id\n2.Name\n3.Age\n4.Gender\n5.Salary\n")
ch=int(input("Enter How u want to Search:"))
match ch:
    case 1:
        id=input("Enter Employee Id:")
        while(True):
            data=F.readline()
            if(data==""):break 
            L=data.split(",")
            L[4]=L[4].rstrip("\n")
            if(L[0]==id):
                print(L)

    case 2:
        name=input("Enter Employee Name:")
        while(True):
            data=F.readline()
            if(data==""):break 
            L=data.split(",")
            L[4]=L[4].rstrip("\n")
            if(name.title() in L[1]):
                print(L)

    case 3:
        age1=input("Enter Employee's Minimum Age:") 
        age2=input("Enter Employee's Maximum Age:") 
        while(True):
                data=F.readline()
                if(data==""):break 
                L=data.split(",")
                L[4]=L[4].rstrip("\n")
                if(L[2]>=age1 and L[2]<=age2):
                    print(L)
    case 4:
        gender=input("Enter Employee Gender:")
        while(True):
                data=F.readline()
                if(data==""):break 
                L=data.split(",")
                L[4]=L[4].rstrip("\n")
                if(L[3]==gender.title()):
                    print(L)
    case 5:
        salary1=input("Enter Employee's Minimum Salary:")
        salary2=input("Enter Employee's Maximum Salary:")
        while(True):
            data=F.readline()
            if(data==""):break 
            L=data.split(",")
            L[4]=L[4].rstrip("\n")
            if(L[4]>=salary1 and L[4]<=salary2):
                print(L)
    case _:
          print("Wrong input...")
F.close()
