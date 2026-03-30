import streamlit as st
import streamlit.components.v1 as components

st.subheader("Real-Time AJAX Integration")

# 1. Get the current text from the URL
user_input = st.query_params.get("text", "")

# 2. HTML Frontend with 'input' event
ajax_html = f"""
<div style="background: #262730; padding: 20px; border-radius: 10px; border: 1px solid #444;">
    <input type="text" id="userInput" value="{user_input}" 
           style="width: 100%; padding: 10px; border-radius: 5px; font-size: 1.1rem;" 
           placeholder="Type something...">
</div>

<script>
    const input = document.getElementById('userInput');
    
    // Auto-focus and keep cursor at the end
    input.focus();
    input.setSelectionRange(input.value.length, input.value.length);

    input.addEventListener('input', (e) => {{
        const val = e.target.value;
        const url = new URL(window.top.location);
        url.searchParams.set('text', val);
        
        // Update URL silently
        window.top.history.replaceState({{}}, '', url);
        
        // Tell Streamlit to rerun. 
        // We use a small delay or window.parent.postMessage if available
        // For this simple version, location.reload is the bridge.
        window.top.location.reload(); 
    }});
</script>
"""

components.html(ajax_html, height=120)

st.divider()

# 3. Python Results
if user_input:
    st.write("### Python is processing...")
    
    # Show uppercase version in real-time
    st.info(f"**Uppercase:** {user_input.upper()}")
    
    # Word count
    words = user_input.split()
    st.metric("Live Word Count", len(words))
    
    # Character count
    st.metric("Live Character Count", len(user_input))
else:
    st.warning("Start typing to see Python work in real-time!")