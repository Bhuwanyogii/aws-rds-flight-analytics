import os
import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px

db = DB()

st.sidebar.title('Flights Analytics')

user_option = st.sidebar.selectbox('Menu',['Select One','Check Flights','Analytics'])

if user_option == 'Check Flights':
    st.title('Check Flights')

    col1, col2 = st.columns(2)

    with col1:
        source_city = db.fetch_source_city()
        source = st.selectbox('Source',source_city)
    with col2:
        destination_city = db.fetch_destination_city(source)
        destination = st.selectbox('Destination', destination_city)

    if st.button('Search'):
        results = db.fetch_all_flights(source,destination)
        st.dataframe(results)

elif user_option == 'Analytics':
    airline, frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels = airline,
            values = frequency,
            hoverinfo = "label+percent",
            textinfo = "value"
        ))

    st.header("Pie chart")
    st.plotly_chart(fig)

    st.header("Bar chart")
    city, frequency1 = db.busy_airport()
    fig = px.bar(
        x = city,
        y = frequency1
    )
    st.plotly_chart(fig, theme = 'streamlit', use_container_width=True)


    st.header("Line chart")
    date, frequency2 = db.daily_frequency()
    fig = px.line(
        x=date,
        y=frequency2
    )
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)


else:
    st.title('✈️ Flight Analytics Dashboard')

    st.markdown("""
    This app lets you explore and analyze flight data stored in a MySQL database (hosted on AWS RDS).

    ### What you can do:
    - **Check Flights** — Search for available flights between any source and destination city, with details like airline, route, departure time, duration, and price.
    - **Analytics** — Visualize trends across the dataset:
        - Airline-wise flight distribution (pie chart)
        - Busiest airports by traffic (bar chart)
        - Daily flight frequency over time (line chart)

    ### Tech stack:
    - **Frontend:** Streamlit
    - **Database:** MySQL on AWS RDS
    - **Visualization:** Plotly
    - **Data pipeline:** Pandas + SQLAlchemy for CSV-to-database import

    ---
    Built by Bhuwan Yogi as a data analytics project.
    """)