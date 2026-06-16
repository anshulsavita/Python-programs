# common function of collection
# len(c) #--> c stands for collections
# sorted(c,[reverse=True]) --->
# # sum(c) it is not for us right now
# max(c) -->
# min(c) -->
# all(c) --> koi bhi value null nahi hone chaiye ya fir 0 ya fir blank ya fir none.
# any(c) --> kam se kam ek value honi chaiye. 

# x=['m','a','n','d','e','e','p']
# print(len(x))
# print(sorted(x))
# t=sorted(x)
# t=sorted(x,reverse=True)
# print(t)

# x=['Ramit','Anay','Vinay','Pankaj','Peter','Anmol']
# t=sorted(x)
# print(t)
# t=max(x)
# print(t)
# t=min(x)
# print(t)
# t=all(x)
# print(t)
# t=any(x)
# print(t)

# **********************
# x=['Ramit','Anay','Vinay','Pankaj','Peter','Anmol']
# for i in x:
#     if('A' in i.upper()):
#         print(i)

# x="Pankaj Sharma,Ankit Singh,Aliya Tripathi,vikas Sharma,Mohan Kapoor"
# L=x.split(",")
# for s in L:
#     if(s.endswith('Sharma')):
#         print(s)

# x="Pankaj Sharma,Ankit Singh,Aliya Tripathi,vikas Sharma,Mohan Kapoor"
# L=x.split(",")
# for s in L:
#     if(s.endswith('Sharma')):
#         i=s.replace('Sharma','Verma')
#         print(i)

# x="Coke and Pepsi are softdrinks,widly used during summer in north india, price of coke is 20 Rs and pepsi is 15 rs"
# L=x.split(" ")
# for s in L:
#     if(s.isdigit()):
#         print(s)

# x="Coke and Pepsi are softdrinks,widly used during summer in north india, price of coke is 20 Rs and pepsi is 15 rs"
# t=x.count(",")
# print(t)

x="red,green,blue,red,yellow"
i=x.replace('red','pink')
i=i.replace('pink','red',1)
print(i)







