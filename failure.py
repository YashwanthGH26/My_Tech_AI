import streamlit as st
import requests

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="TechAI Engine", page_icon="💻", layout="wide")

# PASTE YOUR EXACT MAKE.COM URL HERE (Make sure it has no spaces or typos)
MAKE_WEBHOOK_URL = "https://make.com"

# --- 2. THE INTERFACE ---
st.title("💻 TechAI Contextual Engine")
st.write("Submit your question below:")

user_query = st.text_input("Enter your engineering or code query here:", placeholder="Type here...")
submit_action = st.button("Execute Pipeline Request")

# --- 3. EXECUTING CONNECTION ENGINE ---
if submit_action:
    if not user_query.strip():
        st.error("Please enter a valid question.")
    else:
        with st.spinner("Connecting to server..."):
            try:
                # Direct JSON data structure passing
                data_packet = {"query": user_query}
                
                # Posting standard data without complex custom header fields to bypass 403 filters
                api_response = requests.post(MAKE_WEBHOOK_URL, json=data_packet, timeout=30)
                
                if api_response.status_code == 200:
                    # Handle raw text or JSON flexibly to avoid crash failures
                    try:
                        raw_data = api_response.json()
                        final_answer = raw_data.get("output", str(raw_data))
                    except:
                        final_answer = api_response.text
                    
                    st.success("Successfully executed:")
                    st.info(final_answer)
                else:
                    st.error(f"Server Error Code: {api_response.status_code}. Read Step 2 below to fix this setting inside Make.com.")
            
            except Exception as system_error:
                st.error(f"System Error: {str(system_error)}")
