
F = open(r"C:\Users\Asus\Desktop\Python\filehand40-41\Student\student.db", "r")
while(True):
    info=F.readline()
    if(info==''): break
    print(info,end='')
F.close()
