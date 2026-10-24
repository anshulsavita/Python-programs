# k=lambda a,b:list(a[i]+v for i,v in enumerate(b))
# l1=[1,2,3,4,5]
# l2=[2,3,4,5,6]
# l3=k(l1,l2)
# print(l3)

# *********************

# k=lambda a:list(v[v.find(' ')+1:] for i,v in enumerate(a))
# l=['Lalit Sharma','Ankit Triphati','Manoj patil']
# c=k(l)
# print(c)

# **********************
# # **Add new key (discount) and print 10% discount of price as value
# k=lambda n:list(v.setdefault('discount',v['price']*0.10) for v in n)
# D=[{'id':100,'Name':"Fanta",'price':50},{'id':200,'Name':"pepsi",'price':70},{'id':300,'Name':"Red Bull",'price':120}]
# l=k(D)
# print(D)

# ***********************
# ****Map(fn,sequences)--> map read values one by one from sequences and give it to function parameter
# l=['Lalit Sharma','Ankit Triphati','Manoj patil']
# k=list(map(lambda N: N[N.find(' ')+1:],l))
# print(k)

# def addkey(N):
#     N.setdefault('Discount',N['price']*0.10)
# D=[{'id':100,'Name':"Fanta",'price':50},{'id':200,'Name':"pepsi",'price':70},{'id':300,'Name':"Red Bull",'price':120}]
# k=list(map(addkey,D))
# print(D)

# ******************
# def add (a,b):
#     return a+b
# l1=[5,6,7,8]
# l2=[5,6,7,8]
# k=list(map(add,l1,l2))
# print(k)