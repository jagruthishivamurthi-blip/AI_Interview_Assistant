import streamlit as st
from groq import Groq
st.set_page_config(page_title = "About Me",page_icon='😎',layout='centered')
st.title("AI Placement Assistance")
st.caption("Practice and prepare for your Interview")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (keyError,FileNoteFound):  
  st.error("API key is missing. Add it in Advanced Settings")
  st.stop()
  
