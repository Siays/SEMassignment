import streamlit as st
import os
import database_interaction


def uploadPage():
    # Directory where uploaded videos will be stored
    UPLOAD_DIR = "uploaded_videos"

    # Create the directory if it doesn't exist
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    # Admin Page Title
    st.title("Upload Video for Showcase Corner")

    # File uploader widget
    uploaded_video = st.file_uploader("Upload a Video", type=["mp4", "avi", "mov"])

    # Button to save the uploaded video
    if st.button("Upload Video"):
        if uploaded_video is not None:
            # delete the old video
            # database_interaction.delete_file_from_firebase("db/videos/showCase.mp4")

            # Save the uploaded video
            video_path = os.path.join(UPLOAD_DIR, uploaded_video.name)
            database_interaction.upload_file_to_firebase(video_path, "db/videos/showCase.mp4")

            with open(video_path, "wb") as f:
                f.write(uploaded_video.getbuffer())

            st.success(f"Video '{uploaded_video.name}' has been successfully uploaded!")
        else:
            st.warning("Please upload a video file.")

    # Display uploaded videos in the directory
    st.subheader("Uploaded Videos")
    uploaded_files = os.listdir(UPLOAD_DIR)
    if uploaded_files:
        for video_file in uploaded_files:
            st.write(video_file)
    else:
        st.write("No videos uploaded yet.")

