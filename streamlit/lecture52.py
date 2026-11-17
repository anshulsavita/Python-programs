import streamlit as st
# st.video("https://youtu.be/jRsHojA-Zrg?si=fKUDeGFSUsRM7ubq")
# --------------------------------------

# This will print random images in virticul order
# st.image("https://picsum.photos/200",width=200)
# st.image("https://picsum.photos/201",width=200)
# st.image("https://picsum.photos/200",width=200)
# st.image("https://picsum.photos/201",width=200)

# This will print random images in Horizontal order
# col1,col2,col3,col4=st.columns(4)
# with col1:
#     st.image("https://picsum.photos/200",width=200)
# with col2:
#     st.image("https://picsum.photos/201",width=200)
# with col3:
#     st.image("https://picsum.photos/200",width=200)
# with col4:
#     st.image("https://picsum.photos/201",width=200)

# -------------------------------------------
# decorators and dialogs important topics

# This is like a login page 

# @st.dialog("Login Page")
# def myDialog():
#     email=st.text_input("Enter Email Id:")
#     pwd=st.text_input("Enter Password:",type="password")

# btn=st.button("Open Dialog")
# if(btn):
#     myDialog()

# ----------------------------------------------------

# @st.dialog("Confirmation")
# def myDialog():
#     email=st.warning("Are u sure to delete the current recor:")
#     col1,col2=st.columns(2)
#     with col1:
#         confirm=st.button("Confirm")
#     with col2:
#         confirm=st.button("Cancel")

# btn=st.button("Open Dialog")
# if(btn):
#     myDialog()
