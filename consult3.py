import streamlit as st
import plotly.graph_objs as go
import pandas as pd
def landing_page():
    # Przykładowe dane
    df = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D', 'E', 'F'],
        'Values1': [20, 14, 23, 25, 18, 22],
        'Values2': [10, 18, 16, 20, 12, 15],
        'Values3': [30, 10, 15, 20, 25, 17],
        'Values4': [25, 15, 20, 18, 22, 19],
        'Values5': [15, 20, 12, 16, 19, 23],
        'Values6': [22, 19, 23, 20, 15, 21],
    })
    #st.set_page_config(layout="wide")
    # Tytuł strony
    st.title("Buisness Dashboard")

    # Ustawienie kolumn
    cols = st.columns(3)

    # Wykresy - wiersz 1

    with cols[0]:
        st.plotly_chart(go.Figure(data=[
            go.Bar(
                x=df['Category'],
                y=df['Values1'],
                name='Values1',
                marker=dict(color='#FF851B')
            )
        ], layout=go.Layout(
            title='Wykres 1',
            xaxis={'title': 'Category'},
            yaxis={'title': 'Values'},
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#F3F6FA',
            font=dict(color='#2a3f5f'),
            margin=dict(l=50, r=50, t=50, b=50)
        )))
        for _ in range(10):
            st.write("")
    with cols[1]:
        st.plotly_chart(go.Figure(data=[
            go.Pie(
                labels=df['Category'],
                values=df['Values2']
            )
        ], layout=go.Layout(
            title='Wykres 2',
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#F3F6FA',
            font=dict(color='#2a3f5f'),
            margin=dict(l=50, r=50, t=50, b=50)
        )))
        for _ in range(10):
            st.write("")
    with cols[2]:
        st.plotly_chart(go.Figure(data=[
            go.Scatter(
                x=df['Category'],
                y=df['Values3'],
                name='Values3',
                mode='lines+markers',
                line=dict(color='#7FDBFF', width=2)
            )
        ], layout=go.Layout(
            title='Wykres 3',
            xaxis={'title': 'Category'},
            yaxis={'title': 'Values'},
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#F3F6FA',
            font=dict(color='#2a3f5f'),
            margin=dict(l=50, r=50, t=50, b=50)
        )))
        for _ in range(10):
            st.write("")
    # Wykresy - wiersz 2
    with cols[0]:
        st.plotly_chart(go.Figure(data=[
            go.Bar(
                x=df['Category'],
                y=df['Values4'],
                name='Values4',
                marker=dict(color='#FF851B')
            )
        ], layout=go.Layout(
            title='Wykres 4',
            xaxis={'title': 'Category'},
            yaxis={'title': 'Values'},
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#F3F6FA',
            font=dict(color='#2a3f5f'),
            margin=dict(l=50, r=50, t=50, b=50)
        )))
        for _ in range(10):
            st.write("")
    with cols[1]:
        st.plotly_chart(go.Figure(data=[
            go.Pie(
                labels=df['Category'],
                values=df['Values5']
            )
        ], layout=go.Layout(
            title='Wykres 5',
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#F3F6FA',
            font=dict(color='#2a3f5f'),
            margin=dict(l=50, r=50, t=50, b=50)
        )))
        for _ in range(10):
            st.write("")
    with cols[2]:
        st.plotly_chart(go.Figure(data=[
            go.Scatter(
                x=df['Category'],
                y=df['Values6'],
                name='Values6',
                mode='lines+markers',
                line=dict(color='#7FDBFF', width=2)
            )
            
        ], layout=go.Layout(
            title='Wykres 6',
            xaxis={'title': 'Category'},
            yaxis={'title': 'Values'},
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#F3F6FA',
            font=dict(color='#2a3f5f'),
            margin=dict(l=50, r=50, t=50, b=50)
        )))
        for _ in range(10):
            st.write("")
