import streamlit as st

st.markdown("""
            
        # Intro
        Welcome to my chatbot for the AI of things class.
        The GitHub repo can be found here https://github.com/DontSlipOnDirt/aiot-chatbot. 

        # Chatbot Persona Definition
        The chatbot is meant to replicate the writing style of J.R.R. Tolkien and more specifically his book the *Silmarillion*. As a brief recap, the *Silmarillion* is essentially a book detailing the history of Middle-Earth, the setting of the *Lord of the Rings* trilogy. Tolkien's writing style is lengthy and resembles that of recounting legendary myths and fables. Because his writing style is so decorative, there would often be long paragraphs with many intricate details, similes and metaphors.
        
        # Technical Approach
        The only used language to write this is Python. For this interface, I used the popular library Streamlit. The LLM calls all use the OpenAI API's gpt-4o-mini chatbot model, which does require an OpenAI API key for access. Thankfully, 4o mini is a relatively cheap model, so there should be minimal charges for any interactions with this chatbot.
        
        # Response Workflow Design
        1. System prompt with instructions on how to act to LLM
        2. 
            
        # Prompt Engineering
        The prompt can be found on the chatbot page at the top after the 'S' symbol which stands for system. The prompt simply instructs the AI to simulate Tolkien's writing style in his book the *Silmarillion*. This leads to lengthy answers that mimic fables set in the *Lord of the Rings* world.
            
        # Memory and Context Handling
        The memory is handled using LangChains library. This memory works by... # TODO    
            
        # Additionals
        
        
         """)