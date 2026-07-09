# *******dictionary (dict)-->
# - use to store data using unique keys and values.
#       ex--> {key: value}
#       key must be unique(string/numeric value)
# - mutable in nature
# - dict does not support following operators
#        +(concatination),*n,>,<,<=,>=
# - does not support indexing and slicing
# - using dict we can read data directly using keys
# - following methods are used to create dict
#       - dict()
#       - {}

# ***************
# d={'9301579572':'Anshul','8989101007':'bade papa','6261797302':'Suhani'}
# mb=input("Enter Mobile number:")
# print(d[mb]) #if key does not found then program will crash.

# ***************
# d={'9301579572':['Anshul','Gwalior','Mp'],'8989101007':['bade papa',"Pune",'MH'],'6261797302':['Suhani','bihar','UP']}
# print(d['8989101007'])
# d['9301579572']=['Alia','mumbai','MH']
# print(d)
# d['8989101007']=['Mohan','Jhansi','Up'] # if key exist then it will over write the data.
# print(d)
# del d['8989101007'] 
# print(d)

# **************
# Q--> take input

# d={}
# for i in range(2):
#     key=input("Enter Mobile number:")
#     value=input("Name/city/State:").split(",")
#     d[key]=value
# print(d)

# ***********

# d={'9301579572':['Anshul','Gwalior','Mp'],'8989101007':['bade papa',"Pune",'MH'],'6261797302':['Suhani','bihar','UP']}
# print(d['8989101007'][1:])

# ******************

# d={'9301579572':{'name':'Anshul','City':'Gwalior','State':'Mp'},'8989101007':{'name':'Abhinav','City':'Bhopal','State':'Mp'},'6261797302':{'name':'Suhani','City':'Gwalior','State':'Mp'}}
# print(d['8989101007']['name'])

# *****************

# D={'CS':{'CS100':{'Name':'Ajay','Grade':'A'},'CS101':{'Name':'Anshul','Grade':'B'},'CS102':{'Name':'Vicky','Grade':'C'}},  
#   'IT':{'IT100':{'Name':'Alia','Grade':'A'},'It101':{'Name':'Rohit','Grade':'B'},'It102':{'Name':'Ashwini','Grade':'C'}},
#   'EC':{'EC100':{'Name':'Thomas','Grade':'A'},'EC101':{'Name':'Peter','Grade':'B'},'EC102':{'Name':'Robin','Grade':'C'}},}

# print(D['EC']['EC101']['Name'])

# **************************
# aws study karna hai sir ne bola hai.

# *******methods of dictionary*****
# get('key','message') --> read data according key. if key does not exist the it return specified message.

D={'CS':{'CS100':{'Name':'Ajay','Grade':'A'},'CS101':{'Name':'Anshul','Grade':'B'},'CS102':{'Name':'Vicky','Grade':'C'}},  
  'IT':{'IT100':{'Name':'Alia','Grade':'A'},'It101':{'Name':'Rohit','Grade':'B'},'It102':{'Name':'Ashwini','Grade':'C'}},
  'EC':{'EC100':{'Name':'Thomas','Grade':'A'},'EC101':{'Name':'Peter','Grade':'B'},'EC102':{'Name':'Robin','Grade':'C'}},}

#R=D.get('CS','Not found')
R=D['CS'].get('CS102','Not found')
print(R)
