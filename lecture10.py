# ******methods of string*****
# rfind(pattern,[si],[ei]) --> search string in backward direstion
# replace(oldstr,new str,[n]) --> replace old str with new str, n is number of replacement.
# endswith(substr,[si],[ei]) --> return true if string end with specified substring
# startswith(substr,[si],[ei]) 
# split(substr,[n]) --> this function split the string into multiple parts according to specified substr and remove that substring. n is number of spli.

# x="the man the machine and the python"
# i=x.rfind('the')
# print(i)
# i=x.rfind('the',18) # 18 is a endpoint
# print(i)
# i=x.replace('the','that')
# print(i)
# i=x.replace('the','that',)
# print(i)

# x="the man the machine and the python"
# i=x.replace('the','that',2)
# i=x.replace('that','the',1)
# print(i)

# x="Deepak Tiwari"
# k=x.endwith('tiwari')

# x=['Gwalior','Bhopal','Jabalpur','jaipur','Indor','Rampur','Ramgarh']
# for city in x:
#     if city.endswith('pur'):
#         print(city)

x="Bhopal,Indore,Jabalpur,Gwalior"
L=x.split(",")
print(L)
print(L[2])

# x="130,90,72,12-6-2025 5:30"
# L=x.split(",")
# print(L)
# T=L[3].split(' ') # default their is space split()
# print(T)
# print("BP: ",L[0],"/",L[1],sep='')
# print("Heart Rate:",L[2])
# print("Date:",T[0])
# print("Time:",T[1])
