import streamlit as st

st.markdown("""
            
        # Intro
        Welcome to my chatbot for the AI of things class.
        The GitHub repo can be found here https://github.com/DontSlipOnDirt/aiot-chatbot. 

        # Chatbot Persona Definition
        The chatbot is meant to replicate the writing style of J.R.R. Tolkien and more specifically his book the *Silmarillion*. As a brief recap, the *Silmarillion* is essentially a book detailing the history of Middle-Earth, the setting of the *Lord of the Rings* trilogy. Tolkien's writing style is lengthy and resembles that of recounting legendary myths and fables. Because his writing style is so decorative, there would often be long paragraphs with many intricate details, similes and metaphors.
        
        # Technical Approach
        The only used language to write this is Python. For this interface, I used the popular library Streamlit. The LLM calls all use the OpenAI API's gpt-4o-mini chatbot model, which does require an OpenAI API key for access. Thankfully, 4o mini is a relatively cheap model, so there should be minimal charges for any interactions with this chatbot. I handle the interactions with the LLM and the prompting with LangChain as I initially thought it may be a more complicated project then I originally thought. However, it is still convenient to work with LangChain not only because I am familiar with it but also because it has many useful features that can impprove this chatbot in the future.
        
        # Response Workflow Design
        ![Diagram of Flow of Chatbot](diagram.png)
        1. System prompts LLM with how to speak.
        2. User sends message which is added to the conversation.
        3. LLM is prompted with system prompt and conversation.
        4. LLM responds and its message is added to the conversation.
            
        # Prompt Engineering
        The prompt can be found on the chatbot page at the top after the 'S' symbol which stands for system. The prompt simply instructs the AI to simulate Tolkien's writing style in his book the *Silmarillion*. This leads to lengthy answers that mimic fables set in the *Lord of the Rings* world.
            
        # Memory and Context Handling
        The memory only contains the current conversations history because this app requires you to input your own OpenAI API key with each conversation. I achieve this by simply using Streamlit's message handling and passing it with the prompt to the LLM. This effectively passes the entire current conversation to the LLM as context. I tested this by having a conversation with it and it was able to correctly recall previously discussed topics. 
         """)