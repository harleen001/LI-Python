import streamlit as st
import streamlit.components.v1 as components

st.title("AJAX-style Integration")

# 1. Define the HTML "Frontend"
# This acts like the AJAX sender
ajax_html = """
<div style="background: #262730; padding: 20px; border-radius: 10px; border: 1px solid #444;">
    <label style="color: white; font-family: sans-serif;">Type something (AJAX style):</label><br><br>
    <input type="text" id="userInput" style="width: 100%; padding: 8px; border-radius: 5px; border: 1px solid #555;">
    <p style="color: #888; font-size: 0.8rem; margin-top: 10px;">Data is sent to Python on every keystroke.</p>
</div>

<script>
    const input = document.getElementById('userInput');
    
    input.addEventListener('input', (e) => {
        // This is our 'AJAX' call to the Streamlit Parent
        window.parent.postMessage({
            type: 'streamlit:setComponentValue',
            value: e.target.value
        }, '*');
    });
</script>
"""

# 2. Render the component and capture the return value
# In Streamlit, this variable 'captured_value' updates whenever postMessage is called
captured_value = components.html(ajax_html, height=150)

st.divider()

# 3. Python "Backend" Logic
if captured_value:
    st.subheader("Python received this in real-time:")
    st.code(captured_value)
    
    # Example of Python doing work on the 'AJAX' data
    word_count = len(captured_value.split())
    st.write(f"Word count calculated by Python: **{word_count}**")
else:
    st.info("Start typing in the HTML box above!")