import streamlit as st
import time
from streamlit_cookies_manager import EncryptedCookieManager
import adminPage

# Initialize Cookie Manager
cookies = EncryptedCookieManager(
    prefix="admin_app",  # You can set a prefix for your app
    password="secret_password_please_change",  # Set a password for encryption
)
if not cookies.ready():
    st.stop()

# Hardcoded credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1"

# Function to display the login page
def login_page():
    st.title("Admin Login")

    # Add unique keys to text_input to avoid DuplicateWidgetID error
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Sign In"):
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            st.success("Sign in successful!")
            cookies["logged_in"] = "True"  # Set a cookie for logged in status
            cookies.save()  # Save the cookie

            with st.spinner('Loading...'):
                time.sleep(1)

            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# Check the cookie for the login state
logged_in = cookies.get("logged_in")

# If the user is not logged in, show the login page
if logged_in != "True":
    login_page()
else:
    # Show the main admin content after login
    adminPage.adminPage()
