import streamlit as st

home = st.Page("pages/Home.py", title="Home", icon=":material/home:", default=True)
chatbot = st.Page("pages/Chatbot.py", title="Chatbot", icon=":material/sms:")

pg = st.navigation(
    [
        home,
        chatbot,
    ]
)

pg.run()