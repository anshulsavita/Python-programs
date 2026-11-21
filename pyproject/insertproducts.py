# Lecture 53***
import streamlit as st
import database as DB 

def fillSubCategory():
    cid=st.session_state['category']['categoryid']
    records=DB.getAllData(f"select * from subcategory where categoryid={cid}")
    st.session_state['SC']=records

if('SC' not in st.session_state):
    st.session_state['SC']=[]
    SC=st.session_state['SC']
else:
    SC=st.session_state['SC']

records=DB.getAllData("select * from category")
st.selectbox('Categories',options=records,format_func=lambda x:x['categoryname'],on_change=fillSubCategory,key='category')
st.selectbox("Subcategory",options=SC,format_func=lambda x:x['subcategoryname'])