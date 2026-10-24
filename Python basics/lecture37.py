# reduce(function,sequence,[initial value])
import functools as ft
# l=[10,50,40,20,80]
# k=ft.reduce(lambda a,b:a+b,l)
# print(k)

# **********************
# l=[10,50,40,20,80]
# k=ft.reduce(lambda a,b:a+b,l,100)
# print(k)

# *************************
# l=[['pepsi',100,60],['Fanta',80,40],['coke',200,70]]
# k=ft.reduce(lambda a,b: a+b[1],l,0)
# j=ft.reduce(lambda a,b: a+b[2],l,0)
# print("Total:",k)
# print("Amount to pay:",j)
# s=k-j
# print("save:",s)

# ***************************
# l=[['pepsi',100,60],['Fanta',80,0],['coke',200,70],['Red Bull',200,0],['7up',120,50]]
# k=list(filter(lambda a:a[2]==0,l))
# print(k)

# ************************
L=[
    {"product_id": 101, "product": "Laptop", "product_price": 65000, "sale_price": 59999, "gender": "Male"},
    {"product_id": 102, "product": "Mobile Phone", "product_price": 30000, "sale_price": 27999, "gender": "Female"},
    {"product_id": 103, "product": "Headphones", "product_price": 5000, "sale_price": 3999, "gender": "Male"},
    {"product_id": 104, "product": "Smart Watch", "product_price": 8000, "sale_price": 6499, "gender": "Female"},
    {"product_id": 105, "product": "Tablet", "product_price": 25000, "sale_price": 21999, "gender": "Male"},
    {"product_id": 106, "product": "Keyboard", "product_price": 2500, "sale_price": 1999, "gender": "Female"},
    {"product_id": 107, "product": "Mouse", "product_price": 1500, "sale_price": 1199, "gender": "Male"}]
male=list(filter(lambda a: a['gender']=='Male',L))
female=list(filter(lambda a: a['gender']=='Female',L))
male_p=len(male)/len(L)*100
female_p=len(female)/len(L)*100
print("Total Male:",len(male),"percentage:",male_p)
print("Total Male:",len(female),"percentage:",female_p)
