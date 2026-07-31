# def add(l1,l2):
#     l3=[]
#     for i in range(len(l1)):
#         l3.append(l1[i]+l2[i])
#     return l3
# a=[1,2,3,4,5]
# b=[1,2,3,4,5]
# k=add(a,b)
# print(k)

# ***********lambda function*******
# - anonymous functions(function without name)
# - single line function 
# - syntax -->
#       lambda <parameters>:expression 

# k=lambda a,b:a+b
# c=k(10,20)
# print(c)

# k=lambda c:(c*9/5)+32
# a=k(25)
# print(a)

# k=lambda a,b: (b,a)
# a,b=k(10,20)
# print(a,b)

# ********comprehension if ******
# syntax -->
#           <true> if(exp) else <false>

# a=10
# z="positive" if(a>=0) else"Negative"
# print(z)

# *************
# m=54
# z="A" if(m>=80 and m<=100) else "B" if(m>=60 and m<=79) else "C" if(m>=40 and m<=59) else "D"
# print(z)

# ********comprehension for ******
# <var> for <var> in <collection>

# l=[3*i for i in range(1,11)]
# print(l)

# k=lambda n,a:list(i*n for i in a)
# l=[55,33,44,55,66]
# r=k(10,l)
# print(r)

# k=lambda n,a:list(i*n if(i<=50) else i*0 for i in a)
# l=[55,33,44,55,66]
# r=k(10,l)
# print(r)

# next map