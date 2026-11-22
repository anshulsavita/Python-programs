import streamlit as st
import dataBase as DB

st.markdown(
    "<h1 style='text-align: center;'>Insert Food Details!</h1>",
    unsafe_allow_html=True
)


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
    st.selectbox('Subcategories',options=SC,format_func=lambda x:x['subcategoryname'],key='subcategory')

# ----------------------------------------------------------
col1,col2=st.columns(2)
with col1:
    ft=st.text_input("Enter Food item.")
with col2:
    f_in=st.text_input("Enter Food ingredients.")

# ---------------------------------------------------------
col1,col2,col3=st.columns(3)
with col1:
    fr=st.text_input("Enter Food Rate.")
with col2:
    op=st.text_input("Enter Offer price.")
with col3:
    ps=st.selectbox("Status",['-Select-','Available','Not Available'])
# ----------------------------------------------------------

col1,col2=st.columns(2)
with col1:
    pic=st.file_uploader("Food Picture",type=['jpg','png'])
with col2:
    if(pic):
        st.image(pic,width=130)

# ----------------------------------------------------------
col1,col2=st.columns(2)
with col1:
    btn_submit=st.button("Submit")
with col2:
    btn_reset=st.button("Reset")

if(btn_submit):
    q=f"insert into fooditems(categoryid, subcategoryid, fooditem, rate, offer, ingredients, status, picture) values({st.session_state['category']['categoryid']},{st.session_state['subcategory']['subcategoryid']},'{ft}',{fr},{op},'{f_in}','{ps}','{pic.name}')"
    response=DB.saveRecord(q)
    if(response['status']):
        st.success(response['msg'])
    else:
        st.error(response['msg'])