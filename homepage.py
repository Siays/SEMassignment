import streamlit as st

# Set page configuration
st.set_page_config(layout="wide", page_title="FOCS at a Glance", page_icon=":mortar_board:")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stAppViewContainer {
        background-color: white;
    }

    .nav-bar {
        background-color: #FFA500; /* Set navbar background to an orangish color */
        padding: 10px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        box-shadow: 0px 4px 2px -2px gray; /* Add a shadow to the navbar */
    }

    .nav-menu {
        display: flex;
        gap: 15px; /* Space between the menu items */
    }

    .nav-menu a {
        color: black;
        text-decoration: none;
        font-size: 18px;
        font-weight: normal;
    }

    .nav-logo {
        display: flex;
        align-items: center;
    }

    .nav-logo img {
        height: 40px; /* Set logo height */
        width: 137px; /* Set logo width */
        object-fit: contain; /* Ensure the image maintains its aspect ratio */
    }

    .main-content {
        margin-top: 80px;
        text-align: center;
        color: black;
    }

    .statistics {
        display: flex;
        justify-content: space-around;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .stat-column {
        text-align: center;
        flex: 1;
        color: black;
    }

    .stat-number {
        font-size: 40px;
        font-weight: bold;
    }

    .stat-text {
        font-size: 18px;
        color: black;
    }

    .image-placeholder {
        width: 100%;
        height: 400px;
        background-color: #e0e0e0;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
    }

    .image-caption {
        font-size: 16px;
        margin-top: 10px;
    }

    h1 {
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Navigation Bar with logo and menu
st.markdown(
    """
    <div class="nav-bar">
        <div class="nav-logo">
            <img src="images/nav_bar_logo.png" alt="Logo">
        </div>
        <div class="nav-menu">
            <a href="#">Home</a>
            <a href="#">About Us</a>
            <a href="#">Programmes</a>
            <a href="#">Facilities</a>
            <a href="#">Contact Us</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Main Content
st.markdown(
    """
    <div class="main-content">
        <h1>FOCS at a Glance</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Statistics Section
st.markdown(
    """
    <div class="statistics">
        <div class="stat-column">
            <div class="stat-number">1972</div>
            <div class="stat-text">FOUNDED</div>
        </div>
        <div class="stat-column">
            <div class="stat-number">5</div>
            <div class="stat-text">DEPARTMENTS</div>
        </div>
        <div class="stat-column">
            <div class="stat-number">16</div>
            <div class="stat-text">PROGRAMMES</div>
        </div>
        <div class="stat-column">
            <div class="stat-number">6</div>
            <div class="stat-text">RESEARCH CENTRES</div>
        </div>
        <div class="stat-column">
            <div class="stat-number">3500+</div>
            <div class="stat-text">ACTIVE STUDENTS</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Placeholder Image
st.image("images/body_img.jpg", use_column_width=True)
