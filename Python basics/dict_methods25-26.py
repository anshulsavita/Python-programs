# pop(key) --> remove data from dict according to specified key.
# popitem() --> remove the last item.
# copy() --> create shallow copy of dict
# clear() --> it will clear the data
# update(dict) --> update dict with specified dict values.
# formkeys(sequence,default_value) -->  for making dict from sequence. sequence will be the keys

# D={'A100':{'Name':'Ajay',"Salary":'30000'},'A101':{'Name':'Vijay',"Salary":'40000'},'A102':{'Name':'Vikas',"Salary":'50000'}}
# R=D.pop('A101')
# print(R)
# print(D)

# D={'A100':{'Name':'Ajay',"Salary":'30000'},'A101':{'Name':'Vijay',"Salary":'40000'},'A102':{'Name':'Vikas',"Salary":'50000'}}
# R=D.popitem()
# print(D)

# D={'A100':{'Name':'Ajay',"Salary":'30000'},'A101':{'Name':'Vijay',"Salary":'40000'},'A102':{'Name':'Vikas',"Salary":'50000'}}
# R=D.clear()
# print(D)

# D={'A100':{'Name':'Ajay',"Salary":'30000'},'A101':{'Name':'Vijay',"Salary":'40000'},'A102':{'Name':'Vikas',"Salary":'50000'}}
# M={'A101':{'Name':'Ritika',"Salary":'60000'},'A201':{'Name':'Pankaj',"Salary":'40000'}}
# D.update(M)
# print(D)

# ****************
# D=dict.fromkeys(['INC','BJP','AAP','BSP'],0)
# print(D)

# ******************
# D=dict.fromkeys(['INC','BJP','AAP','BSP'],0)
# print(D)
# for i in range(5):
#     party=input("Enter Party Name:")
#     D[party]=D[party]+1
# print(D)

# ******************

d={'India':{'capital':'Delhi'},'Pakistan':{"capital":'Lahore'},'Nepal':{'Capital':'Katmandu'}}
x=input("Enter country:")
r=d.get(x,'not found')
print(r)

