import streamlit as st


def render_nav_bar():
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
            gap: 30px;
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
        st.image("images/nav_bar_logo.png", width=200)

    with col2:
        st.markdown(
            """
            <div class="nav-menu">
                <a href="?page=home">Home</a>
                <a href="#">About Us</a>
                <a href="#">Programmes</a>
                <a href="#">Facilities</a>
                <a href="#">Contact Us</a>
                <a href="?page=showcase_corner">Showcase Corner</a>
                <a href="?page=subsribe_openDay">Open Day Information</a>
                <a href="?page=chatbot">FAQ Chatbot</a>
            </div>
            """,
            unsafe_allow_html=True
        )
