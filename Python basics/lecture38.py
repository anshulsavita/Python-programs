# ************player summary************
# players={0:{"name":'Abhishek Sharma',"Runs":[0,0,0,0,0,0]},
#          1:{"name":'Shubman Gill',"Runs":[0,0,0,0,0,0]}}
# current_p=0
# p1=0
# p2=0
# for i in range(1,13):
#     k=int(input(f"{players[current_p]['name']} is playing Ball {i}:"))
#     if(current_p==0):
#         p1=p1+k
#     else:
#         p2=p2+k
#     if(k==0):
#         players[current_p]['Runs'][0]+=1
#     elif(k==1):
#         players[current_p]['Runs'][1]+=1
#         if(current_p==0):
#             current_p=1
#         else:
#             current_p=0
#         print("Player changed...!")
#     elif(k==2):
#         players[current_p]['Runs'][2]+=1
#     elif(k==3):
#         players[current_p]['Runs'][3]+=1
#         if(current_p==0):
#             current_p=1
#         else:
#             current_p=0
#         print("Player changed...!")
#     elif(k==4):
#         players[current_p]['Runs'][4]+=1
#     elif(k==6):
#         players[current_p]['Runs'][5]+=1
#     if(i==6):
#         if(current_p==0):
#             current_p=1     
#         elif(current_p==1):
#             current_p=0
#         print("Over change.....")
#         print("Player changed...!")

# print(players)
# print(f"Abhishek Sharma's total runs: {p1}\nShubman Gill total runs: {p2}")


# create dict in python for flight details.. keys are flightid, flight type, source,destination,duration,fare,days in list,flight complany

flights = [
    {
        "flightid": "AI101",
        "flight_type": "Domestic",
        "source": "Delhi",
        "destination": "Mumbai",
        "duration": "2h 15m",
        "fare": 5500,
        "days": ["Monday", "Wednesday", "Friday"],
        "flight_company": "Air India"
    },
    {
        "flightid": "6E202",
        "flight_type": "Domestic",
        "source": "Bhopal",
        "destination": "Delhi",
        "duration": "1h 30m",
        "fare": 3500,
        "days": ["Tuesday", "Thursday", "Saturday"],
        "flight_company": "IndiGo"
    },
    {
        "flightid": "UK303",
        "flight_type": "Domestic",
        "source": "Mumbai",
        "destination": "Bangalore",
        "duration": "1h 45m",
        "fare": 4200,
        "days": ["Monday", "Tuesday", "Friday"],
        "flight_company": "Vistara"
    },
    {
        "flightid": "AI404",
        "flight_type": "International",
        "source": "Delhi",
        "destination": "Dubai",
        "duration": "3h 30m",
        "fare": 12000,
        "days": ["Wednesday", "Friday", "Sunday"],
        "flight_company": "Air India"
    },
    {
        "flightid": "6E505",
        "flight_type": "Domestic",
        "source": "Kolkata",
        "destination": "Chennai",
        "duration": "2h 30m",
        "fare": 6000,
        "days": ["Monday", "Thursday", "Saturday"],
        "flight_company": "IndiGo"
    }
]

# ******************************
# ---input source and destination and print available flights
# k1=input("Enter source:")
# k2=input("Enter Destination:")
# for i in range(len(flights)):
#     if(flights[i]['source']==k1 and flights[i]['destination']==k2):
#         print(flights[i])

#   ----------or--------------
# k1=input("Enter source:")
# k2=input("Enter Destination:")
# k=list(filter(lambda i: i['source']==k1 and i['destination']==k2,flights))

# if(any(k)==True):
#     print(k)
# else:
#     print("Flight nots found...")

# ******************************
# ---input source, destination, Date and print available flights
# k1=input("Enter source:")
# k2=input("Enter Destination:")
# day=input("Enter Day:")
# k=False
# for i in range(len(flights)):
#     if(flights[i]['source']==k1 and flights[i]['destination']==k2 and day in flights[i]['days']):
#         print(flights[i])
#         k=True
# if(k==False):
#     print("Flight not found...")

#   ---------------or-------------
# k1=input("Enter source:")
# k2=input("Enter Destination:")
# day=input("Enter Day:")

# k=list(filter(lambda i: i['source']==k1 and i['destination']==k2 and day in i['days'],flights))

# if(any(k)==True):
#     print(k)
# else:
#     print("Flight nots found...")

# ******************************
# ---input source, destination, min and max price and find available flights.
# k1=input("Enter source:")
# k2=input("Enter Destination:")
# min=int(input("Enter Minimum price:"))
# max=int(input("Enter Maximum price:"))

# k=False
# for i in range(len(flights)):
#     if(flights[i]['source']==k1 and flights[i]['destination']==k2 and (flights[i]['fare']>=min and flights[i]['fare']<=max)):
#         print(flights[i])
#         k=True
# if(k==False):
#     print("Flight not found...")

#  ----------or------------
# k1=input("Enter source:")
# k2=input("Enter Destination:")
# min=int(input("Enter Minimum price:"))
# max=int(input("Enter Maximum price:"))
# k=list(filter(lambda i: i['source']==k1 and i['destination']==k2 and (i['fare']>=min and i['fare']<=max),flights))

# if(any(k)==True):
#     print(k)
# else:
#     print("Flight nots found...")

# ******************************
# ---input source, destination, flight company and find available flights.
# k1=input("Enter source:")
# k2=input("Enter Destination:")
# flight_company=input("Enter Flight Company:")
# k=list(filter(lambda i: i['source']==k1 and i['destination']==k2 and flight_company in i['flight_company'],flights))
# if(any(k)==True):
#     print(k)
# else:
#     print("Flights not found...")

# ******************************
# ---give 10% discount on each flight..
k=list(map(lambda i: i.setdefault('Discount',i['fare']-i['fare']*0.10),flights))
print(flights)
