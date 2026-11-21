import streamlit as st
import p_database as DB

def fillcities():
    sid=st.session_state['states']['stateid']
    records=DB.getAllData(f"select * from cities where stateid={sid}")
    st.session_state['city']=records

records=DB.getAllData("select * from states")
st.selectbox('states',options=records,format_func=lambda x:x['statename'],on_change=fillcities,key='states')

if('city' not in st.session_state):
    st.session_state['city']=[]
    city=st.session_state['city']
else:
    city=st.session_state['city']

st.selectbox("cities",options=city,format_func=lambda x:x['cityname'])