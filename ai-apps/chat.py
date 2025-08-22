from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate   

from dotenv import load_dotenv
import streamlit as st

load_dotenv()

#prompt Template
prompt_template = PromptTemplate.from_template("""""")


model = ChatGroq(model="openai/gpt-oss-20b")# try this model  as well.  deepseek-r1-distill-llama-70b
parser = StrOutputParser()
chain = model | parser


st.title("AI Chat App")

# Application state that will be available after the app refresh
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Iterate over the chat history and show each message
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])


user_msg = st.chat_input("type here...")

if user_msg:
    # add the user message to the chat history list
    st.session_state.chat_history.append({"role": "user", "content": user_msg})
    
    with st.chat_message("user"):
        st.write(user_msg)
    
    #invoke model
    result = chain.invoke(st.session_state.chat_history)

    # add the AI message to the chat history list
    #st.session_state.chat_history.append({"role": "ai", "content": "how may i help you?"})
    st.session_state.chat_history.append({"role": "ai", "content": result})
    with st.chat_message("ai"):
        #st.write("how may i help you?")
        st.write(result)
    print(st.session_state.chat_history)
    