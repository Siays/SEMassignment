import streamlit as st
import database_interaction

def main():
    st.title("Showcase Corner")
    st.write("Welcome to the Showcase Corner!")
    video= database_interaction.retrieve_file_from_firebase("db/videos/crazy_frog.mp4")
    st.video(video)



