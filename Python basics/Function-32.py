# **********Function*********
# - use to divide a large program in a small module.
# - one can call function anytime anywhere in a program multiple times thus it provide reusability of code.
# - syntax
# -called functions -->
# def <function name>(args):
#     ====
#     =====
#     return 0

# def add(a,b): # called fn
#     c=a+b
#     return c

# k=add(100,500) #calling fn
# j=add(89,67)
# print(k,j)

# ********************
# def si(p,r,t):
#     c=p*r*t/100
#     return c

# k=si(5,7,8)
# print(k)

# ********************
# call by values-->
# def factorial(n):
#     f=1
#     while(n>1):
#         f=f*n
#         n-=1
#     return f

# k=factorial(4)
# print(k)

# **********************
# call by refrence --> Actual args copied their address in formal args.
# def call(l): # called(formal)
#     l[2]=l[2]+3000

# x=[1,2,3,4,5]
# call(x) # calling(actual)
# print(x)

# ********************
# def add_tags(tag,text):
#     t=f"<{tag}>{text}</{tag}>"
#     return t

# k=add_tags('i','softech')
# print(k)

# ***********************
def insert_string_middle(text,tag):
    t=f"{tag[:1]}{text}{tag[1:]}"
    return t

k=insert_string_middle('softech','[]')
print(k)