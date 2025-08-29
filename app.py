import streamlit as st
import pandas as pd
import pickle as pk


st.title("Cab Price Prediction")


url = 'https://images.moneycontrol.com/static-mcnews/2024/02/Cab-Fare-increase.jpg'

st.image(url)
st.divider()

st.sidebar.title("Taxi Booking")
st.sidebar.image("https://img.freepik.com/free-vector/checkered-circle-taxi-frame_78370-3172.jpg?semt=ais_hybrid&w=740&q=80")



ride_distance = st.sidebar.slider(
    "Enter the Ride Distance (in km)",
    0,100,1
)

dr_rating = st.sidebar.slider(
    "Enter the Driver's Rating (1 to 5)",
    1,5,1
)

cst_rating = st.sidebar.slider(
    "Enter the Customer's Rating (1 to 5)",
    1,5,1
)

vtat = st.sidebar.slider(
    "Average VTAT (Value Added Tax)",
    0,100,1
)



ctat = st.sidebar.slider(
    "Average CTAT",
    0,100,1
)





# ["Delhi","Evening","three","Evening","Mumbai","Economy",23.8,39]

to_predict=[ride_distance,dr_rating,cst_rating,vtat,ctat]
column_data =['Ride Distance', 'Driver Ratings', 'Customer Rating', 'Avg VTAT','Avg CTAT']

# st.write(to_predict)
my_dict = {}
for i in range(5):
    my_dict[column_data[i]] = to_predict[i]


    
st.dataframe(my_dict)


f=open('cab_model.pkl','rb')
chatGPT = pk.load(f)
result = round(chatGPT.predict([to_predict])[0],1)



to_write=f"Estimated Ticket Cost: {result} Rs."
st.markdown(
    "<h3 style='font-size:50px;'>"+to_write+"</h3>", 
    unsafe_allow_html=True
)
