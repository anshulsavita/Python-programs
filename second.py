# *****input statement--> use to input string only
# <var name>=input("msg")
# ***
# rate =input("Enter rate:")
# qty=input("Enter Quantity:")
# amt=rate*qty
# printf(amt)

# *****parsing method
# rate =float(input("Enter rate:"))
# qty=float(input("Enter Quantity:"))
# amt=rate*qty
# print(amt)

# x=66
# y="km"
# z=str(x)+y
# print(z)

# ****Single if condition--->
#syntax-->
# if():
#   =====
#   =====
# else:
#   ====
#   ====

# rate =float(input("Enter rate:"))
# qty=float(input("Enter Quantity:"))
# amt=rate*qty
# print(amt)
# if(amt>=100000):
#     dis=20
# else:
#     dis=10
# dis_amt=amt*dis/100
# print("Discount:",dis,"%")
# print("Discount Amount:",dis_amt)
# na=amt-dis_amt
# print("Net Amount:",na)


# ******multiple if
# if(exp):
#     =====
#     =====
# elif(exp):
#     ====
#     ====
# else:
#     ====
#     ====

# salary=float(input("Enter salary:"))
# if(salary>=200000 and salary<=300000):
#     da=salary*30/100
#     pf=salary*12/100
#     hra=salary*7/100
#     print("Da:",da,"Hra:",hra,"Pf:",pf)

# elif(salary>100000 and salary<=199999):
#     da=salary*25/100
#     pf=salary*12/100
#     hra=salary*5/100
#     print("Da:",da,"Hra:",hra,"Pf:",pf)

# elif(salary>=50000 and salary<=99999):
#     da=salary*20/100
#     pf=salary*12/100
#     hra=salary*3/100
#     print("Da:",da,"Hra:",hra,"Pf:",pf)

# else:
#     print("Invalid salary....")

# Input current reading and previous reading and find out total reading
cr=float(input("Enter current reading:"))
pr=float(input("Enter previous reading:"))
tr=cr-pr
print("Total Reading:",tr)
if(tr>=1000):
    c=13
    
elif(tr>=500 and tr<=999):
    c=10
  
elif(tr>=0 and tr<=499):
    c=5

print("Charge per unit:",c)
t_amt =tr*c
print("Total amount:",t_amt)
 

