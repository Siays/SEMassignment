import streamlit as st
import uploadShowCase


# Function to render the admin navigation bar
def render_nav_bar_admin():
    st.markdown(
        """
        <style>
        .nav-logo img {
            height: 40px; /* Set logo height */
            width: 137px; /* Set logo width */
            object-fit: contain; /* Ensure the image maintains its aspect ratio */
        }

        .nav-menu {
            display: flex;
            gap: 50px;
        }

        .nav-menu a {
            color: black;
            text-decoration: none;
            font-size: 18px;
            font-weight: normal;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 3])

    with col1:
        st.image("images/nav_bar_logo.png", width=137)

    with col2:
        st.markdown(
            """
            <div class="nav-menu">
                <a href="?page=home">Home</a>
                <a href="?page=uploadShowCase">Upload ShowCase</a>
            </div>
            """,
            unsafe_allow_html=True
        )


# Set page configuration
st.set_page_config(layout="wide", page_title="FOCS Admin Website", page_icon=":mortar_board:")


def adminPage():
    # Render navigation bar after successful login
    render_nav_bar_admin()
    # Get the page parameter from the URL
    query_params = st.query_params
    page = query_params.get("page", "home")

    if page == "home":
        # Main Content for Homepage
        st.markdown(
            """
            <div class="main-content">
                <h1>FOCS Admin</h1>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.image("images/adminhome.png", use_column_width=True)
    elif page == "uploadShowCase":
        uploadShowCase.uploadPage()
