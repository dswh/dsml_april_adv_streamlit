import pandas as pd
import streamlit as st
import datetime
import pickle


st.write("""
    # Cars24 Used Car Price Prediction App!
""")


col1, col2 = st.columns(2)

fuel_type = col1.selectbox("Select fuel type",
                            ["Diesel", "Petrol", "CNG", "LPG", "Electric"])

engine = col1.slider("Set the engine power",
                    500, 5000, step=100)

transmission_type = col2.selectbox("Select transmission type",
                                    ['Manual', 'Automatic'])

seats = col2.selectbox("Select the number of seats",
                        [4,5,6,7,8])


encode_dict = {
    "fuel_type": {"Diesel": 1, "Petrol": 2, "CNG": 3, "LPG": 4, "Electric": 5},
    "transmission_type": {"Manual": 1, "Automatic": 2}
}


def model_pred(fuel_type, transmission_type, engine, seats):

    with open("car_pred", "rb") as file:
        reg_model = pickle.load(file)
    
    input_ftrs = [[2018.0, 1, 40000, fuel_type, transmission_type, 19.70, engine, 86.30, seats]]
    return reg_model.predict(input_ftrs)


if st.button("Predict Price"):
    fuel_type = encode_dict['fuel_type'][fuel_type]
    transmission_type = encode_dict['transmission_type'][transmission_type]

    price = model_pred(fuel_type, transmission_type, engine, seats)
    st.text("Predicted price of the car: "+ str(price))


