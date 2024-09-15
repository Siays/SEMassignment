import streamlit as st
import database_interaction

def main():
    st.title("Open Day Information")

    # Fetch and display the poster image
    poster = database_interaction.retrieve_file_from_firebase("db/image/openDay.png")
    st.image(poster, caption="Open Day Poster", use_column_width=True)

    # Input fields for students
    with st.form(key='student_form'):
        name = st.text_input("Name")
        entry_batch = st.text_input("Entry Batch")
        course_taken = st.text_input("Course")
        email = st.text_input("Email")

        submit_button = st.form_submit_button("Submit")

        if submit_button:
            # Handle form submission, e.g., save to database or send email
            st.write(f"Thank you {name} for signing up!")
            st.write(f"Entry Batch: {entry_batch}")
            st.write(f"Email: {email}")
            # You can add code here to process the input, e.g., save it to a database or send a notification email


