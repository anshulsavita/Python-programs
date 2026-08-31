# F = open("kid.txt", "r", encoding="utf-8")
# txt = F.read()
# print(txt)
# F.close()

# *********************
# F = open("kid.txt", "r", encoding="utf-8")
# txt = F.read()
# print(txt.count("\n"))
# F.close()

# *********************
# c=0
# F = open("kid.txt", "r", encoding="utf-8")
# txt = F.read()
# for i in txt:
#     if(i.isupper()==True):
#         c+=1
# print(c)
# F.close()

# *********************
# F = open("kid.txt", "r", encoding="utf-8")
# txt = F.read()
# txt=txt.split(' ')
# print(len(txt))
# F.close()

# ********************
# F = open("kid.txt", "r", encoding="utf-8")
# txt = F.read()
# print(len(txt))
# F.close()

# *******************
sf=input("Enter Source File:")
S=open(sf,"rb")
data=S.read()
tf=input("Enter Target File:")
T=open(tf,'wb')
T.write(data)
T.close()
S.close()
print("File copied..")