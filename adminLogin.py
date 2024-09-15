import streamlit as st
import time
import adminPage

# Hardcoded credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1"


# Function to display the login page
def login_page():
    st.title("Admin Login")

    # Add unique keys to text_input to avoid DuplicateWidgetID error
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login"):
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            st.success("Login successful!")
            st.session_state.logged_in = True

            with st.spinner('Loading...'):
                time.sleep(1)

            # Refresh the page to remove the login UI
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")


# Check if the user is logged in
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Show the login page if the user is not logged in
if not st.session_state.logged_in:
    login_page()
else:
    # Show the main admin content after login
    adminPage.adminPage()

