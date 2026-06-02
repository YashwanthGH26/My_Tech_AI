import streamlit as st
import requests
import json

# --- 1. APP INITIALIZATION & SECURITY SETUP ---
st.set_page_config(
    page_title="TechAI Engine | Enterprise Q&A",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. BACKEND API ROUTING CONSTANTS ---
# Replace this with your exact local or deployed production n8n webhook URL link
N8N_WEBHOOK_URL = "http://localhost:5678/webhook/ask-tech-ai"

# --- 3. CUSTOM CSS BRAND VISUAL ANCHORS ---
# CRITICAL FIX: Changed 'unsafe_style_allowed=True' to 'unsafe_allow_html=True'
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 6px;
        width: 100%;
        font-weight: bold;
    }
    .stTextInput>div>div>input { background-color: #262730; color: white; }
    .response-box {
        background-color: #1e1e24;
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid #ff4b4b;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR LOGIC & ZERO-COST FREEMIUM MANAGEMENT ---
with st.sidebar:
    st.title("⚙️ Access Control")
    st.markdown("### Tier Status: **Free Tier**")
    st.info("You have 5 free queries remaining for today.")

    st.markdown("---")
    st.markdown("### 💎 Go Premium")
    st.markdown("Unlock Unlimited Infrastructure access, Deep Dev-RAG search, and Advanced Code Generation.")

    # Zero-Cost Monetization Redirects
    if st.button("Upgrade to Premium Pro ($0/mo Trial)"):
        st.success("Redirecting safely to our payment checkout gateway...")
        st.markdown("[Click here to activate your Stripe payment gateway session](https://buymeacoffee.com)")

# --- 5. CORE UI LAYOUT HEADERS ---
st.title("💻 TechAI Contextual Engine")
st.caption("Powered by Agentic n8n Orchester, Vector RAG Datastores, and Model Context Protocols (MCP)")
st.write("Submit complex technical queries, source script fragments, or architectural infrastructure debugging constraints below.")

# --- 6. STATE HANDLING FOR SEAMLESS CHAT ARCHIVING ---
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Input Interface Block
user_query = st.text_input("Enter your engineering or code query here:",
                           placeholder="e.g., Debug this Dockerfile multi-stage memory leak or write a Kubernetes YAML network policy...")
submit_action = st.button("Execute Pipeline Request")

# --- 7. APPLIED RUNTIME INTEGRATION ENGINE ---
if submit_action:
    if not user_query.strip():
        st.error("Validation Error: Please write a valid input text string prompt before processing execution.")
    else:
        with st.spinner("Executing Pipeline: Querying Vector Stores and Compiling Response via MCP..."):
            try:
                # Construct safe structural data payload packet
                payload = {"query": user_query}
                headers = {"Content-Type": "application/json"}

                # Execute REST API POST transaction call to n8n pipeline workflow engine
                api_response = requests.post(N8N_WEBHOOK_URL, data=json.dumps(payload), headers=headers, timeout=60)

                # Verify server state responses
                if api_response.status_code == 200:
                    raw_data = api_response.json()

                    # Pull output data token string dynamically matching n8n structure logic
                    final_ai_answer = raw_data.get("output", "Pipeline warning: System generated a blank data array payload.")

                    # Update cache state histories
                    st.session_state.conversation_history.append({"prompt": user_query, "reply": final_ai_answer})

                    # Render contextual UI output blocks
                    st.markdown("### ⚡ Pipeline Response Executed Successfully:")
                    st.markdown(f'<div class="response-box">{final_ai_answer}</div>', unsafe_allow_html=True)

                else:
                    st.error(f"Backend Server Failure: Pipeline responded with error status code {api_response.status_code}. Verify n8n workflow listening states.")

            except requests.exceptions.Timeout:
                st.error("System Network Interruption Error: Connection request reached server timeout constraints.")
            except requests.exceptions.ConnectionError:
                st.error("Pipeline Failure: Streamlit was completely unable to reach your backend local n8n gateway port (http://localhost:5678). Please make sure Docker and n8n are actively running.")
            except Exception as system_error:
                st.error(f"An unexpected exception error structural state occurred: {str(system_error)}")

# --- 8. HISTORICAL CONTEXT RENDERING ---
if st.session_state.conversation_history:
    st.markdown("---")
    st.subheader("📚 Active Session Chat Cache Logs")
    for logged_chat in reversed(st.session_state.conversation_history):
        with st.expander(f"Prompt Log Trace: {logged_chat['prompt'][:60]}..."):
            st.markdown(f"**Your Request:** {logged_chat['prompt']}")
            st.markdown(f"**AI Engine Output:** {logged_chat['reply']}")
