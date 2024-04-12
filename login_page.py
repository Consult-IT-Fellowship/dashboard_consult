import streamlit as st

def login():
    """Displays a login form and returns True if credentials are valid."""
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "boss" and password == "imboss":
            st.success("Logged in as {}".format(username))
            with open("login.txt", "w") as file:
                file.write("1")
            return True
        if username == "sales" and password == "imsales":
            st.success("Logged in as {}".format(username))
            with open("login.txt", "w") as file:
                file.write("2")
            return True
        if username == "warehouse" and password == "imwarehouse":
            st.success("Logged in as {}".format(username))
            with open("login.txt", "w") as file:
                file.write("3")
            return True
        if username == "consultant" and password == "imconsultant":
            st.success("Logged in as {}".format(username))
            with open("login.txt", "w") as file:
                file.write("5")
            return True
        if username == "it" and password == "imit":
            st.success("Logged in as {}".format(username))
            with open("login.txt", "w") as file:
                file.write("4")
            return True
        else:
            st.error("Invalid username or password")
    return False  # Explicitly return False on failed login