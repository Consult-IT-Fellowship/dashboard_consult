import streamlit as st

def login():
    """Displays a login form and returns True if credentials are valid."""
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "boss" and password == "imboss":
            st.success("Logged in as {}".format(username))
            return True
        else:
            st.error("Invalid username or password")
    return False  # Explicitly return False on failed login