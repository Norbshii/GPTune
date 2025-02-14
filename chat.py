import streamlit as st
import os
import google.generativeai as genai
import time

# Load API key from environment variable
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    st.error("Please set the GOOGLE_API_KEY environment variable with your Gemini API key.")
    exit()

# Configures the Gemini API with the obtained API key.
genai.configure(api_key=API_KEY)

# Check if a chat session exists, if not, initialize a new one.
if 'chat_session' not in st.session_state:
    model = genai.GenerativeModel('gemini-1.5-pro')
    st.session_state.chat_session = model.start_chat()
    st.session_state.chat_history = []  # Initialize chat history

def handle_chat(name, emotion, situation, message_type):
    # Tailored question to prompt concise, quote-like responses
    question = f"Generate a short motivational quote for someone feeling {emotion}, dealing with {situation}, who needs {message_type}."
    try:
        response = st.session_state.chat_session.send_message(question)
        # Directly deliver the motivational quote
        intro_response = f"Hello {name}, here's a motivational quote just for you:"
        full_response = f"{intro_response} '{response.text}'"
        st.session_state.chat_history.append({"type": "Question", "content": question})
        st.session_state.chat_history.append({"type": "Response", "content": full_response})
        return full_response
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        time.sleep(1)
        return "An error occurred. Please try again."

def display_history():
    with st.container():
        for entry in st.session_state.chat_history:
            if entry['type'] == "Question":
                st.markdown(f"<p style='font-size:16px; font-weight:bold;'>Your Inquiry:</p><p style='font-size:16px;'>{entry['content']}</p>", unsafe_allow_html=True)
            elif entry['type'] == "Response":
                st.markdown(f"<p style='font-size:16px; font-weight:bold;'>Response from Illya:</p><p style='font-size:16px;'>{entry['content']}</p>", unsafe_allow_html=True)

st.set_page_config(page_title="Illya - Motivational Quote Bot")
st.header("Illya - Personalized Motivation Generator")

user_name = st.text_input("Enter your name:")
emotional_states = ['Happy', 'Sad', 'Anxious', 'Excited', 'Stressed', 'Hopeful']
situations = ['Dealing with a challenge', 'Celebrating a success', 'Feeling lost', 'In love']
message_types = ['Encouragement', 'Comfort', 'Motivation', 'Celebration', 'Understanding']
user_emotion = st.selectbox("How are you feeling today?", emotional_states)
user_situation = st.selectbox("What's your current situation?", situations)
user_message_type = st.selectbox("What kind of message would you like to hear?", message_types)

if st.button("Get Personalized Quote"):
    if user_name:
        response_text = handle_chat(user_name, user_emotion, user_situation, user_message_type)
        display_history()
    else:
        st.warning("Please enter your name to get a personalized quote.")

if st.button("Reset Conversation"):
    st.session_state.chat_session = model.start_chat()
    st.session_state.chat_history = []  # Clear the history
