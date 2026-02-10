import streamlit as st
import pandas as pd
data={
    "name":["vinod","haha","hee"],
    "age":[10,20,40]
}
#st.write(data)
st.table(data)

#used data frame to create table
df=pd.DataFrame(data)
st.dataframe(df)
#table edit
st.data_editor(df)

#visualizartion
#line chart
st.line_chart(df,x="name",y="age")

#barchart
st.bar_chart(df,x="name",y="age")