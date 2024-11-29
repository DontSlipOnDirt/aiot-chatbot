import streamlit as st
from streamlit_chat import message

# Initialize session state for OpenAI token and messages
if "openai_token" not in st.session_state:
    st.session_state.openai_token = ""
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Chatbot")

# Sidebar section for OpenAI token input
token_input = st.sidebar.text_input(
    "Enter your OpenAI Token",
    type="password",
    placeholder="sk-...",
    help="Input your OpenAI API token here to use the chatbot."
)

# Save token in session state
if token_input:
    st.session_state.openai_token = token_input
    st.sidebar.success("Token saved successfully!")

# Chatbot interface
user_input = st.text_input("You:", placeholder="Type your message here...")

# Display chat messages
for i, msg in enumerate(st.session_state.messages):
    if i % 2 == 0:
        message(msg, is_user=True)  # User messages
    else:
        message(msg)  # Bot messages

# Handle user input
if user_input and st.session_state.openai_token:
    st.session_state.messages.append(user_input)
    
    # Placeholder response from chatbot
    # Replace this with actual API call to OpenAI
    response = f"This is a placeholder response to: {user_input}"
    
    st.session_state.messages.append(response)
    st.experimental_rerun()
elif user_input and not st.session_state.openai_token:
    st.error("Please enter your OpenAI token in the sidebar before chatting.")