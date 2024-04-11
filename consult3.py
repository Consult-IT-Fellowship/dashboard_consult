import streamlit as st
import plotly.graph_objs as go
import pandas as pd

# Przykładowe dane
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [20, 14, 23, 25],
    'Values2': [10, 18, 16, 20],  # Dodatkowe dane dla drugiego wykresu
    'Values3': [30, 10, 15, 20]  # Dodatkowe dane dla trzeciego wykresu
})

# Tytuł strony
st.title("bookcraft pozdro dashboard")

# Wykres słupkowy i liniowy
st.plotly_chart(go.Figure(data=[
    go.Bar(
        x=df['Category'],
        y=df['Values'],
        name='Values',
        marker=dict(color='#FF851B')  # Kolor słupków
    ),
    go.Scatter(
        x=df['Category'],
        y=df['Values2'],
        name='Values2',
        mode='lines+markers',
        line=dict(color='#7FDBFF', width=2)  # Kolor linii
    )
], layout=go.Layout(
    title='Sprzedaż w kategoriach A, B, C, D',
    xaxis={'title': 'Category'},
    yaxis={'title': 'Values'},
    plot_bgcolor='#F3F6FA',  # Kolor tła wykresu
    paper_bgcolor='#F3F6FA',  # Kolor tła dashboardu
    font=dict(color='#2a3f5f'),  # Kolor tekstu
    margin=dict(l=40, r=40, t=40, b=40)  # Marginesy
)))

# Wykres kołowy
st.plotly_chart(go.Figure(data=[
    go.Pie(
        labels=df['Category'],
        values=df['Values3']
    )
], layout=go.Layout(
    title='Udział wiekowy klientów czy coś??',
    plot_bgcolor='#F3F6FA',  # Kolor tła wykresu
    paper_bgcolor='#F3F6FA',  # Kolor tła dashboardu
    font=dict(color='#2a3f5f'),  # Kolor tekstu
    margin=dict(l=40, r=40, t=40, b=40)  # Marginesy
)))
