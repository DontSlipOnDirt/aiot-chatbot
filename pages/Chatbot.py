import streamlit as st
from openai import OpenAI

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

prompt = "You are J.R.R. Tolkien and you can only speak in the style of the silmarillion. Utilize any prior knowledge about J.R.R. Tolkien to accurately simulate him."

# Initialize session state for OpenAI token and messages
if "openai_token" not in st.session_state:
    st.session_state.openai_token = ""
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": prompt}
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

        # llm = ChatOpenAI(temperature=0, model="gpt-4o-mini", api_key=token_input)
        # prompt_template = ChatPromptTemplate.from_messages(
        #     [("system", prompt), ("user", "{text}")]
        # )

        # llm.invoke([{"role": "system", "content": prompt}])
        # st.session_state.messages.append({"role": "user", "content": user_input})
        # st.chat_message("user").write(user_input)
        # response = llm.invoke(user_input)
        # msg = response.content
        # st.session_state.messages.append({"role": "assistant", "content": msg})
        # st.chat_message("assistant").write(msg)

        # Plain OpenAI 4o calls
        client = OpenAI(api_key=token_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)
        response = client.chat.completions.create(model="gpt-4o-mini", messages=st.session_state.messages)
        msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)

    else:
        st.error("Please enter your OpenAI API key in the sidebar.")