F = open(r"C:\Users\Asus\Desktop\Python\filehand40-41\Student\student.db", "a")
while(True):
    rl=input("Enter Student Roll number:")
    name=input("Enter Student Name:")
    gender=input("Enter Student Gender:")
    p=input("Enter Physics Marks:")
    c=input("Enter Chemistry Marks:")
    m=input("Enter Maths Marks:")
    F.write(f"{rl},{name},{gender},{p},{c},{m}\n")
    ch=input("U want to add more yes/no?:")
    if(ch=="no"): break
F.close()
