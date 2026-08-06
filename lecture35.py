# def addValue(a):
#     return a+100
# L=[5,6,7,8,9]
# k=list(map(addValue,L))
# print(k)

# L=[5,6,7,8,9]
# k=list(map(lambda a: a+100,L))
# print(k)

# *****Filter****
# filter(fn,sequence) --> return element if condition is satisfied.
# L=[6,7,9,4]
# k=list(filter(lambda a: a%2==0,L))
# print(k)

# *******************
# L=[6,7,9,4]
# k=list(filter(lambda a: a>5,L))
# print(k)

# *********************
# def search(a):
#     return a>5
# L=[6,7,9,4]
# k=list(filter(search,L))
# print(k)

# ************************
# d=[{'Rollno': 100,'Name': "anshul","p":89,"C":28,"M":80},{'Rollno': 101,'Name': "Sandeep","p":73,"C":78,"M":90},{'Rollno': 102,'Name': "rohit","p":65,"C":45,"M":50},{'Rollno': 103,'Name': "sumit","p":59,"C":38,"M":70},{'Rollno': 104,'Name': "savita","p":74,"C":87,"M":29}]
# k=list(filter(lambda S: 'd' in S['Name'].lower(),d))
# print(k)

# ***************************
# d=[{'Rollno': 100,'Name': "anshul","p":89,"C":99,"M":95},{'Rollno': 101,'Name': "Sandeep","p":73,"C":78,"M":90},{'Rollno': 102,'Name': "rohit","p":65,"C":45,"M":50},{'Rollno': 103,'Name': "sumit","p":59,"C":38,"M":70},{'Rollno': 104,'Name': "savita","p":74,"C":87,"M":29}]
# K=list(filter(lambda a: (a['p']+a['C']+a['M'])/3 >= 90, d))
# print(K)

# ********************
# def setKey(A):
#     return A[1]
# l=[[6,8],[8,2],[10,50],[6,7],[9,67]]
# R=sorted(l,key=setKey)
# print(R)

# ********************
l=[[6,8],[8,2],[10,50],[6,7],[9,67]]
R=sorted(l,key=lambda A:A[1])
print(R)