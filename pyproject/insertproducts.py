import streamlit as st
import database as DB # this is a module made by user

records=DB.getAllData("select * from category")
CL=[]
for record in records:
    CL.append(list(record.values())[1])
print(CL)
st.selectbox('Categories',CL)