import streamlit as st
from openai import OpenAI

# Initialize session state for storing OpenAI token and messages
if "openai_token" not in st.session_state:
    st.session_state.openai_token = ""
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant that only talks in American slang."}  # Initial system message
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

# Display chat history using streamlit.chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if user_input := st.chat_input("Type your message here..."):
    # Append user input to the conversation
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate a response if OpenAI token is provided
    if st.session_state.openai_token:
        try:
            client = OpenAI(api_key=st.session_state.openai_token)

            if "openai_model" not in st.session_state:
                st.session_state["openai_model"] = "gpt-3.5-turbo"

            if "messages" not in st.session_state:
                st.session_state.messages = []

            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

        except Exception as e:
            bot_message = f"Error: {e}"

        # Append bot response to the conversation
        if prompt := st.chat_input("What is up?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                stream = client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    stream=True,
                )
                response = st.write_stream(stream)
            st.session_state.messages.append({"role": "assistant", "content": response})
        # st.session_state.messages.append({"role": "assistant", "content": bot_message})
        # with st.chat_message("assistant"):
        #     st.markdown(bot_message)
    else:
        st.error("Please enter your OpenAI API key in the sidebar.")
