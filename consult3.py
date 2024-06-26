import streamlit as st
import plotly.graph_objs as go
import pandas as pd
import random

def save_logout_command():
    with open("login.txt", "w") as file:
        file.write("0")

#Pobranie danych  z pliku data_set csv i po dlugosci miesiecy zsumowanie wartosci 
def getting_sales_data():
    data = pd.read_csv('data_set.csv')
    values = data['value']

    months = {
        'Styczeń' : sum(values[0:32]),
        'Luty' : sum(values[32:60]),
        'Marzec' : sum(values[60:91]),
        'Kwiecień' : sum(values[91:121]),
        'Maj' : sum(values[121:152]),
        'Czerwiec' :sum(values[152:182]),
        'lipiec' :sum(values[182:213]),
        'Sierpień' :sum(values[213:244]),
        'Wrzesień' :sum(values[244:274]),
        'Październik' :sum(values[274:305]),
        'Listopad' : sum(values[305:335]),
        'Grudzień' :sum(values[335:366]),
    }
    return months


def getting_sales_predicted():
    data = pd.read_csv('data_set.csv')
    values = data['value']
    data = {'Styczeń' : 10604378,
        'Luty' : 9712031,
        'Marzec' : 10055337
    }

    return data

def getting_sales_data2():
    data = pd.read_csv('data_set.csv')
    values = data['value']

    months = {
        'Styczeń' : sum(values[0:32])+ random.randint(-50000,50000),
        'Luty' : sum(values[32:60])+random.randint(-50000,50000),
        'Marzec' : sum(values[60:91] ) + random.randint(-50000,50000),
        'Kwiecień' : sum(values[91:121])+ random.randint(-50000,50000),
        'Maj' : sum(values[121:152])+ random.randint(-50000,50000),
        'Czerwiec' :sum(values[152:182])+random.randint(-50000,50000),
        'lipiec' :sum(values[182:213])+random.randint(-50000,50000),
        'Sierpień' :sum(values[213:244])+random.randint(-50000,50000),
        'Wrzesień' :sum(values[244:274])+random.randint(-50000,50000),
        'Październik' :sum(values[274:305])+random.randint(-50000,50000),
        'Listopad' : sum(values[305:335])+random.randint(-50000,50000), 
        'Grudzień' :sum(values[335:366])+ random.randint(-50000,50000),
    }
    return months

