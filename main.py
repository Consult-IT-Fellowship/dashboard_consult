import streamlit as st
from consult3 import *
from login_page import *



st.set_page_config(layout="wide")



'''Jeżeli fukncja login z login_page zwroci true to wtedy wyswietli się poniżej dalsza część przydzielona do worker()
*TO DO:
    -fajnie by było jakby strona się czyściła po zalogowaniu.
    -Należy dodać loginy dla 3 róznych użytkowników i stworzyć rózne wyglądy po zalogowaniu
    -potem dodać baze i chuj
    -predykcje analityczne przy uzyciu modelu
    pozdro pozdro
'''
if __name__ == "__main__":
    if login():
        worker()
        
