import pandas as pd
import altair as alt
import streamlit as st

data = pd.read_csv("https://raw.githubusercontent.com/SShomo/UrbanvsRuralCali/main/clean_cupid.csv.csv")

st.set_page_config(page_title="Urban vs Rural California", initial_sidebar_state = 'collapsed', layout = 'wide')

alt.data_transformers.disable_max_rows()

selection = alt.selection_multi(fields=['sex'], bind='legend')
interval = alt.selection_interval()
all_sex = data.sex.unique().tolist()

plot_df = data[data.sex.isin(all_sex)]

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


chart2 = alt.Chart(data).mark_bar().encode(
    x = 'location',
    y='count()',
     color=alt.condition(interval, 'sex', alt.value('lightgray')),
    tooltip = ['city_type', 'sex']
).add_selection(
    interval
).interactive()

chart3 = alt.Chart(data).mark_bar().encode(
    x='count()',
    y='religion',
    color='religion',
    tooltip=['religion', 'sex']
).transform_filter(
    interval
)

chart4 = chart2 & chart3


#Can we scroll? Controls
#Input boxes/Buttons
#What does your layout look like?

#Where is my daata [Github, Streamlit, Browser]
#Sessions as part of interactivity
#streamlit layouts and containers, look it up

#Selectboxes for multiple controls

tab1, tab2, tab3 = st.tabs(["About", "General Info", "Vocabulary"])

with tab1:
  with st.container():
    st.image('https://cdn.cookielaw.org/logos/abdd0205-22cc-4fe3-9905-15c572527293/7556293c-5b79-4ada-b220-2a9a79bf5b49/be7ee31a-0ca2-4aeb-894e-ee0219934cbe/okcupid_whitebg.png')
  with st.container():
    st.markdown(""" <style> .big-font { font-size:45px !important } </style> """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">  Do females have better vocabulary than males?</p>', unsafe_allow_html=True)
  with st.container():
    st.write("This project seeks to answer whether or not women have a better vocabulary than men. I go about this using the OKCupid dataset that was released in May 2016. The data was collected in between November 2014 to May 2015 by a group of Danish researchers. It is a very big dataset with around 59,000 rows of data. This was too much to work with so I did some major trimming of the dataset. The essay-type questions were split up into nine different categories, so I removed rows that had any unfilled essays in any of the nine categories and combined them all into a full essay category. For the religion column, I just wanted the user’s religion and not how they felt about it, so I split it in a way that only gives the religion. ")
    
    st.write("This dataset does have a fair bit of controversy, as you can imagine since the researchers had not asked OkCupid or the people whose data was scraped from the site. None of the participants had a say in whether or not they wanted their personal data to be released to the public. The researchers argued that since the data was already publicly available, they had the right to use it for their research. Originally, the dataset had usernames that could be traced back to people if they had used the same username on another site, but that has since been removed. ")
with tab2:
  with st.container():
    st.image('https://cdn.cookielaw.org/logos/abdd0205-22cc-4fe3-9905-15c572527293/7556293c-5b79-4ada-b220-2a9a79bf5b49/be7ee31a-0ca2-4aeb-894e-ee0219934cbe/okcupid_whitebg.png')
    col1, col2 = st.columns(2)
    with col1:
      st.header('Status of Availability')
      st.altair_chart(chart1, use_container_width = True)
      st.write("These are some general observations about the genders and their differences in the dataset. It should be kept in mind that there are about 1000 more male entries in the dataset than female. This gives us a better idea of what we are working with in terms of the research question.")
      st.image("https://media.istockphoto.com/id/1226975070/vector/heartbeat-heart-shape-centered-line-heart-beat-heartbeat-pulse-flat-vector-icon.jpg?s=170667a&w=0&k=20&c=Pe3H317bPhRr4Kybg4VYdHjZLvVmFaHmwqWna8YsWYE=")
    with col2:
      st.header('Religions and Gender in Cities')
      st.altair_chart(chart4, use_container_width = True)
    #with st.container():

with tab3:
    selected = st.multiselect(
    "Gender", options = all_sex, default = all_sex)
    with st.container():
      st.image('https://cdn.cookielaw.org/logos/abdd0205-22cc-4fe3-9905-15c572527293/7556293c-5b79-4ada-b220-2a9a79bf5b49/be7ee31a-0ca2-4aeb-894e-ee0219934cbe/okcupid_whitebg.png')
      col1, col2 = st.columns(2)
    with col1:
      st.header('Visualization')
      #st.write("This is a test")
    with col2:
      st.header('Visualization')
      st.write("This is a test")
  
    with st.container():
      st.header("Visualization")
      st.write("This is a test")
