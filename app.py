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
# CRITICAL FIX: We will replace this dummy URL with your real Make.com webhook URL in Step 2
MAKE_WEBHOOK_URL = "https://make.com"

# --- 3. CUSTOM CSS BRAND VISUAL ANCHORS ---
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
st.caption("Powered by Make.com Cloud Orchestrator, Free Hugging Face AI Models, and Streamlit")
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
        with st.spinner("Executing Pipeline: Fetching responses from Cloud AI Engine..."):
            try:
                # Construct safe structural data payload packet
                payload = {"query": user_query}
                headers = {"Content-Type": "application/json"}

                # Execute REST API POST transaction call to Make.com cloud engine
                if "your-unique-webhook-id" in MAKE_WEBHOOK_URL:
                    st.warning("Configuration Notice: You need to paste your real Make.com URL into line 15 of your app.py file.")
                else:
                    api_response = requests.post(MAKE_WEBHOOK_URL, data=json.dumps(payload), headers=headers, timeout=60)

                    # Verify server state responses
                    if api_response.status_code == 200:
                        raw_data = api_response.json()

                        # Pull output data token string dynamically matching Make.com response structure
                        final_ai_answer = raw_data.get("output", "Pipeline warning: System generated a blank data array payload.")

                        # Update cache state histories
                        st.session_state.conversation_history.append({"prompt": user_query, "reply": final_ai_answer})

                        # Render contextual UI output blocks
                        st.markdown("### ⚡ Pipeline Response Executed Successfully:")
                        st.markdown(f'<div class="response-box">{final_ai_answer}</div>', unsafe_allow_html=True)

                    else:
                        st.error(f"Cloud Server Failure: Pipeline responded with error status code {api_response.status_code}. Verify Make.com scenario states.")

            except requests.exceptions.Timeout:
                st.error("System Network Interruption Error: Connection request reached server timeout constraints.")
            except requests.exceptions.ConnectionError:
                st.error("Pipeline Failure: Streamlit was completely unable to reach your Make.com endpoint URL. Please check your internet connection and webhook status.")
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
