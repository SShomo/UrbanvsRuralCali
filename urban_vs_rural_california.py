import pandas as pd
import altair as alt
import streamlit as st

data = pd.read_csv("https://raw.githubusercontent.com/SShomo/UrbanvsRuralCali/main/clean_cupid.csv.csv")

alt.data_transformers.disable_max_rows()
selection = alt.selection_multi(fields=['sex'], bind='legend')

chart1 = alt.Chart(data).mark_bar().encode(
    x= alt.X('count(sex):Q', title= 'Count'),
    y='sex:O',
    color='sex:N',
    row='status:N',
    tooltip = ['count(sex)'],
    opacity=alt.condition(selection, alt.value(1), alt.value(0.2))
).add_selection(
    selection
)

st.set_page_config(page_title="Urban vs Rural California", initial_sidebar_state = 'collapsed', layout = 'wide')

#Can we scroll? Controls
#Input boxes/Buttons
#What does your layout look like?

#Where is my daata [Github, Streamlit, Browser]
#Sessions as part of interactivity
#streamlit layouts and containers, look it up

#Selectboxes for multiple controls

tab1, tab2, tab3 = st.tabs(["About", "Urban", "Rural"])

with tab1:
  with st.container():
    st.image('https://cdn.cookielaw.org/logos/abdd0205-22cc-4fe3-9905-15c572527293/7556293c-5b79-4ada-b220-2a9a79bf5b49/be7ee31a-0ca2-4aeb-894e-ee0219934cbe/okcupid_whitebg.png')
  with st.container():
    st.markdown(""" <style> .big-font { font-size:45px !important } </style> """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">  Females have better vocabulary than males</p>', unsafe_allow_html=True)
  with st.container():
    st.write("This is a test")

with tab2:
  with st.container():
    st.image('https://cdn.cookielaw.org/logos/abdd0205-22cc-4fe3-9905-15c572527293/7556293c-5b79-4ada-b220-2a9a79bf5b49/be7ee31a-0ca2-4aeb-894e-ee0219934cbe/okcupid_whitebg.png')
    col1, col2 = st.columns(2)
    with col1:
      st.header('Visualization')
      st.altair_chart(chart1, use_container_width = True)
      st.write("This is a test")
    with col2:
      st.header('Visualization')
      st.write("This is a test")

  
    with st.container():
      st.header("Visualization")
      st.write("This is a test")

with tab3:
    with st.container():
      st.image('https://cdn.cookielaw.org/logos/abdd0205-22cc-4fe3-9905-15c572527293/7556293c-5b79-4ada-b220-2a9a79bf5b49/be7ee31a-0ca2-4aeb-894e-ee0219934cbe/okcupid_whitebg.png')
      col1, col2 = st.columns(2)
    with col1:
      st.header('Visualization')
      st.write("This is a test")
    with col2:
      st.header('Visualization')
      st.write("This is a test")
  
    with st.container():
      st.header("Visualization")
      st.write("This is a test")


with st.sidebar:
  st.header("This is a sidebar")
