import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv("us_vehicles.csv")

st.header('Car data in the US')

hist_checkbox = st.checkbox('Build histogram')
disp_checkbox = st.checkbox('Build distribution')

button = st.button('Build plot') # crear un botón

if hist_checkbox and button: # when the button is clicked
    # write a message
    st.write('Creation of a histogram of the car sales dataset')
    
    # create histogram
    
    fig = px.histogram(car_data, x="odometer")
    
    # show interactive Plotly graph
    
    st.plotly_chart(fig, use_container_width=True) 

if disp_checkbox and button: # when the button is clicked
    # write a message
    st.write('Creation of a scatter graph of the car sales dataset')
    
    # create scatter
    
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    
    # show interactive Plotly graph
    
    st.plotly_chart(fig, use_container_width=True) 

