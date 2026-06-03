import streamlit as st
import sqlite3
import hashlib
import os

DB_PATH = "users.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    """Create the users table if it doesn't already exist."""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id       INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT    NOT NULL UNIQUE,
                password TEXT    NOT NULL
            )
        """)
        conn.commit()

def hash_password(password: str) -> str:
    """SHA-256 hash a plain-text password."""
    return hashlib.sha256(password.encode()).hexdigest()

def user_exists(username: str) -> bool:
    """Return True if the username is already taken."""
    with get_connection() as conn:
        row = conn.execute(
            "SELECT 1 FROM users WHERE username = ?", (username,)
        ).fetchone()
    return row is not None

def register_user(username: str, password: str) -> bool:
    """Insert a new user. Returns False on duplicate username."""
    try:
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hash_password(password)),
            )
            conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

init_db()


st.set_page_config(
    page_title="Sign Up",
    page_icon="🔐",
    layout="centered",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@700;800&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background: #0d0d0f;
    color: #e8e6df;
}

[data-testid="stAppViewContainer"] {
    font-family: 'DM Mono', monospace;
}

/* Remove default Streamlit padding */
.block-container {
    padding-top: 4rem !important;
    max-width: 460px !important;
}

h1 {
    font-family: 'Syne', sans-serif;
    font-size: 2.6rem !important;
    font-weight: 800;
    letter-spacing: -1px;
    color: #f5f0e8;
    margin-bottom: 0.2rem !important;
}

.subtitle {
    font-size: 0.78rem;
    color: #6b6860;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 2.4rem;
}

/* Input fields */
input[type="text"], input[type="password"] {
    background: #17171a !important;
    border: 1px solid #2e2e35 !important;
    border-radius: 6px !important;
    color: #e8e6df !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.9rem !important;
    transition: border-color 0.2s;
}
input[type="text"]:focus, input[type="password"]:focus {
    border-color: #c8a96e !important;
    box-shadow: 0 0 0 2px rgba(200,169,110,0.15) !important;
}

/* Labels */
label[data-testid="stWidgetLabel"] p {
    font-size: 0.72rem !important;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #6b6860 !important;
}

/* Button */
div.stButton > button {
    background: #c8a96e !important;
    color: #0d0d0f !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    border: none !important;
    border-radius: 6px !important;
    padding: 0.6rem 2rem !important;
    width: 100%;
    transition: background 0.2s, transform 0.1s;
}
div.stButton > button:hover {
    background: #dfc08a !important;
    transform: translateY(-1px);
}
div.stButton > button:active {
    transform: translateY(0);
}   

/* Alert boxes */
div[data-testid="stAlert"] {
    border-radius: 6px !important;
    font-size: 0.82rem !important;
    font-family: 'DM Mono', monospace !important;
}

/* Divider */
hr {
    border-color: #2e2e35 !important;
    margin: 2rem 0 !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<h1>Signup</h1>", unsafe_allow_html=True)
username = st.text_input("Username", placeholder="e.g. john_doe", max_chars=32)
password = st.text_input("Password", type="password", placeholder="Min. 8 characters")


if password:
    length_ok  = len(password) >= 8
    has_upper  = any(c.isupper() for c in password)
    has_digit  = any(c.isdigit() for c in password)
    has_symbol = any(c in "!@#$%^&*()_+-=[]{}|;':\",./<>?" for c in password)

st.markdown("")  

if st.button("Create account"):
    if not username.strip():
        st.error("Username cannot be empty.")
    elif len(username.strip()) < 3:
        st.error("Username must be at least 3 characters.")
    elif not password:
        st.error("Password cannot be empty.")
    elif len(password) < 8:
        st.error("Password must be at least 8 characters.")
    elif user_exists(username.strip()):
        st.warning(f"The username **{username.strip()}** is already taken. Please choose a different one.")
    else:
        success = register_user(username.strip(), password)
        if success:
            st.success(f"Account created for **{username.strip()}**! You can now log in.")
        else:
            st.warning(f"The username **{username.strip()}** is already taken. Please choose a different one.")
