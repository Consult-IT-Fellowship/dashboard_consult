import streamlit as st
import plotly.graph_objs as go
import pandas as pd
from consult3 import landing_page
from login_page import login



#Jeżeli fukncja login z login_page zwroci true to wtedy wyswietli się poniżej dalsza część przydzielona do worker()
#TO DO:
    #fajnie by było jakby strona się czyściła po zalogowaniu.
    #Należy dodać loginy dla 3 róznych użytkowników i stworzyć rózne wyglądy po zalogowaniu
    #potem dodać baze i chuj
    #predykcje analityczne przy uzyciu modelu
    #pozdro pozdro
def main():
    page = st.sidebar.selectbox("Menu", ["Login", "Consult"])

    if page == "Login":
        if login():
            st.session_state.logged_in = True
    elif page == "Consult":
        if st.session_state.logged_in == True:
            landing_page()
        else:
            st.write("Prosimy najpierw się zalogować.")

if __name__ == "__main__":
    st.session_state.logged_in = False
    st.set_page_config(layout="wide")
    main()
