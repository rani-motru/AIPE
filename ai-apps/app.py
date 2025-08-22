from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")# try this model  as well.  deepseek-r1-distill-llama-70b
parser = StrOutputParser()
chain = model | parser

# displays some text in the app
st.title("AI App with Langchain")
st.divider()

# Sidebar
with st.sidebar:
    st.markdown("### Settings")
    
    temp = st.slider("Temperature", min_value=0.0, max_value=1.0)
    
    stream = st.toggle("Stream")

# if not st.user.is_logged_in:
#     if st.button("Log in"):
#         st.login()
# else:
#     if st.button("Log out"):
#         st.logout()
#     st.write(f"Hello, {st.user.name}!")

# displays a text input
user_prompt = st.text_input("Write your prompt...")

# create the model
model = ChatGroq(model="openai/gpt-oss-20b")

# create parser
parser = StrOutputParser()

# create a chain
chain = model | parser

# invoke the chain with the user prompt
completion = chain.invoke(user_prompt)

print(completion)
st.write(completion)
