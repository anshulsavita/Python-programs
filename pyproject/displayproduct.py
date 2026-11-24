import streamlit as st
import database1 as DB
records=DB.getAllData("Select category.categoryname,subcategory.subcategoryname,products.* from products,category,subcategory where category.categoryid=products.categoryid and subcategory.subcategoryid=products.subcategoryid")
for rec in records:
    pbtn=st.button('Edit',key=f"{rec['productid']}")
    rec['Edit']=pbtn

col1,col2=st.columns(2)
with col1:
    txt=st.text_input("Search:")
with col2:
    btn=st.button("Search")
if(btn):
    records=DB.getAllData(f"Select category.categoryname,subcategory.subcategoryname,products.* from products,category,subcategory where category.categoryid=products.categoryid and subcategory.subcategoryid=products.subcategoryid and products.productname like '%{txt}%'")

st.dataframe(records)
