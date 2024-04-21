import streamlit as st
import openai
from consult3 import save_logout_command
def chatbot_business():
    # Ustawienie klucza API OpenAI
    openai.api_key = "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"

    # Funkcja do zadawania pytań za pomocą OpenAI GPT-3
    def ask_question(text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"""You are an buisness asistant. You are helping buisness owners to maintain their business, answer in a professional manner. Langugae should be formal and professional, it
                should be POLISH or ENGLISH based on the user's language."""},
                {"role": "assistant", "content": "Hello, how can I assist you today"},
                {"role": "user", "content": text}
            ]
        )
        return response['choices'][0]['message']['content']

    # Tytuł strony
    st.title("Chatbot AI")

    # Pole tekstowe do wpisywania wiadomości
    user_input = st.text_input("Wpisz pytanie:", "")

    # Wybór hobby
    #hobby = st.selectbox("Wybierz hobby:", ["sport", "muzyka", "sztuka"])

    # Obsługa wysłania pytania
    if st.button("Zadaj pytanie"):
        if user_input:
            # Zadanie pytania i uzyskanie odpowiedzi
            bot_response = ask_question(user_input)
            
            # Wyświetlenie odpowiedzi
            st.header("Odpowiedź Chatbota:")
            st.write(bot_response)
    if st.button("Log out"):
        save_logout_command()
        st.experimental_rerun()