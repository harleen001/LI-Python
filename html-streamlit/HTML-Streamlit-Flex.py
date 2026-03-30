import streamlit as st

# 1. Page Config (For better width)
st.set_page_config(layout="centered")

# 2. Complete CSS Overrides to replicate the original design
# We must use !important to overwrite Streamlit's built-in styles.
st.markdown("""
<style>
    /* 1. Global Page Styles (Matches original dark mode) */
    .stApp { background-color: #0e1117; color: white; }
    .stHorizontalBlock { gap: 15px !important; justify-content: center; }
    h1 { text-align: center; color: white !important; font-size: 2.2rem; }
    h2 { font-size: 1.8rem; }
    p { color: #fafafa; }
    
    /* 2. Style THE BUTTONS to look exactly like CARDS */
    div.stButton > button {
        width: 100%;
        height: auto !important; /* Let content set height */
        min-height: 20px;
        background-color: #262730;
        color: white;
        border: 1px solid #444;
        border-radius: 12px;
        padding: 18px 15px !important;
        font-family: 'Segoe UI', sans-serif;
        text-align: center;
        text-decoration: none;
        transition: all 0.3s ease;
        display: flex;
        flex-direction: column; /* Stack Emoji/Text and Subtext */
        align-items: center;
        justify-content: center;
        line-height: 1.2 !important;
    }

    /* 3. Style THE TEXT inside the button (We use JS below to create this) */
    /* Large Title (e.g., "Home") */
    .btn-title { 
        font-size: 1.1rem !important; 
        font-weight: 600 !important; 
        margin-bottom: 5px;
        display: block;
    }
    /* Smaller Subtext (e.g., "Return to start") */
    .btn-sub { 
        font-size: 0.8rem !important; 
        color: #888 !important; 
        font-weight: 400 !important;
        display: block;
    }

    /* 4. Overwrite ALL default Streamlit hover/active/focus effects */
    div.stButton > button:hover {
        border-color: #ff4b4b !important;
        background-color: #31333f !important;
        color: white !important;
        transform: translateY(-3px);
    }

    /* Target the focus state and active state directly */
    div.stButton > button:focus:not(:active), 
    div.stButton > button:active {
        border-color: #ff4b4b !important;
        background-color: #31333f !important;
        color: white !important;
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Handle Navigation Logic using Session State (Unbreakable)
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# Helper for the visual active state (red border)
def get_btn_type(target):
    return "primary" if st.session_state.current_page == target else "secondary"

# 4. Display the Title and Navigation
st.subheader("HTML Flexbox Navigation")

col1, col2, col3 = st.columns(3)

# We use simple button labels; the CSS/JS handles the rest
with col1:
    if st.button("Home|Return to start", key="home_btn", type=get_btn_type("home")):
        st.session_state.current_page = "home"

with col2:
    if st.button("Data|View Metrics", key="data_btn", type=get_btn_type("dash")):
        st.session_state.current_page = "dash"

with col3:
    if st.button("Setup|App Config", key="set_btn", type=get_btn_type("settings")):
        st.session_state.current_page = "settings"

st.divider()

# 5. The Dynamic Page Content (This changes below the buttons)
if st.session_state.current_page == "home":
    st.header("Welcome!")

    st.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800")

elif st.session_state.current_page == "dash":
    st.header("Data Dashboard")
    st.write("Live Stats")
    colA, colB = st.columns(2)
    colA.metric("Active Users", "1,452", "+5%")
    colB.metric("Revenue", "$12,400", "+15%")
    st.line_chart([10, 25, 20, 40, 35, 50])

elif st.session_state.current_page == "settings":
    st.header("⚙️ App Settings")
    st.toggle("Dark Mode (System)")
    st.slider("Refresh Rate", 1, 60, 5)

# 6. JAVASCRIPT: The only way to split the text "Data|Metrics" into two lines
# We target the button text and replace the "|" with dynamic HTML spans.
st.markdown("""
<script>
    const buttons = window.parent.document.querySelectorAll('div.stButton > button');
    buttons.forEach(button => {
        if (button.innerText.includes('|')) {
            const parts = button.innerText.split('|');
            button.innerHTML = `<span class="btn-title">${parts[0]}</span><span class="btn-sub">${parts[1]}</span>`;
        }
    });
</script>
""", unsafe_allow_html=True)