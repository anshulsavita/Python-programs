# L=[['pepsi',67,30],['Fanta',100,23],['7up',50,10]]
# k=list(map(lambda a: [a[0],a[1],a[2],a[1]-a[2]],L))
# print(k)

# *********or*******
# L=[['pepsi',67,30],['Fanta',100,23],['7up',50,10]]
# k=list(map(lambda a: a+[a[1]-a[2]],L))
# print(k)

# **********or*******
# L=[['pepsi',67,30],['Fanta',100,23],['7up',50,10]]
# k=list(map(lambda a: a.append(a[1]-a[2]) or a,L))
# print(L)

# *********or*******
# L=[['pepsi',67,30],['Fanta',100,23],['7up',50,10]]
# k=list(map(lambda a: a.append(a[1]-a[2]),L))
# print(L)

# ***********************
L=[{'name':'Pepsi','rate':67,'offer':30},
   {'name':'Fanta','rate':67,'offer':80},
   {'name':'7up','rate':100,'offer':130}]
k=list(map(lambda a: a.setdefault('Status','loss')if (a['rate']>a['offer']) else a.setdefault('Status','profit'),L))
print(L)

