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
col1,col2=st.columns(2)
with col1:
    st.selectbox('Categories',options=records,format_func=lambda x:x['categoryname'],on_change=fillSubCategory,key='category')
with col2:
    st.selectbox("Subcategory",options=SC,format_func=lambda x:x['subcategoryname'],key='subcategory')

pn=st.text_input("Enter Product Name.")
col1,col2,col3=st.columns(3)
with col1:
    pr=st.text_input("Enter Product Rate.")
with col2:
    op=st.text_input("Enter Product offer Price.") 
with col3:
    stk=st.text_input("Enter Product stock.")

col1,col2=st.columns(2)
with col1:
    pic=st.file_uploader("Product Picture",type=['jpg','png'])
with col2:
    if(pic):
        st.image(pic,width=130)

col1,col2=st.columns(2)
with col1:
    btn_submit=st.button("Submit")
with col2:
    btn_reset=st.button("Reset")

if(btn_submit):
    q=f"insert into products(categoryid, subcategoryid, productname, productrate, offerprice, stock, picture) values({st.session_state['category']['categoryid']},{st.session_state['subcategory']['subcategoryid']},'{pn}',{pr},{op},{stk},'{pic.name}')"
    print(q)
    response=DB.saveRecord(q)
    if(response['status']):
        st.success(response['msg'])
    else:
        st.error(response['msg'])