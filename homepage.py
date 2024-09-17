import streamlit as st
import nav_bar_manager
import showcase_corner_visitor
import database_interaction
import subsribe_open_day
import chatbot

# Set page configuration
st.set_page_config(layout="wide", page_title="FOCS_website", page_icon=":mortar_board:")

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Main content styling */

      .block-container {
            background-color: white;
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

    /* Image placeholder styling */
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

nav_bar_manager.render_nav_bar()

# Get the page parameter from the URL
query_params = st.query_params
page = query_params.get("page", "home")

if page == "home":
    # Main Content for Homepage
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

    st.image("images/body_img.jpg", use_column_width=True)
    # video = database_interaction.retrieve_file_from_firebase("db/videos/crazy_frog.mp4")
    # st.video(video)

    # database_interaction.upload_file_to_firebase("videos/happy_cat.mp4", "db/videos/happy_cat.mp4");

elif page == "showcase_corner":
    showcase_corner_visitor.main()

elif page == "subsribe_openDay":
    subsribe_open_day.main()

elif page == "chatbot":
    chatbot.main()
