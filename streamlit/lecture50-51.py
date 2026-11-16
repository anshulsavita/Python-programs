import streamlit as st
# python=st.checkbox("Python",value=True)
# java=st.checkbox("Java")
# cpp=st.checkbox("C++")
# if(python):
#     st.write("Python Fee 30000/-")
# if(java):
#     st.write("Java Fee 45000/-")
# if(cpp):
#     st.write("C++ Fee 5000/-")
# -------------------------------------------

# gen=st.radio("Gender",['Male','Female'])
# st.write(gen)

# ------------------------------------------

# States=st.selectbox("States",['-Select-','Madhya Pradesh','Uttar Pradesh','Haryana','Punjab'])
# st.write(States)

# -------------------------------------------
# States=st.multiselect("States",['-Select-','Madhya Pradesh','Uttar Pradesh','Haryana','Punjab'])
# st.write(States)

# --------------------------------------------

# file=st.file_uploader("Select Image",type=["jpg","png"])
# if(file):
#     st.image(file,use_container_width=True)

# ----------------------------------------------
# file=st.file_uploader("Select Image",type=["jpg","png"],accept_multiple_files=True)
# if(file):
#     st.image(file,use_container_width=False,width=100)

# ---------------------------------------------
# audio_file=open("streamlit/flute.mp3","rb")
# audio_bytes=audio_file.read()
# st.audio(audio_bytes,format="audio/mp3",start_time=0)

# ---------------------------------------------
# v_file=open("html/HTML Coaching/Travis.mp4","rb")
# v_bytes=v_file.read()
# st.video(v_bytes,format="video/mp4",start_time=0)

# ---------------------------------------------
file=st.file_uploader("select Video File",type=["mp4","mpeg"])
if(file):
    st.video(file.getvalue())
