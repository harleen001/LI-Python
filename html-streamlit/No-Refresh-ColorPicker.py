import streamlit as st
import streamlit.components.v1 as components

st.subheader("Real-time Color Changer")

# 1. Get the value from the URL if it exists
chosen_color = st.query_params.get("color", "None")

# 2. The HTML Grid
# We use window.top.history.replaceState to change the URL silently
# Then window.parent.location.reload() to trigger Streamlit's rerun
html_code = """
<div style="display: flex; gap: 10px;">
    <div class="box" style="background: #FF4B4B; width: 50px; height: 50px; cursor: pointer; border-radius: 8px;" onclick="send('#FF4B4B')"></div>
    <div class="box" style="background: #1C83E1; width: 50px; height: 50px; cursor: pointer; border-radius: 8px;" onclick="send('#1C83E1')"></div>
    <div class="box" style="background: #00D411; width: 50px; height: 50px; cursor: pointer; border-radius: 8px;" onclick="send('#00D411')"></div>
</div>

<script>
    function send(color) {
        const url = new URL(window.top.location);
        url.searchParams.set('color', color);
        window.top.history.replaceState({}, '', url);
        window.top.location.reload(); // Tells Streamlit to check the URL
    }
</script>
"""

components.html(html_code, height=100)

# 3. Display the result
if chosen_color != "None":
    st.subheader(f"Python received: {chosen_color}")
    st.markdown(f"Your color is: <div style='width:30px; height:30px; background:{chosen_color}; display:inline-block;'></div>", unsafe_allow_html=True)