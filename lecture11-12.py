# x="12#78#79#90#34"
# L=x.split("#")
# print(L)
# s=0
# for v in L:
#     s=s+int(v)
# print(s)

# x="Gwalior,Indore,Bhopal,Jabalpur"
# L=x.split(",",1)
# print(L)

# ******methods of string***

# rsplit(substr,[n]) --> This function split the string into multiple parts in reverse direction and remove that substring. n is number of split 
# partition(substr) --> when we perform partition it becomes three parts according to specified substring, one go in left, one go in right and one in middle.
# strip([pattern]) --> remove leading and trailing spaces or any pattern (aage or peeche), default spaces.
# lstrip([pattern]) --> remove from left side.
# rstrip([pattern]) --> remove from right side.
# ljust(width,[pattern]) -->increse width and left justify the string and we get pattern in remaining area(default space).
# center(total space,[pattern]) --> pattern comes in center of total space.
# isalpha() -->
# istitle()-->
# isspace()-->
# islower()-->
# isupper()-->
# isalnum()-->
# isdigit()-->

# x="Gwalior,Indore,Bhopal,Jabalpur"
# L=x.rsplit(",",1)
# print(L)

# x="Vikas Vivek Vinod pankaj mohan"
# L=x.partition("Vinod")
# print(L)

# x="     Vikas    "
# print(x)
# L=x.strip()
# print(L)

# x="#######Vikas########"
# print(x)
# L=x.strip('#')
# print(L)

# x="#######Vikas########"
# print(x)
# L=x.rstrip('#')
# print(L)

# x="AGRA"
# T=x.ljust(10,'#')
# print(T)

# x="9391123085"
# T=x[:2].ljust(10,"#")
# print(T)

# x="PS-SOFTECH"
# T=x.center(20,"#")
# print(T)

# x="Gwalior"
# print(x.isalpha())


# x="Gwalior7"
# print(x.isalpha())
# print(x.istitle())

# x="      "
# print(x.isspace()) # sare space hone chaiye

# x="gwalior"
# print(x.islower())
# print(x.isupper())
# print(x.isalnum()) #aplhabet and numeric.

# x="888888"
# print(x.isdigit())

x="Gwalior7"
for c in x:
    if(c.isalpha()):
        print(c,"is alpha")
    elif(c.isdigit()):
        print(c,'is digit')

