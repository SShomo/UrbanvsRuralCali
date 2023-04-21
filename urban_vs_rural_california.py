import pandas as pd
import altair as alt
import streamlit as st

data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

st.set_page_config(page_title="Urban vs Rural California", initial_sidebar_state = 'collapsed', layout = 'wide')

#Can we scroll? Controls
#Input boxes/Buttons
#What does your layout look like?

#Where is my daata [Github, Streamlit, Browser]
#Sessions as part of interactivity
#streamlit layouts and containers, look it up


tab1, tab2, tab3 = st.tabs(["About", "Urban", "Rural"])

with tab1:
  with st.container():
    st.image('https://cdn.cookielaw.org/logos/abdd0205-22cc-4fe3-9905-15c572527293/7556293c-5b79-4ada-b220-2a9a79bf5b49/be7ee31a-0ca2-4aeb-894e-ee0219934cbe/okcupid_whitebg.png')
  with st.container():
    st.markdown(""" <style> .big-font { font-size:64px !important } </style> """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">.  Research Question !!</p>', unsafe_allow_html=True)
with tab2:
  with st.container():
    st.image('https://cdn.cookielaw.org/logos/abdd0205-22cc-4fe3-9905-15c572527293/7556293c-5b79-4ada-b220-2a9a79bf5b49/be7ee31a-0ca2-4aeb-894e-ee0219934cbe/okcupid_whitebg.png')
    col1, col2 = st.columns(2)
    with col1:
      st.write('visualization')
      #with st.containter():
        #st.write("Words")
    with col2:
      st.write= ('visualization')
  
  with st.container():
    pass
    #st.write('visualization')

with tab3:
  with st.container():
    st.image('https://cdn.cookielaw.org/logos/abdd0205-22cc-4fe3-9905-15c572527293/7556293c-5b79-4ada-b220-2a9a79bf5b49/be7ee31a-0ca2-4aeb-894e-ee0219934cbe/okcupid_whitebg.png')


col1, col2, col3 = st.columns(3)

#Make a sidebar
with st.sidebar:
  st.header("This is a sidebar")
#Make three charts
