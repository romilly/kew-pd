from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

from pew.chat.sqlite_recorder import SQLiteChatRecorder
import os

# Run chat with OpenAI and record prompts, respnses

load_dotenv()
api_key = os.environ["OPENAI_API_KEY"]
st.title("PEW")
st.caption("Prompt Engineering Workbench")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
recorder = SQLiteChatRecorder('/home/romilly/git/active/streamlit_spikes/data/chats.db')
client = OpenAI(api_key=api_key)
model = "gpt-3.5-turbo"
if prompt := st.chat_input(key='chat_input'):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model=model, messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
    recorder.add_record('localhost', {'model': model, 'user_input': prompt, 'response': msg})
