import streamlit as st
from consult3 import landing_page
from login_page import login

def main():
    with open("login.txt", "r") as file:
        logged_in = file.read().strip()  # Odczytaj stan zalogowania

    if logged_in == "True":
        page = st.sidebar.radio("Menu", ["Boss_Dashboard"])  # Wyświetl tylko opcję konsultacji
        if page == "Consult":
            landing_page()
    else:
        page = st.sidebar.radio("Menu", ["Login"])  # Wyświetl tylko opcję logowania
        if page == "Login":
            if login():  # Sprawdź stan zalogowania
                st.write("Logged in successfully!")  # Opcjonalna wiadomość
                # Tutaj możesz również zaktualizować plik "login.txt" na "True" po udanym logowaniu
                st.experimental_rerun()
if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
    with open("login.txt", "w") as file:
        file.write("False")