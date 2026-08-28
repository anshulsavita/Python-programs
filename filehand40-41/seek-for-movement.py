# --> 0=begin, 1-current, 2-end (represents)
# utf --> universal text formate.

# F=open("kid.txt",'rb')
# F.seek(150,0) # begin (0) se 150 th position per move karna hai
# data=F.read(100) #--> 100 - itni bite padhni hai
# print(data.decode('utf-8',errors='ignore')) 
# # decode is to fix invisible codes like '\t' or '\n',it is needed because we are opening it in byte mode so it will print '\t' insteed of "   " or "\n" insteed of "next line" ects.. so for fix this we need decode.
# F.seek(100,1)
# data=F.read(50)
# print(data.decode('utf-8',errors='ignore'))
# F.close()

# **************************
F=open("kid.txt","rb")
F.seek(-150,2)
data=F.read(10)
print(data.decode("utf-8",errors="ignore"))
F.close()