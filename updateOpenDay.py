import streamlit as st
import os
import pandas as pd
import database_interaction
import email_notification  # Assuming you have an email module to send notifications

def updateInfo():
    # Tab layout
    tabs = st.tabs(["Update OpenDay Poster", "Update Batch & Course", "Notify Users"])

    # 1. Update Poster Tab
    with tabs[0]:
        st.header("Update OpenDay Poster")
        # Directory where the uploaded poster will be stored
        UPLOAD_DIR = "uploaded_images"

        # Create the directory if it doesn't exist
        if not os.path.exists(UPLOAD_DIR):
            os.makedirs(UPLOAD_DIR)

        # File uploader widget
        uploaded_poster = st.file_uploader("Upload a Poster", type="png")

        # Button to upload the poster
        if st.button("Upload Poster"):
            if uploaded_poster is not None:
                # Save the uploaded poster
                poster_path = os.path.join(UPLOAD_DIR, uploaded_poster.name)

                # Delete the old poster
                database_interaction.delete_file_from_firebase("db/image/openDay.png")

                # Upload the new poster to Firebase Storage
                with open(poster_path, "wb") as f:
                    f.write(uploaded_poster.getbuffer())

                database_interaction.upload_file_to_firebase(poster_path, "db/image/openDay.png")

                st.success(f"Poster '{uploaded_poster.name}' has been successfully uploaded!")
            else:
                st.warning("Please upload a poster image.")

    # 2. Update Batch & Course Tab
    with tabs[1]:

        # --- Manage Batches ---
        st.subheader("Manage Batches")

        # Fetch existing batches from Firestore
        batches = database_interaction.fetch_batches_from_firestore()

        if batches:
            # Convert the list of batches into a DataFrame
            batch_df = pd.DataFrame(batches, columns=['batch_name'])

            st.write("#### Available Batches")
            st.dataframe(batch_df)  # Display batches in a table

            new_batch = st.text_input("New Batch Name")
            if st.button("Add Batch"):
                if new_batch:
                    database_interaction.insert_record_into_firestore("batches", {"batch_name": new_batch})
                    st.success(f"Batch '{new_batch}' added successfully!")
                else:
                    st.warning("Please enter a batch name.")

            # Delete batch
            selected_batch = st.selectbox("Select Batch to Delete", batch_df['batch_name'])
            if st.button("Delete Batch"):
                database_interaction.delete_record_from_firestore("batches", selected_batch)
                st.success(f"Batch '{selected_batch}' deleted successfully!")

        else:
            st.write("No batches available.")

        st.write("---")

        # --- Manage Courses ---
        st.subheader("Manage Courses")

        # Fetch existing courses from Firestore
        courses = database_interaction.fetch_courses_from_firestore()

        if courses:
            # Convert the list of courses into a DataFrame
            course_df = pd.DataFrame(courses, columns=['course_name'])

            st.write("#### Available Courses")
            st.dataframe(course_df)  # Display courses in a table

            # Add a new course
            new_course = st.text_input("New Course Name")
            if st.button("Add Course"):
                if new_course:
                    database_interaction.insert_record_into_firestore("courses", {"course_name": new_course})
                    st.success(f"Course '{new_course}' added successfully!")
                else:
                    st.warning("Please enter a course name.")

            # Delete course
            selected_course = st.selectbox("Select Course to Delete", course_df['course_name'])
            if st.button("Delete Course"):
                database_interaction.delete_record_from_firestore("courses", selected_course)
                st.success(f"Course '{selected_course}' deleted successfully!")

        else:
            st.write("No courses available.")

    with tabs[2]:
        st.header("Notify Students")
        st.subheader("Send Email Notification to Students Based on Selected Batch")

        # Fetch the list of entry batches for selection
        entry_batches = database_interaction.fetch_batches_from_firestore()

        if entry_batches:
            selected_batch = st.selectbox("Select Batch for Notification", entry_batches)

            if st.button("Send Notifications"):
                # Fetch all registered users from Firestore
                students = database_interaction.fetch_all_data_from_collection("students")

                if students:
                    for student in students:
                        student_data = student.to_dict()
                        name = student_data.get("name")
                        email = student_data.get("email")
                        course = student_data.get("course")
                        entry_batch = student_data.get("entry_batch")

                        # Send an email to each student if the entry_batch matches the selected batch
                        if entry_batch == selected_batch:
                            email_notification.send_email(
                                recipient=email,
                                subject="Open Day Notification",
                                body=f"Dear {name},\n\nWe are excited to inform you about the upcoming Open Day event!\n"
                                     f"Course: {course}\n"
                                     f"Entry Batch: {entry_batch}\n\nDon't miss it!\n\nBest regards,\nThe Team"
                            )

                    st.success(f"Notifications sent to users in batch '{selected_batch}'!")
                else:
                    st.warning("No users found to notify.")
        else:
            st.warning("No entry batches available for selection.")
