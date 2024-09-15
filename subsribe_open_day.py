import streamlit as st
import database_interaction

def main():
    st.title("Open Day Information")
    video= database_interaction.retrieve_file_from_firebase("db/videos/showCase.mp4")
    st.video(video)


