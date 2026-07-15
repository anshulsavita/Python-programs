# ******Methods of dictonary****
# setdefault(key,value) --> this function insert key:value within the dict, if specified key does not exist, but it will not update the key and its value if given key is exist.
# Values() --> return all the values in list
# keys()--> return all the keys in list
# items() --> Return keys and values in list of tuples.

# D={'CS':{'CS100':{'Name':'Ajay','Grade':'A'},'CS101':{'Name':'Anshul','Grade':'B'},'CS102':{'Name':'Vicky','Grade':'C'}},  
#   'IT':{'IT100':{'Name':'Alia','Grade':'A'},'It101':{'Name':'Rohit','Grade':'B'},'It102':{'Name':'Ashwini','Grade':'C'}},
#   'EC':{'EC100':{'Name':'Thomas','Grade':'A'},'EC101':{'Name':'Peter','Grade':'B'},'EC102':{'Name':'Robin','Grade':'C'}},}

# D.setdefault('CiVil',{'CIVIL100':{'Name':'Vijay','Grade':'A'},'CIVIL101':{'Name':'Deepak','Grade':'B'},'Civil102':{'Name':'Rohan','Grade':'C'}})
# print(D)

D={}
for i in range(2):
    dep=input("Enter department:")
    employee={}
    for j in range(2):
        employeeid=input("Enter Employee Id:")
        name,gender,salary=input("Enter name,Gender,Salary:").split(",")
        employee.setdefault(employeeid,{'Name':name,"Gender":gender,'Salary':salary})
    D.setdefault(dep,employee)
print(D)

# D={'A100':{'Name':'Ajay',"Salary":'30000'},'A101':{'Name':'Vijay',"Salary":'40000'}}
# V=D.values()
# print(V)
# # #*******or*****
# print(list(V))
# k=D.keys()
# print(list(k))

# for k in D:
#     print(k) # by default it will give Keys
#     print(D[k]) # it will give values of keys
#     print(k,D[k])

# I=D.items()
# print(I)