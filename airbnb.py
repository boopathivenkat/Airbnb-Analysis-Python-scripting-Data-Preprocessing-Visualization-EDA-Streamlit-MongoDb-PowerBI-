import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import os

st.set_page_config(layout="wide")    
selected = option_menu("", ['Home','Data','Contact Us'],default_index=0,orientation="horizontal")

if selected == "Home":         
    st.title("*:green[Welcome] :violet[to] :red[Boopathi's] :grey[Airbnb]:blue[ Analysis]* :sunglasses: ") 
    st.markdown("***Vacation rental American company***")  
    st.divider()
    coll1, coll2 = st.columns(2)
    coll3, coll4 = st.columns(2)
    coll5, coll6 = st.columns(2)

    
    with coll1: 
        st.subheader("""***Airbnb is an American San Francisco-based company operating an online marketplace for short- and long-term homestays and experiences. The company acts as a broker and charges a commission from each booking. The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia.***""")
        st.divider()
        
    with coll2: 
        st.image('C:/Airbnb/front.jpg',width=420)  
        st.caption("***Headquarters at 888 Brannan Street, in San Francisco, California, United States***")

    with coll3: 
        st.image("C:\Airbnb\logo.jpg",width=420)  
        st.caption("***Airbnb is a shortened version of its original name, AirBedandBreakfast.com***") 

    with coll4: 
        st.subheader("""***The company is credited with revolutionizing the tourism industry, while also having been the subject of intense criticism by residents of tourism hotspot cities like Barcelona and Venice for enabling an unaffordable increase in home rents,and for a lack of regulation***""")
        st.divider()
        
    with coll5:      
  
        st.subheader("***Lodging, Hospitality, Homestay, Travel Industry, Property management and Tourism***")
        st.subheader("***Number of employees- 6,907 (2023) Revenue	(Decrease) US$5.99 billion (2023)***")
        
    with coll6:         
        st.image("C:/Airbnb/dom.jpg",width=420) 
        st.caption("***Area served - Worldwide***")
    
      
        
   
    
        
elif selected=="Contact Us":
    
    st.title("Contact Us")
    
    coll1, coll2 = st.columns(2)

    with coll1: 
        st.subheader('Boopathi Venkatachalam :sunglasses:')
        st.caption('Mobile:- 9751959575, E-Mail - boopathi762000@gmail.com')

        st.caption(":red[Note: * fill all mandatory fields]")     
        Name = st.text_input("Name*")
        Mobile = st.text_input("Mobile*")
        Email = st.text_input("Email*")
        Message = st.text_area("Message (optional)")
        
        if st.button("Submit"):
            st.success('''Thank you for your Message, We will get back to you soon''')
    
    with coll2:
        st.image('photo.jpg')
        st.link_button("Git Hub", "https://streamlit.io/gallery")

  
    st.subheader('Airbnb Data Visualisation')

    st.markdown('''The goal of this project is to extract data from the Phonepe pulse Github repository,
                 transform and clean the data,insert it into a MySQL database, and create a live geo visualization dashboard using Streamlit and Plotly in Python.
                 The dashboard will display the data in an interactive and visually appealing manner, with atleast 10 different dropdown options for users to select differentfacts and figures to display.
                 The solution must be secure, efficient,and user-friendly,providing valuable insights and informationabout the data in the Phonepe pulse Github repository.''')
    
    