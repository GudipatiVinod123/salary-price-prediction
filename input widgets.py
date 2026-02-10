import streamlit as st
from datetime import datetime
st.title("welcome to Streamlit")
st.button("Submit kottu bey")
st.checkbox("Agree kottu mawa")

#selecting male and female use radio
gender=st.radio("Select Gender",["Male","Female","Others"])
st.write("You Entered :",gender)

#selecting Box
#for selecting one skill
st.selectbox("choose your Skills",["python","c","java"])

#selecting multiple skills
st.multiselect("choose your skills",["python","django","vinod","flashman"])

#slider
st.slider("volume:",min_value=0,max_value=100,value=1)

#enter name text
st.text_input("Enter your name")
#number input
st.number_input("Enter phone number")
#enter data of birth
st.date_input("Date", datetime.today())

#files upload here
st.file_uploader("upload resume here")

#take a photo 
#st.camera_input("take photo")
#audio record
voice=st.audio_input("click to record")
#display audio for listen
st.audio(voice)
#image
#st.image()
#video link
#st.video("https://www.youtube.com/watch?v=3A3o60xNkfQ")

