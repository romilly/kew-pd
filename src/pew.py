import json
from datetime import datetime
from uuid import uuid4

from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

from pew.chat.chat_record import ChatRecord
from pew.chat.sqlite_chat_record_library import SQLiteChatRecordLibrary
import os

from pew.helpers.convert_chat_completion import serialize_chat_completion

# Run chat with OpenAI and record prompts, responses
load_dotenv(os.path.join(os.getcwd(),'.env')) #neded because of the wat streamlit apps are run
base_url = os.environ["BASE_URL"]
api_key = os.environ["API_KEY"]
model = os.environ["MODEL"]
st.title("PEW")
st.caption("Prompt Engineering Workbench")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
recorder = SQLiteChatRecordLibrary('../data/chats.db')
client = OpenAI(base_url=base_url, api_key=api_key)
if prompt := st.chat_input(key='chat_input'):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model=model, messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
    record = ChatRecord(uuid4(), datetime.now(), 'xavier', prompt, json.dumps(serialize_chat_completion(response)))
    recorder.add_record(record.id, record)
