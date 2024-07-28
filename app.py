import json
import os
from services import bedrock_agent_runtime
import streamlit as st
import uuid

# Get config from environment variables
agent_id = "LYDKIM8W2B" #os.environ.get("BEDROCK_AGENT_ID")
agent_alias_id = "SJFWKM5FJR"#os.environ.get("BEDROCK_AGENT_ALIAS_ID", "TSTALIASID") # TSTALIASID is the default test alias ID
ui_title = "🚀InvestRock - Mutual Fund AI assistant🤖\n" #os.environ.get("BEDROCK_AGENT_TEST_UI_TITLE", "Agents for Amazon Bedrock Test UI")
ui_icon = ":favicon-logo.png" #os.environ.get("BEDROCK_AGENT_TEST_UI_ICON") 

def init_state():
    st.session_state.session_id = str(uuid.uuid4())
    st.session_state.messages = []
    st.session_state.citations = []
    st.session_state.trace = {}

# General page configuration and initialization
st.set_page_config(page_title=ui_title, page_icon=ui_icon, layout="wide", menu_items={'Get Help': 'mailto:sudarkodimuthiah22@gmail.com',
        'Report a bug': "https://github.com/Sudarkodi-Muthiah-repo/amazon-bedrock-agent-test-ui/issues",
        'About': "# This is an AI assistant for mutual fund\n\n"})
st.title(ui_title)
st.subheader("Welcome to InvestRock!👩‍💻 Would you like to explore our list of mutual funds, or do you have specific investment💵💸 goals in mind for creating a diversified portfolio? I am a helpful chat assistant. How can I help you?")
html_chat = '<center><h6>🤗 This project is done by Sudarkodi Muthiah 🤗</h6>'
st.markdown(html_chat,unsafe_allow_html=True)
st.write('Contact me [Sudarkodi](https://www.linkedin.com/in/sudarkodi-muthiah/)')

if len(st.session_state.items()) == 0:
    init_state()

# Messages in the conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

# Chat input that invokes the agent
if prompt := st.chat_input("Ask anything about Mutualfunds"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        with st.spinner("🤖InvestRock is thinking..."):
            response = bedrock_agent_runtime.invoke_agent(
            agent_id,
            agent_alias_id,
            st.session_state.session_id,
            prompt
        )
        output_text = response["output_text"]

        placeholder.markdown(output_text, unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": output_text})
      