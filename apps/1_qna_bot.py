from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

import streamlit as st

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

st.title("ASKbuddy QnA Bot")
st.markdown(" This is a simple QnA bot that uses the Google Gemini API to answer questions. Type your question below and press Enter to get an answer. Type 'exit', 'quit', or 'bye' to end the chat.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)
 
query = st.chat_input("Type your question here...")
if query:
    st.session_state.messages.append({"role": "user" , "content": query})
    st.chat_message("user").markdown(query)
    result = llm.invoke(query)
    st.chat_message("ai").markdown(result.content[0]["text"])    
    st.session_state.messages.append({"role": "ai" , "content": result.content[0]["text"]})

while True:
    que = input("User: ")

    if que.lower() in ["exit", "quit" , 'bye']:
        print("Exiting the chat...")
        break

    result = llm.invoke(que)
    print("AI: " , result.content[0]["text"] , "\n\n")