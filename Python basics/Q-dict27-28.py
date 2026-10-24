# **
# d={}
# x=int(input("Enter n:"))
# for i in range(1,x):
#     t=i*i
#     d.setdefault(i,t)
# print(d)

# *********sum all the items in dictionary*****
# d={7:100,2:900,3:500,4:1000}
# l=[]
# for i in d:
#     l.append(i+d[i])
# print(l)

# *****or****
# d={7:100,2:900,3:500,4:1000}
# l=[]
# for i in d.items():
#     l.append(sum(i))
# print(l)

# *********program to map two list into a dict. map-->element of l1 becomes key and l2 becomes value.********
# l1=["India","Nepal","Bangladesh"]
# l2=["New Delhi","Katmandu","Dhaka"]
# d={}
# for i,v in enumerate(l1):
#     d.setdefault(l1[i],l2[i])
# print(d) 

# **********or **********
# l1=["India","Nepal","Bangladesh"]
# l2=["New Delhi","Katmandu","Dhaka"]
# d={}
# for i,v in enumerate(l1):
#     d[v]=l2[i]
# print(d) 

# *****************

# d={1:400,2:500,3:600,4:800}
# ma=max(d.values())
# mi=min(d.values())
# print(ma)
# print(mi)

# ***********************
# ---to convert list in dictionary---works only when it has 2 elements in list or tuple, one for key and another for value.
# t=[[8,9],[4,6],[56,8]]
# D=dict(t)
# print(D)




