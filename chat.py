import streamlit as st
import os
import google.generativeai as genai

# Assume API_KEY and model configuration are the same as your provided code
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

# Define music preferences options
moods = ['Happy', 'Sad', 'Energetic', 'Relaxed']
genres = ['Pop', 'Rock', 'Jazz', 'Electronic', 'Classical']
feelings = ['Stressed', 'Excited', 'Melancholic', 'Cheerful']

# Initialize session state for song suggestions if not already set
if 'song_suggestions' not in st.session_state:
    st.session_state.song_suggestions = []

def fetch_songs(mood, genre, feeling):
    # This function would interact with the music database or API to get songs
    # Placeholder for song fetching logic
    songs = [f"{mood} {genre} song 1", f"{mood} {genre} song 2", f"{mood} {genre} song 3"]
    return songs

# Streamlit user interface for song selection
st.title("Music Mood Suggester")
user_mood = st.selectbox("Select your mood:", moods)
user_genre = st.selectbox("Select your favorite genre:", genres)
user_feeling = st.selectbox("What are you feeling right now?", feelings)

if st.button("Get Song Suggestions"):
    suggested_songs = fetch_songs(user_mood, user_genre, user_feeling)
    st.session_state.song_suggestions = suggested_songs
    st.write("Here are some songs that might match your mood:")
    for song in suggested_songs:
        st.write(song)

# Resetting suggestions
if st.button("Reset Suggestions"):
    st.session_state.song_suggestions = []
