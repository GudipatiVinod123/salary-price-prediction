import streamlit as st
# used for title
st.title("This is Welcome Streamlit")
#header
st.header("Welcome to my page")
#subheader
st.subheader("what do you want")
#text
st.text("my self nn and my degree in Be")
# give ** is Bold and give * is italic
st.markdown("*vinod*") #italic
st.markdown("**vinod**") #Bold

# code
st.code(["s = int(input('Enter the number'))"], language="python")
st.code(["s=int(input('Enter the name'))"],language="c")  

#latex used to write formulas
st.latex("2^2=4")

#caption
st.divider()
st.caption("Hey bets")
#Divider
st.divider()
#write is used to print output
st.write("Machine")

