import streamlit as st
import database_interaction

def main():
    st.title("Open Day Information")

    # Fetch and display the poster image
    poster = database_interaction.retrieve_file_from_firebase("db/image/openDay.png")
    st.image(poster, caption="Open Day Poster", width=800)

    # Fetch the list of entry batches from Firestore
    entry_batches = database_interaction.fetch_batches_from_firestore()

    # Fetch the list of courses from Firestore
    courses = database_interaction.fetch_courses_from_firestore()

    # Input fields for students
    with st.form(key='student_form'):
        name = st.text_input("Name")

        if entry_batches:
            # Provide a list of options for Entry Batch from Firestore
            entry_batch = st.selectbox("Entry Batch", entry_batches)
        else:
            st.warning("No entry batches available.")
            entry_batch = None

        if courses:
            # Provide a list of options for Course from Firestore
            course_taken = st.selectbox("Course", courses)
        else:
            st.warning("No courses available.")
            course_taken = None

        email = st.text_input("Email")

        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if name and entry_batch and course_taken and email:
                # Prepare data to insert into Firestore
                student_data = {
                    "name": name,
                    "entry_batch": entry_batch,
                    "course": course_taken,
                    "email": email
                }
                # Insert the record into the "students" collection
                database_interaction.insert_record_into_firestore("students", student_data)

                st.write(f"Thank you {name} for signing up!")
                st.write(f"Entry Batch: {entry_batch}")
                st.write(f"Course: {course_taken}")
                st.write(f"Email: {email}")
            else:
                st.warning("Please fill in all fields.")
