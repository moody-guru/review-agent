import streamlit as st
import requests
import pandas as pd
import datetime

# Page Configuration
st.set_page_config(
    page_title="Lyzr AI Intern Challenge",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for "Production" look
st.markdown("""
    <style>
    .metric-card {background-color: #f0f2f6; padding: 20px; border-radius: 10px;}
    .stDataFrame {border-radius: 10px;}
    </style>
    """, unsafe_allow_html=True)

# Sidebar Info
with st.sidebar:
    
    st.header("Backend Intern Challenge")
    st.markdown("**Developer:** Pushkar Sahu")
    st.markdown("[🔗 LinkedIn Profile](https://www.linkedin.com/in/pushkar-273616298/)")
    
    st.divider()
    st.markdown("### 🟢 System Status")
    if st.button("PING SERVER"):
        try:
            resp = requests.get("http://localhost:8000/logs")
            if resp.status_code == 200:
                st.success("Backend is Online 🟢")
            else:
                st.warning(f"Backend Returned {resp.status_code} 🟠")
        except:
            st.error("Backend Offline 🔴")

# Main Title
st.title("🤖 Automated Pull Request Review Agent")
st.markdown("Monitoring GitHub repositories for code changes and generating real-time AI feedback.")
st.divider()

# --- ROBUST DATA FETCHING ---
data = []
try:
    response = requests.get("http://localhost:8000/logs")
    if response.status_code == 200:
        json_data = response.json()
        # Check if we actually got a list
        if isinstance(json_data, list):
            data = json_data
        else:
            st.warning(f"⚠️ Backend returned unexpected format: {json_data}")
    else:
        st.error(f"❌ Backend Error: {response.status_code}")
except Exception as e:
    st.error(f"❌ Connection Error: Is 'uvicorn' running? ({e})")

# --- METRICS SECTION ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total PRs Reviewed", value=len(data))

with col2:
    # Safe access to the first item
    if data and isinstance(data, list) and len(data) > 0:
        last_status = data[0].get('status', 'Unknown')
    else:
        last_status = "Waiting..."
    st.metric(label="Last Review Status", value=last_status)

with col3:
    # Safe summation
    if data and isinstance(data, list):
        lines = sum([d.get('lines_analyzed', 0) for d in data])
    else:
        lines = 0
    st.metric(label="Total Lines Processed", value=lines)

st.divider()

# --- ACTIVITY FEED ---
st.subheader("📡 Live Activity Feed")

if st.button("🔄 Refresh Data", type="primary"):
    st.rerun()

if not data:
    st.info("Waiting for incoming webhooks... (Create a PR to start)")
else:
    # Display nice cards for each review
    for item in data:
        # Use .get() to avoid KeyErrors if fields are missing
        timestamp = item.get('timestamp', 'N/A')
        pr_id = item.get('pr_id', '?')
        repo = item.get('repo', 'Unknown Repo')
        status = item.get('status', 'Unknown')
        summary = item.get('summary', 'No summary provided.')
        lines_count = item.get('lines_analyzed', 0)

        with st.expander(f"{timestamp} | PR #{pr_id} in {repo} {status}"):
            c1, c2 = st.columns([1, 3])
            with c1:
                st.write(f"**Repo:** `{repo}`")
                st.write(f"**Lines Analyzed:** `{lines_count}`")
            with c2:
                st.markdown("### 📝 AI Review Summary")
                st.markdown(summary)