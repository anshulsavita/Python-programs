# Lecture 53***
import streamlit as st
import database as DB # this is a module made by user

# formate function bolta hai ki tume kya dikhana hai options me se, option me hamare pass multiple dict ki lists hai
# on_change on line 20 is called as event
# fillSubCategory is a function
# on line 20 we assign a name to selectbox using key='category'. key will automatically become variable of session
# sessions are predefined, 
# sessions dict hai jisme categoryi key hai or values jo ham select karenge voh uski vales as a dict aayegi for example hamne select kiya Dairy Products so session hoga {'category': {'categoryid': 2, 'categoryname': 'Dairy Products'}}.

def fillSubCategory():
    cid=st.session_state['category']['categoryid']
    records=DB.getAllData(f"select * from subcategory where categoryid={cid}")
    st.session_state['SC']=records

records=DB.getAllData("select * from category")
st.selectbox('Categories',options=records,format_func=lambda x:x['categoryname'],on_change=fillSubCategory,key='category')

if('SC' not in st.session_state):
    st.session_state['SC']=[]
    SC=st.session_state['SC']
else:
    SC=st.session_state['SC']

st.selectbox("Subcategory",options=SC,format_func=lambda x:x['subcategoryname'])