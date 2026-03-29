from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
load_dotenv()


st.set_page_config(
    page_title="Groq Chatbot",
    page_icon="🤖",
    layout="wide",
)

st.title("Groq Chatbot")


if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []


for message in st.session_state["chat_history"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=None,
)
prompt= st.chat_input("Ask Groq Chatbot")

if prompt:
   st.chat_message("user").markdown(prompt)
   st.session_state["chat_history"].append({"role":"user","content":prompt})
   response= llm.invoke(input=[{"role":"system","content":"you are helpful assistant"},*st.session_state.chat_history])
   responseContent= response.content
   st.session_state["chat_history"].append({"role":"assistant","content":responseContent})
   with st.chat_message("assistant"):
       st.markdown(responseContent)

