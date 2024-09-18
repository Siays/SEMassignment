import streamlit as st
import database_interaction
import subsribe_open_day
import chatbot

def main():
    st.title("Showcase Corner")
    st.markdown("""
        <style>
        .custom-text {
            text-align: justify;
        }
        </style>
        <div class="custom-text">
            <p>Welcome to the Project Showcase Corner of the Faculty of Computer Science! This section is designed to highlight the most outstanding final year projects (FYP) created by our talented students. Here, you will find videos that showcase innovative solutions, technical expertise, and creative approaches to real-world problems. These projects represent the hard work and dedication of our top-performing students, offering a glimpse into the exciting advancements happening within our faculty.<br></p>
            <p>Each project featured here has been carefully selected by our FYP Board Committee, based on excellence in both execution and academic performance. Students whose projects receive a grade of A are invited to share their work through engaging video presentations, giving you a closer look at the challenges they tackled and the impact of their solutions. This platform not only celebrates the achievements of our students but also provides inspiration and insight for future students, industry professionals, and anyone interested in the field of computer science.<br></p>
            <p>We invite you to explore the projects, gain insights into cutting-edge research, and discover the innovative minds driving the future of technology. Whether you're a prospective student or simply curious, the Project Showcase Corner offers an exciting journey into the world of computer science at our university.<br><br></p>
        </div>
        """, unsafe_allow_html=True)


    video = database_interaction.retrieve_file_from_firebase("db/videos/showCase.mp4")
    st.video(video)

    # Adding hyperlink for 'notification' and 'FAQ'
    st.markdown("""
        Impressed? Don't hesitate to 
        subscribe to our university open day <a href="?page=subsribe_openDay">notification</a> email!
    """, unsafe_allow_html=True)

    st.markdown("""
        Have questions? Check out our 
        <a href="?page=chatbot">FAQ</a> to see if we can help resolve your doubts!
    """, unsafe_allow_html=True)

    # Handling page navigation
    query_params = st.query_params
    page = query_params.get("page", "subsribe_openDay")

    if page == "subsribe_openDay":
        subsribe_open_day.main()  # This will trigger your subscription page functionality
    elif page == "chatbot":
        chatbot.main()  # This will trigger your FAQ or chatbot page functionality


