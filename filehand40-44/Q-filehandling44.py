# --> read data from a file from 40 byte to 200 byte and make them upper case.
# F=open("kid.txt",'rb')
# F.seek(40,0) 
# data=F.read(200) 
# data=data.upper()
# print(data.decode('utf-8',errors='ignore')) 
# F.close()

# ***********************************
# --> copy only those characters whom startswith 'th' from a file and put is into another file
f=open('kid.txt','r',encoding='utf-8')
t=open('kii.txt','w')
data=f.read()
l=data.split(' ')
for i in l:
    if(i.startswith('th')):
        t.write(f"{i} ")
t.close()
f.close()
print("Data Transfered...")

# ************************************
# --> count how many t is in a file
# f=open("kid.txt",'r',encoding="utf-8")
# data=f.read()
# c=data.lower().count('t')
# print(c)
# f.close()

