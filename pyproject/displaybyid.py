import streamlit as st
import database1 as DB

pid=st.text_input("Enter Product Id:")
btn=st.button("Search")
if(btn):
    record=DB.getById(f"Select category.categoryname,subcategory.subcategoryname,products.* from products,category,subcategory where category.categoryid=products.categoryid and subcategory.subcategoryid=products.subcategoryid and products.productid={pid}")
    if(record):
        st.success('Found')
    else:
        st.error('Not Found')