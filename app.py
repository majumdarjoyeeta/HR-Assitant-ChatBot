# frontend/app.py

import streamlit as st
import requests

st.set_page_config(page_title="HR Assistant Chatbot", layout="wide")
st.title("🤖 HR Assistant Chatbot")

# Sidebar: Upload Job Description
st.sidebar.header("📄 Upload Job Description")
st.sidebar.write("Upload a `.txt` file containing the job description.")
uploaded_file = st.sidebar.file_uploader("Choose a JD file", type=["txt"])
if uploaded_file is not None:
    try:
        response = requests.post("http://localhost:5000/upload_jd", files={"file": uploaded_file})
        if response.status_code == 200:
            st.sidebar.success("✅ Job description uploaded successfully!")
        else:
            st.sidebar.error("❌ Failed to upload JD: " + response.text)
    except Exception as e:
        st.sidebar.error("⚠️ Error connecting to backend: " + str(e))

# Chat Interface
st.header("💬 Ask Your HR Questions")
st.caption("Ask about qualifications, skills, or general HR queries. You can enter multiple questions using 'and', 'then', or 'but'.")
user_input = st.text_input("Enter your HR-related query:")

if st.button("📝 Send") and user_input:
    st.session_state.setdefault("chat_history", []).append(("You", user_input))
    payload = {"message": user_input}
    backend_url = "http://localhost:5000/chat"
    try:
        response = requests.post(backend_url, json=payload)
        if response.status_code == 200:
            data = response.json()
            st.success("🧠 AI processed your query. Here's the breakdown:")
            for seg in data["segments"]:
                st.markdown(f"### ➤ Segment: `{seg['segment']}`")
                st.markdown(f"**Detected Intents:** {', '.join(seg['intents'])}")
                for intent, resp in seg["responses"].items():
                    st.markdown(f"#### 🗣 {intent.upper()} Response:")
                    st.markdown(f"> {resp}")
                    st.session_state.setdefault("chat_history", []).append((intent.upper(), resp))
                st.markdown("---")
        else:
            st.error("❌ Backend error: " + response.text)
    except Exception as e:
        st.error("⚠️ Error connecting to backend: " + str(e))

# Display Chat History
st.subheader("🕓 Chat History")
for sender, message in reversed(st.session_state.get("chat_history", [])):
    color = "#d4edda" if sender == "You" else "#f1f1f1"
    st.markdown(
        f"<div style='background-color: {color}; padding: 10px; margin-bottom: 10px; border-radius: 10px;'>"
        f"<strong>{sender}:</strong><br>{message}</div>",
        unsafe_allow_html=True
    )