def getting_sales_data2_predicted():
    data = pd.read_csv('data_set.csv')
    values = data['value']

    months = {
        'Styczeń' :  9712031,
        'Luty' :12055337,
        'Marzec' : 10055337
    }
    return months


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
    # Tytuł strony
    st.title("Business Dashboard")

    # Ustawienie kolumn
    cols = st.columns(3)

    # Wykresy - wiersz 1

    # Tworzenie wykresu dla sprzedaży w poszczególnych miesiącach
    with cols[0]:
        fig = go.Figure(data=[
            go.Bar(
                x=list(getting_sales_data().keys()),  
                y=list(getting_sales_data().values()), 
                name='Values1',
                marker=dict(color='#FF851B')
            )
        ], layout=go.Layout(
            title='Sprzedaż w poszczególnych miesiącach',
            xaxis={'title': 'Category', 'tickvals': list(range(len(getting_sales_data()))), 'ticktext': list(getting_sales_data().keys()), 'tickfont': dict(size=17)},  # Add tickvals and ticktext for custom x-axis labels
            yaxis={'title': 'Values', 'tickfont': dict(size=19)},
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#0E1117',
            font=dict(color='#2a3f5f', size=20),
            margin=dict(l=50, r=50, t=50, b=50),  
        ))
        st.plotly_chart(fig)

    # Wykres kołowy dla książek w magazynie
    with cols[1]:
        df2 = pd.DataFrame({'ksiazki': ['Fantasy', 'Dokument', 'Horror', 'Przygodowe', 'Dla dzieci', 'Beletrystyka']})
        st.plotly_chart(go.Figure(data=[
            go.Pie(
                labels=df2['ksiazki'],
                values=df['Values2']
            )
        ], layout=go.Layout(
            title='Książki w magazynie',
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#0E1117',
            font=dict(color='#2a3f5f', size=20),
            margin=dict(l=50, r=50, t=50, b=50),
            legend=dict(font=dict(size=20)) #legenda
        )))

    # Wykres liniowy dla marży brutto
    with cols[2]:
        st.plotly_chart(go.Figure(data=[
            go.Scatter(
                x=list(getting_sales_data2().keys()),
                y=list(getting_sales_data2().values()),
                name='Values3',
                mode='lines+markers',
                line=dict(color='#7FDBFF', width=2)
            )
        ], layout=go.Layout(
            title='Marża brutto',
            xaxis={'title': 'Category', 'tickfont': dict(size=17)},
            yaxis={'title': 'Values', 'tickfont': dict(size=19)},
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#0E1117',
            font=dict(color='#2a3f5f', size=20),
            margin=dict(l=50, r=50, t=50, b=50)
        )))

    # Wykresy - wiersz 2

    # Tworzenie wykresu dla przewidywanej sprzedaży AI na najbliższe 3 miesiące
    with cols[0]:
        fig = go.Figure(data=[
            go.Bar(
                x=list(getting_sales_predicted().keys()),
                y=list(getting_sales_predicted().values()),
                name='Values4',
                marker=dict(color='#FF851B')
            )
        ], layout=go.Layout(
            title='Przewidywana sprzedaż AI na najbliższe 3 miesiące',
            xaxis={'title': 'Category', 'tickfont': dict(size=17)},
            yaxis={'title': 'Values', 'tickfont': dict(size=19)},
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#0E1117',
            font=dict(color='#2a3f5f', size=20),
            margin=dict(l=50, r=50, t=50, b=50)
        ))
        st.plotly_chart(fig)

    # Wykres kołowy dla monitorowania zamówień na podstawie regionów
    with cols[1]:
        df3 = pd.DataFrame({'kraje': ['Polska', 'Holandia', 'Niemcy', 'Francja', 'USA', 'Szwecja']})
        st.plotly_chart(go.Figure(data=[
            go.Pie(
                labels=df3['kraje'],
                values=df['Values5']
            )
        ], layout=go.Layout(
            title='Zamówienia według regionów',
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#0E1117',
            font=dict(color='#2a3f5f', size=20),
            margin=dict(l=50, r=50, t=50, b=50),
            legend=dict(font=dict(size=20)) #legenda
        )))

    # Wykres liniowy dla marży brutto z prognozą na najbliższe 3 miesiące
    with cols[2]:
        st.plotly_chart(go.Figure(data=[
            go.Scatter(
                x=list(getting_sales_predicted().keys()),
                y=list(getting_sales_predicted().values()),
                name='Values6',
                mode='lines+markers',
                line=dict(color='#7FDBFF', width=2)
            )
        ], layout=go.Layout(
            title='Marża brutto, prognoza na najbliższe 3 miesiące',
            xaxis={'title': 'Category', 'tickfont': dict(size=17)},
            yaxis={'title': 'Values','tickfont': dict(size=19)},
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#0E1117',
            font=dict(color='#2a3f5f', size=20),
            margin=dict(l=50, r=50, t=50, b=50)
        )))

    # Przycisk wylogowania
    if st.button("Log out"):
        save_logout_command()
        st.experimental_rerun()

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
    st.title("Dział Sprzedaży")

    # Ustawienie kolumn
    cols = st.columns(2)
    with cols[0]:
        # Wykresy - wiersz 1
        # Tworzenie wykresu dla sales dla sales
        fig = go.Figure(data=[
            go.Bar(
                x=list(getting_sales_data().keys()),  
                y=list(getting_sales_data().values()), 
                name='Values1',
                marker=dict(color='#FF851B')
            )
        ], layout=go.Layout(
            title='Sprzedaż w poszczególnych miesiącach',
            xaxis={'title': 'Category', 'tickvals': list(range(len(getting_sales_data()))), 'ticktext': list(getting_sales_data().keys())},  # Add tickvals and ticktext for custom x-axis labels
            yaxis={'title': 'Values'},
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#0E1117',
            font=dict(color='#2a3f5f'),
            margin=dict(l=50, r=50, t=50, b=50)  
        ))



            # Wyswietlenie wykresu sales prediction dla sales
        st.plotly_chart(fig)

    with cols[1]:
        # Tworzenie wykresu
        fig = go.Figure(data=[
            go.Bar(
                x=list(getting_sales_predicted().keys()),
                y=list(getting_sales_predicted().values()),
                name='Values4',
                marker=dict(color='#FF851B')
            )
        ], layout=go.Layout(
            title='Przewidywana sprzedaż AI na najbliższe 3 miesiące',
            xaxis={'title': 'Category'},
            yaxis={'title': 'Values'},
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#0E1117',
            font=dict(color='#2a3f5f'),
            margin=dict(l=50, r=50, t=50, b=50)
        ))
        
    # Wyświetlanie wykresu
        st.plotly_chart(fig)

        #AI proposition for sales
    with cols[0]:
        st.write("Propozycje AI jak poprawić sprzedaż na podstawie wykresu:")
        st.write('')
        st.write("Zwiększ liczbę odwiedzających witrynę internetową")
        st.write("- Zoptymalizuj SEO strony.")
        st.write("- Prowadź kampanie PPC.")
        st.write("- Ułatw nawigację na stronie.")
        st.write("- Oferuj bezpłatne próby/rabaty.")
    with cols[1]:
        st.write("Zwiększ średnią wartość zamówienia:")
        st.write("- Oferuj produkty komplementarne.")
        st.write("- Oferuj produkty komplementarne.")
        st.write('- Stwórz programy lojalnościowe.')
        st.write('- Oferuj bezpłatną wysyłkę/zachęty.')

    if st.button("Log out"):
        save_logout_command()
        st.experimental_rerun()
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
    st.title("Magazyn")

    # Ustawienie kolumn
    cols = st.columns(2)
    with cols[0]:
        df2 = pd.DataFrame({'ksiazki': ['Fantasy', 'Dokument', 'Horror', 'Przygodowe', 'Dla dzieci', 'Beletrystyka']})
        st.plotly_chart(go.Figure(data=[
            go.Pie(
                labels=df2['ksiazki'],
                values=df['Values2']
            )
        ], layout=go.Layout(
            title='Książki w magazynie',
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#0E1117',
            font=dict(color='#2a3f5f'),
            margin=dict(l=50, r=50, t=50, b=50)
        )))

    with cols[1]:
        df3 = pd.DataFrame({'kraje': ['Polska', 'Holandia', 'Niemcy', 'Francja', 'USA', 'Szwecja']})
        st.plotly_chart(go.Figure(data=[
            go.Pie(
                labels=df3['kraje'],
                values=df['Values5']
            )
        ], layout=go.Layout(
            title='Zamówienia według regionów',
            plot_bgcolor='#F3F6FA',
            paper_bgcolor='#0E1117',
            font=dict(color='#2a3f5f'),
            margin=dict(l=50, r=50, t=50, b=50)
        )))

    link='Link do szczegółowego stanu magazynu: [click here](https://docs.google.com/spreadsheets/d/1nd-cwH1cNfceeBij6SNzq-I2x7zfKsYwf_9zyWJxyEs/edit?usp=sharing)'
    st.markdown(link,unsafe_allow_html=True)

    for _ in range(10):
        st.write("")
    if st.button("Log out"):
        save_logout_command()
        st.experimental_rerun()
