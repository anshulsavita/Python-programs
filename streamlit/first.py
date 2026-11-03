import streamlit as st
# st.title("Machine Learning App")
# st.header("Supervised Learning")
# st.subheader("Linear Regression")
# st.text("Hello Students")
# st.write("Hi students")
# st.error("There is error in code...pls contact with admin")
# st.warning("pls input integer only")
# st.info("Input FirstName Middlename & Lastname")
# st.success("Record Found Successfully")

# ------------------------------------------------------------------

# flights = [
#     {
#         "flightid": 101,
#         "flightname": "AI-101",
#         "source": "Delhi",
#         "destination": "Mumbai",
#         "time_arrival": "10:30 AM",
#         "time_departure": "08:00 AM",
#         "days": ["Monday", "Wednesday", "Friday"],
#         "companyname": "Air India"
#     },
#     {
#         "flightid": 102,
#         "flightname": "6E-202",
#         "source": "Mumbai",
#         "destination": "Bangalore",
#         "time_arrival": "02:00 PM",
#         "time_departure": "12:00 PM",
#         "days": ["Tuesday", "Thursday", "Saturday"],
#         "companyname": "IndiGo"
#     },
#     {
#         "flightid": 103,
#         "flightname": "UK-303",
#         "source": "Delhi",
#         "destination": "Chennai",
#         "time_arrival": "06:00 PM",
#         "time_departure": "03:30 PM",
#         "days": ["Monday", "Tuesday", "Friday"],
#         "companyname": "Vistara"
#     },
#     {
#         "flightid": 104,
#         "flightname": "SG-404",
#         "source": "Kolkata",
#         "destination": "Delhi",
#         "time_arrival": "11:00 AM",
#         "time_departure": "08:30 AM",
#         "days": ["Wednesday", "Thursday", "Sunday"],
#         "companyname": "SpiceJet"
#     },
#     {
#         "flightid": 105,
#         "flightname": "AI-505",
#         "source": "Bangalore",
#         "destination": "Hyderabad",
#         "time_arrival": "04:30 PM",
#         "time_departure": "03:00 PM",
#         "days": ["Monday", "Friday", "Saturday"],
#         "companyname": "Air India"
#     },
#     {
#         "flightid": 106,
#         "flightname": "6E-606",
#         "source": "Mumbai",
#         "destination": "Goa",
#         "time_arrival": "01:00 PM",
#         "time_departure": "11:30 AM",
#         "days": ["Tuesday", "Wednesday", "Sunday"],
#         "companyname": "IndiGo"
#     },
#     {
#         "flightid": 107,
#         "flightname": "IX-707",
#         "source": "Delhi",
#         "destination": "Jaipur",
#         "time_arrival": "09:00 AM",
#         "time_departure": "07:45 AM",
#         "days": ["Monday", "Thursday", "Saturday"],
#         "companyname": "Air India Express"
#     },
#     {
#         "flightid": 108,
#         "flightname": "QP-808",
#         "source": "Hyderabad",
#         "destination": "Pune",
#         "time_arrival": "07:00 PM",
#         "time_departure": "05:30 PM",
#         "days": ["Tuesday", "Friday", "Sunday"],
#         "companyname": "Akasa Air"
#     },
#     {
#         "flightid": 109,
#         "flightname": "6E-909",
#         "source": "Chennai",
#         "destination": "Kolkata",
#         "time_arrival": "03:30 PM",
#         "time_departure": "01:00 PM",
#         "days": ["Wednesday", "Friday", "Saturday"],
#         "companyname": "IndiGo"
#     },
#     {
#         "flightid": 110,
#         "flightname": "AI-110",
#         "source": "Ahmedabad",
#         "destination": "Delhi",
#         "time_arrival": "08:00 PM",
#         "time_departure": "06:15 PM",
#         "days": ["Monday", "Tuesday", "Sunday"],
#         "companyname": "Air India"
#     }
# ]
# st.dataframe(flights)
# st.table(flights)

# ----------------------------------------------------------------

amount=st.number_input(label="Enter Amount:",help="Enter Amount in $",placeholder="Enter Amount Here..")
rate=st.number_input(label="Enter rate:",help="Enter Rate in %",placeholder="Enter Rate Here..")
time=st.number_input(label="Enter time:",help="Enter Time in Year",placeholder="Enter Time Here..")

btn=st.button(label="Click Here")
if(btn):
    ia=(amount*rate*time)/100
    st.success(f"Interest amount:{ia}")