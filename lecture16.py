# ******Tuple*****---
# - is a collection/sequence whice holds data hetrogenous in nature
# - immutable in nature
# - support indexing and slicing
# - support various operators like
#   >,<,<=,>=,==,!=
#   in, not in
# - support + concatination, *n (repeat)
# - one can create tuple using
#   - ()
#   - tuple() --> constructor

# t=()
# print(type(t))

# ******************
# T=(5,7,5,4,8,9,34,23)
# print(T[3])
# print(T[2:6])
# print(T[:])
# print(T[:5])
# print(T[5:])
# print(T[::-1])
# print(T[5:1:-1])
# k=T+(66,'Gwalior') # --> create new address(memory) 
# print(k)
# k=T+*3 # create new address
# print(k)

# ******************
# T1=(400,7,5,4)
# T2 =(7,1200,400,9)
# print(T1>T2)
# j=1200 in T2
# print(j)
# T1[1]=90 # --> error because it is immutable
# T=T+(45) # --> because (45) is not a touple, (45,) is a tuple.

# *******************
t=(400,7,5,4,'pune',66.7,(66,44,55))
print(t[4][1:]) #--> print une
print(t[6][2]) #--> print 55
print(t[6][:2]) #--> print 55
n=t[:4]+t[5:] # --> remove pune
print(n)

# *********************
# best example why we use tuple-->
#   - money = (500,200,100,50,20,10,5,2) # currency never change
#   - week = ('Sunday','Monday','Tuesday','Wednesday','Thursday',"Friday",'Saturday')
#   - Months = 


