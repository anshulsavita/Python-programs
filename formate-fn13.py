# *******methods of string***
# isspace() --> 
# isdecimal() --> it is same as digit.
# isnumeric() --> it is same as digit.
# "pattern".join(collection) --> join each element of collection with give pattern.

# escape sequence
# \n      new line
# \t      tab space
# \b      backspace
# \r      enter key
# \\      print \
# \"      print "
# \'      print '

# conversion specifier
# %d      int
# %f      float
# %s      string
# %r      raw

# ****format function****
# syntax -->
# "".format(var list) -->

# a=100
# b=300
# c=20
# d=a+b+c
# k="{0},{1},{2},{3},{0},{3}".format(a,b,c,d)  
# #value of a in 0, b in 1, c in 2 and d in 3. we can use data for multiple times like shown in example.
# print(k)

# a=100
# b=3000
# c=20
# d=a+b+c
# k="{0:10.2f}\n{1:10.2f}\n{2:10.2f}\n------------\n{3:10.2f}".format(a,b,c,d) #value automatic right justify 
# print(k)

# 0 represents index
# 10 represents width
# .2f represents number of decimals and float.
# > represents right justify always after colon(:)
# < represents left justify
# ^ represents mid justify

# ******using conversion specifier**********
a=100
b=3000
c=20
d=a+b+c
k="%10.2f\n%10.2f\n%10.2f\n---------\n%10.2f"%(a,b,c,d)
print(k)

# - represents left justify in --> 
# k="%-10.2f\n%-10.2f\n%-10.2f\n---------\n%-10.2f"%(a,b,c,d)

# *************
# ***Quition --> print It was dark time 12:30 Am, I had 2000 $ in my pocket.
# time = "12:30"
# money = 2000
# k="it was dark time {0} AM, i had {1:.2f}$ in my pocket".format(time,money)
# print(k)

# k= "Its was dark time %s AM, i had %.2f $ in my pocket"%(time,money)
# print(k)

# *******or********
# k=f"It was dark time {time} AM, i had {money:.2f}$ in my pocket."
# print(k)

# **************
# ****join-->
# "pattern".join(collection) --> join each element of collection with give pattern.
# x=['m','a','n','d','e','e','p']
# k=''.join(x)
# print(k)
# k='@'.join(x)
# print(k)
