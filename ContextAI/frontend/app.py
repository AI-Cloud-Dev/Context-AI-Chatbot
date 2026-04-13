import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="ContextAI", layout="wide")
st.title("🧠 ContextAI Chatbot")

# ---------------- SESSION STATE ----------------
if "token" not in st.session_state:
    st.session_state.token = None

if "mode" not in st.session_state:
    st.session_state.mode = "login"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "chat_input" not in st.session_state:
    st.session_state.chat_input = ""


# ---------------- NAVIGATION ----------------
if not st.session_state.token:
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login Page", key="nav_login"):
            st.session_state.mode = "login"

    with col2:
        if st.button("Register Page", key="nav_register"):
            st.session_state.mode = "register"


# =====================================================
# REGISTER
# =====================================================
if st.session_state.mode == "register" and not st.session_state.token:

    st.subheader("📝 Register")

    reg_email = st.text_input("Email", key="reg_email")
    reg_password = st.text_input("Password", type="password", key="reg_password")

    if st.button("Create Account", key="register_btn"):

        if not reg_email or not reg_password:
            st.error("Email and password required")
        else:
            try:
                res = requests.post(f"{API_URL}/auth/register", json={
                    "email": reg_email,
                    "password": reg_password
                })

                if res.status_code == 200:
                    st.success("User created successfully!")
                    st.session_state.mode = "login"
                else:
                    st.error(res.json().get("detail", "Registration failed"))

            except Exception as e:
                st.error(f"Server error: {str(e)}")


# =====================================================
# LOGIN
# =====================================================
if st.session_state.mode == "login" and not st.session_state.token:

    st.subheader("🔐 Login")

    email = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login", key="login_btn"):

        if not email or not password:
            st.error("Email and password required")
        else:
            try:
                res = requests.post(f"{API_URL}/auth/login", json={
                    "email": email,
                    "password": password
                })

                if res.status_code == 200:
                    st.session_state.token = res.json()["access_token"]
                    st.session_state.mode = "chat"
                    st.success("Logged in successfully!")
                    st.rerun()
                else:
                    st.error(res.json().get("detail", "Login failed"))

            except Exception as e:
                st.error(f"Server error: {str(e)}")


# =====================================================
# CHAT PAGE
# =====================================================
if st.session_state.token and st.session_state.mode == "chat":

    headers = {"Authorization": f"Bearer {st.session_state.token}"}

    st.success("Authenticated ✔")

    # ---------------- LOGOUT ----------------
    if st.button("Logout", key="logout_btn"):
        st.session_state.token = None
        st.session_state.mode = "login"
        st.session_state.chat_history = []
        st.session_state.chat_input = ""
        st.rerun()


    # =====================================================
    # UPLOAD SECTION
    # =====================================================
    st.subheader("📄 Upload Document")

    file = st.file_uploader("Upload PDF / DOCX / XLSX", key="file_upload")

    if file:
        if st.button("Upload File", key="upload_btn"):
            try:
                with st.spinner("Uploading..."):
                    res = requests.post(
                        f"{API_URL}/api/upload",
                        files={"file": file},
                        headers=headers
                    )

                if res.status_code == 200:
                    st.success("File uploaded successfully!")
                else:
                    st.error(res.json().get("detail", "Upload failed"))

            except Exception as e:
                st.error(f"Upload error: {str(e)}")


    # =====================================================
    # CHAT SECTION
    # =====================================================
    # ---------------- CHAT SECTION ----------------
st.subheader("💬 Chat with ContextAI")

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask something")

    submitted = st.form_submit_button("Send")

if submitted:
    if not user_input.strip():
        st.warning("Please enter a message")
    else:
        try:
            with st.spinner("Thinking..."):
                res = requests.post(
                    f"{API_URL}/api/chat",
                    json={"message": user_input},
                    headers=headers
                )

            if res.status_code == 200:
                answer = res.json()["response"]

                st.session_state.chat_history.append(("user", user_input))
                st.session_state.chat_history.append(("ai", answer))

            else:
                st.error(res.json().get("detail", "Chat failed"))

        except Exception as e:
            st.error(f"Chat error: {str(e)}")


    # =====================================================
    # CHAT DISPLAY (ChatGPT style)
    # =====================================================
    st.divider()
    st.subheader("🧾 Conversation")

    for role, msg in st.session_state.chat_history:

        if role == "user":
            with st.chat_message("user"):
                st.write(msg)
        else:
            with st.chat_message("assistant"):
                st.write(msg)