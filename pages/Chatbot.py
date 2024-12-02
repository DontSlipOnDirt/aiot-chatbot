import streamlit as st
from openai import OpenAI

# Initialize session state for OpenAI token and messages
if "openai_token" not in st.session_state:
    st.session_state.openai_token = ""
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are J.R.R. Tolkien and you can only speak in the style of the silmarillion. Your knowledge only goes up to 1973. Utilize any prior knowledge about J.R.R. Tolkien to accurately simulate him."}
    ]

# Sidebar: Input OpenAI token
st.sidebar.title("OpenAI API Key")
token_input = st.sidebar.text_input(
    "Enter your OpenAI API key",
    type="password",
    placeholder="sk-...",
    help="Provide your OpenAI API key to use the chatbot."
)

if token_input:
    st.session_state.openai_token = token_input
    st.sidebar.success("API key saved!")

# Chat interface
st.title("Chatbot")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if user_input := st.chat_input("Type your message here..."):
    if st.session_state.openai_token:

        client = OpenAI(api_key=token_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)
        response = client.chat.completions.create(model="gpt-4o-mini", messages=st.session_state.messages)
        msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)

    else:
        st.error("Please enter your OpenAI API key in the sidebar.")