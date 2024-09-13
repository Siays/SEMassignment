# import time
# import streamlit as st
# import adminPage
# # Hardcoded login credentials (in a real app, these should come from a secure database)
# ADMIN_USERNAME = "admin"
# ADMIN_PASSWORD = "1"
# logged_in = False
#
# # Function to display the login page
# def login():
#     st.title("Admin Login")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password", key="focsPass")
#
#     if st.button("Login"):
#         if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
#             st.success("Login successful!")
#             with st.spinner('Loading...'):
#                 # Wait for 1 second
#                 time.sleep(1)
#             adminPage.main()
#     #         # Set the login state to true
#     #         logged_in = True
#     #         # Redirect user to the main page after successful login
#     #         # st.experimental_rerun()
#     #
#         else:
#             st.error("Invalid username or password")


# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False
#
# # If the user is not logged in, show the login page
# if not logged_in:
#     main()
# else:
    # If logged in, show the main content
    # with st.spinner('Loading...'):
        # Wait for 1 second
        # time.sleep(1)
    # adminPage.main()
# if __name__ == "__main__":
#     main()

# login()

# # VERSION 2 - CANNOT LOAD THE ADMINPAGE
#
#
# import time
# import streamlit as st
# import adminPage
#
# # Hardcoded login credentials (in a real app, these should come from a secure database)
# ADMIN_USERNAME = "admin"
# ADMIN_PASSWORD = "1"
# logged_in = False
#
# # Function to display the login page
# def main():
#     st.title("Admin Login")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")  # Removed the 'key' argument
#
#     if st.button("Login"):
#         if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
#             st.success("Login successful!")
#             with st.spinner('Loading...'):
#                 # Wait for 1 second
#                 time.sleep(1)
#             # adminPage.main()
#             # Set the login state to true
#             global logged_in
#             logged_in = True
#             # Redirect user to the main page after successful login
#             # st.experimental_rerun()
#         else:
#             st.error("Invalid username or password")
#
#
# # if "logged_in" not in st.session_state:
# #     st.session_state.logged_in = False
# #
# # # If the user is not logged in, show the login page
# if logged_in:
#     # If logged in, show the main content
#     with st.spinner('Loading...'):
#         # Wait for 1 second
#         time.sleep(1)
#     adminPage.main()
# if __name__ == "__main__":
#     main()


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

