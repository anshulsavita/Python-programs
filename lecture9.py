# ******Methods of string****
# - capitalize() --> this function convert the string in title case. first letter of first word becomes uppercase.
# - title() --> convert each word in title case. first letter of every word becomes uppercase.
# - casefold() --> covert uppercase in lowercase.
# - lower() --> same....covert uppercase in lowercase.
# - (.) -->  member operator
# - upper() --> convert lowercase into uppercase
# - count(pattern/substring) --> count specified pattern
# - count(pattern,[si]) --> same....  starting index.. search pattern after specified index.
# - index(pattern,[si],[ei]) --> return the index of specified pattern.
# this function generate exception(error) when given pattern does not exist
# - find(pattern,[si],[ei]) --> same as index but will not generate exception if pattern does not exist it will return -1

# x="This is test program"
# t=x.capitalize() 
# t=x.title()
# t=x.casefold()
# t=x.upper()
# t=x.count('is')
# t=x.count('is',4)
# print(t)

# **************************
# x="the man the machine and the python"
# t=x.index('the')
# print(t)
# t=x.index('the',t+1)
# print(t)
# t=x.index('the',t+1)
# print(t)
# t=x.index('the',t+1)
# print(t)

# t=x.find('the')
# print(t)

# t=x.find('that')
# print(t)

# t=x.find ('ach',10,25)
# print(t)

# *******************
# i=0
# while(True):
#     i=x.find('the',i)
#     if(i==-1):break
#     print(i)
#     i+=1

# ******************
# **enter a name of three word (Ram kumar sharma) and find the middle name
# x="Hari Prasad Sharma"
# i=x.find(' ')
# j=x.find(' ',i+1)
# print(x[i+1:j])

# ******************
# **input a name of three word from user (Ram kumar sharma) and find the middle name
# x=input("Enter Name:")
# i=x.find(' ')
# j=x.find(' ',i+1)
# print(x[i+1:j])