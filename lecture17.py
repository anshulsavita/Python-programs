# T=(45,67,90,45,67) 
# for i in T:
#     print(i)
# # *********or*********
# for i in range(len(T)):
#     print(T[i])

# ************************
# t=((45,67),(90,45,67),(8,4,5,6),(1,2,9,8))
# for i in t:
#     c=0
#     for v in i:
#         c=c+v
    # print(c)

# ************

# t=(('Ankit',78,90,34),('Tushar',32,30,34),('shyam',55,67,90),('peter',90,99,78))
# for i in t:
#     if(i[1]>=50):
#         print(i)

# *************

# t=(('Ankit',78,90,34),('Tushar',32,30,34),('shyam',55,67,90),('Alia',90,99,78))
# for i in t:
#     if(i[0].startswith('A')):
#         print(i[0])

# ************

# t1=(10,20,30,40)
# t2=(60,90,80,67)
# c=0
# for i in range(len(t1)):
#     c=t1[i]+t2[i]
#     print(c)

# ***************

t=(33,44,55,77,88,99)
for i,v in enumerate(t):
    print(i,v)