def mobile():
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

    # Tytuł strony
    st.title("Business Dashboard")

    # Tworzenie wykresu dla Values1
    st.subheader("Sprzedaż w poszczególnych miesiącach")
    st.markdown("")  # Dodaj przerwę
    st.plotly_chart(go.Figure(data=[
        go.Bar(
            x=list(getting_sales_data().keys()),  
            y=list(getting_sales_data().values()), 
            name='Values1',
            marker=dict(color='#FF851B')
        )
    ], layout=go.Layout(
        xaxis={'title': 'Category', 'tickvals': list(range(len(getting_sales_data()))), 'ticktext': list(getting_sales_data().keys()), 'tickfont': dict(size=17)},  # Add tickvals and ticktext for custom x-axis labels
        yaxis={'title': 'Values', 'tickfont': dict(size=19)},
        plot_bgcolor='#F3F6FA',
        paper_bgcolor='#0E1117',
        font=dict(color='#2a3f5f'),
        margin=dict(l=50, r=50, t=50, b=50)
    )), use_container_width=True, height=300, width=400)

    # Dodaj przerwę między wykresami
    st.markdown("---")

    # Tworzenie wykresu dla Values2
    st.subheader("Książki w magazynie")
    st.markdown("")  # Dodaj przerwę
    st.plotly_chart(go.Figure(data=[
        go.Pie(
            labels=['Fantasy', 'Dokument', 'Horror', 'Przygodowe', 'Dla dzieci', 'Beletrystyka'],
            values=df['Values2']
        )
    ], layout=go.Layout(
        plot_bgcolor='#F3F6FA',
        paper_bgcolor='#0E1117',
        font=dict(color='#2a3f5f'),
        margin=dict(l=50, r=50, t=50, b=50)
    )), use_container_width=True, height=300, width=400)

    # Dodaj przerwę między wykresami
    st.markdown("---")

    # Tworzenie wykresu dla Values3
    st.subheader("Marża brutto")
    st.markdown("")  # Dodaj przerwę
    st.plotly_chart(go.Figure(data=[
        go.Scatter(
            x=list(getting_sales_data2().keys()),
            y=list(getting_sales_data2().values()),
            name='Values3',
            mode='lines+markers',
            line=dict(color='#7FDBFF', width=2)
        )
    ], layout=go.Layout(
        xaxis={'title': 'Category', 'tickfont': dict(size=17)},
        yaxis={'title': 'Values', 'tickfont': dict(size=19)},
        plot_bgcolor='#F3F6FA',
        paper_bgcolor='#0E1117',
        font=dict(color='#2a3f5f'),
        margin=dict(l=50, r=50, t=50, b=50)
    )), use_container_width=True, height=300, width=400)

    # Dodaj przerwę między wykresami
    st.markdown("---")

    # Tworzenie wykresu dla Values4
    st.subheader("Przewidywana sprzedaż AI na najbliższe 3 miesiące")
    st.markdown("")  # Dodaj przerwę
    st.plotly_chart(go.Figure(data=[
        go.Bar(
            x=list(getting_sales_predicted().keys()),
            y=list(getting_sales_predicted().values()),
            name='Values4',
            marker=dict(color='#FF851B')
        )
    ], layout=go.Layout(
        xaxis={'title': 'Category', 'tickfont': dict(size=17)},
        yaxis={'title': 'Values', 'tickfont': dict(size=19)},
        plot_bgcolor='#F3F6FA',
        paper_bgcolor='#0E1117',
        font=dict(color='#2a3f5f'),
        margin=dict(l=50, r=50, t=50, b=50)
    )), use_container_width=True, height=300, width=400)

    # Dodaj przerwę między wykresami
    st.markdown("---")

    # Tworzenie wykresu dla Values5
    st.subheader("Zamówienia według regionów")
    st.markdown("")  # Dodaj przerwę
    st.plotly_chart(go.Figure(data=[
        go.Pie(
            labels=['Polska', 'Holandia', 'Niemcy', 'Francja', 'USA', 'Szwecja'],
            values=df['Values5']
        )
    ], layout=go.Layout(
        plot_bgcolor='#F3F6FA',
        paper_bgcolor='#0E1117',
        font=dict(color='#2a3f5f'),
        margin=dict(l=50, r=50, t=50, b=50)
    )), use_container_width=True, height=300, width=400)

    # Dodaj przerwę między wykresami
    st.markdown("---")

    # Tworzenie wykresu dla Values6
    st.subheader("Marża brutto, prognoza na najbliższe 3 miesiące")
    st.markdown("")  # Dodaj przerwę
    st.plotly_chart(go.Figure(data=[
        go.Scatter(
            x=list(getting_sales_predicted().keys()),
            y=list(getting_sales_predicted().values()),
            name='Values6',
            mode='lines+markers',
            line=dict(color='#7FDBFF', width=2)
        )
    ], layout=go.Layout(
        xaxis={'title': 'Category'},
        yaxis={'title': 'Values'},
        plot_bgcolor='#F3F6FA',
        paper_bgcolor='#0E1117',
        font=dict(color='#2a3f5f'),
        margin=dict(l=50, r=50, t=50, b=50)
    )), use_container_width=True, height=300, width=400)

    if st.button("Log out"):
        save_logout_command()
        st.experimental_rerun()