def sales_page():
    # Przykładowe dane
    df = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D', 'E', 'F'],
        'Values1': [20, 14, 23, 25, 18, 22],
        'Values2': [10, 18, 16, 20, 12, 15],
        'Values3': [30, 10, 15, 20, 25, 17],
        'Values4': [25, 15, 20, 18, 22, 19],
        'Values5': [15, 20, 12, 16, 19, 23],
        'Values6': [22, 19, 23, 20, 15, 21],
    })
    #st.set_page_config(layout="wide")
    # Tytuł strony
    st.title("Sales")

    # Ustawienie kolumn
    cols = st.columns(3)

    # Wykresy - wiersz 1

    with cols[0]:
        st.plotly_chart(go.Figure(data=[
            go.Bar(
                x=df['Category'],
                y=df['Values1'],
                name='Values1',
                marker=dict(color='#FF851B')
            )
        ], layout=go.Layout(
            title='Wykres 1',
            xaxis={'title': 'Category'},
            yaxis={'title': 'Values'},
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#F3F6FA',
            font=dict(color='#2a3f5f'),
            margin=dict(l=50, r=50, t=50, b=50)
        )))
        for _ in range(10):
            st.write("")
    with cols[1]:
        st.plotly_chart(go.Figure(data=[
            go.Pie(
                labels=df['Category'],
                values=df['Values2']
            )
        ], layout=go.Layout(
            title='Wykres 2',
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#F3F6FA',
            font=dict(color='#2a3f5f'),
            margin=dict(l=50, r=50, t=50, b=50)
        )))
        for _ in range(10):
            st.write("")
    with cols[2]:
        st.plotly_chart(go.Figure(data=[
            go.Scatter(
                x=df['Category'],
                y=df['Values3'],
                name='Values3',
                mode='lines+markers',
                line=dict(color='#7FDBFF', width=2)
            )
        ], layout=go.Layout(
            title='Wykres 3',
            xaxis={'title': 'Category'},
            yaxis={'title': 'Values'},
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#F3F6FA',
            font=dict(color='#2a3f5f'),
            margin=dict(l=50, r=50, t=50, b=50)
        )))
        for _ in range(10):
            st.write("")
def warehouse_page():
    # Przykładowe dane
    df = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D', 'E', 'F'],
        'Values1': [20, 14, 23, 25, 18, 22],
        'Values2': [10, 18, 16, 20, 12, 15],
        'Values3': [30, 10, 15, 20, 25, 17],
        'Values4': [25, 15, 20, 18, 22, 19],
        'Values5': [15, 20, 12, 16, 19, 23],
        'Values6': [22, 19, 23, 20, 15, 21],
    })
    #st.set_page_config(layout="wide")
    # Tytuł strony
    st.title("Warehouse")

    # Ustawienie kolumn
    cols = st.columns(3)

    # Wykresy - wiersz 1

    with cols[0]:
        st.plotly_chart(go.Figure(data=[
            go.Bar(
                x=df['Category'],
                y=df['Values1'],
                name='Values1',
                marker=dict(color='#FF851B')
            )
        ], layout=go.Layout(
            title='Wykres 1',
            xaxis={'title': 'Category'},
            yaxis={'title': 'Values'},
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#F3F6FA',
            font=dict(color='#2a3f5f'),
            margin=dict(l=50, r=50, t=50, b=50)
        )))
        for _ in range(10):
            st.write("")
    with cols[1]:
        st.plotly_chart(go.Figure(data=[
            go.Pie(
                labels=df['Category'],
                values=df['Values2']
            )
        ], layout=go.Layout(
            title='Wykres 2',
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#F3F6FA',
            font=dict(color='#2a3f5f'),
            margin=dict(l=50, r=50, t=50, b=50)
        )))
        for _ in range(10):
            st.write("")
    with cols[2]:
        st.plotly_chart(go.Figure(data=[
            go.Scatter(
                x=df['Category'],
                y=df['Values3'],
                name='Values3',
                mode='lines+markers',
                line=dict(color='#7FDBFF', width=2)
            )
        ], layout=go.Layout(
            title='Wykres 3',
            xaxis={'title': 'Category'},
            yaxis={'title': 'Values'},
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#F3F6FA',
            font=dict(color='#2a3f5f'),
            margin=dict(l=50, r=50, t=50, b=50)
        )))
        for _ in range(10):
            st.write("")