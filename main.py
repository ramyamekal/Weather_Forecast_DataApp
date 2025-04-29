import streamlit as st
import plotly.express as px
from backend import get_data

# Add Form
st.title("weather Forecast for the Next Days")
place = st.text_input("Place: ")
days= st.slider("Forecast Days", min_value=1,max_value=5,help="Select the number of forecasted days")
option = st.selectbox("select data to view",("Temperature","Sky"))
st.subheader(f"{option} fort he next {days} days in {place}")

if place:
    try:
#get temperature/sky data
        filtered_data = get_data(place,days)

        if option == "Temperature":
            #create temperature plot
            temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures,labels={"x":"Date","y":"Temperature(C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear":"images/clear.png","Clouds":"images/cloud.png","Rain":"images/rain.png","Snow":"images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths)

    except KeyError:
        st.write("That place does not exist")