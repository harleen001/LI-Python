import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="centered")
st.title("RPG Health Bar Sync")

# 1. Get the current text from the URL (Our State)
user_text = st.query_params.get("msg", "")
char_count = len(user_text)

# Calculate "Health" (Max 100 characters for full health)
health_percent = min(char_count, 100) 
bar_color = "#00FF00" if health_percent > 50 else "#FFFF00" if health_percent > 20 else "#FF0000"

# 2. THE HEALTH BAR (Python → HTML)
# We use an f-string to "inject" the Python variable 'health_percent' into the CSS
health_bar_html = f"""
<div style="font-family: 'Courier New', monospace; color: white; margin-bottom: 10px;">
    PLAYER_1 STATUS: {health_percent}/100 XP
</div>
<div style="width: 100%; background: #333; border: 3px solid #fff; height: 30px; border-radius: 5px; overflow: hidden;">
    <div style="width: {health_percent}%; 
                background: {bar_color}; 
                height: 100%; 
                transition: width 0.5s ease-in-out;
                box-shadow: 0 0 10px {bar_color};">
    </div>
</div>
"""
components.html(health_bar_html, height=100)

st.divider()

# 3. THE AJAX INPUT (HTML → Python)
# 3. THE AJAX INPUT (Fixed with Debounce)
input_html = f"""
<div style="background: #111; padding: 20px; border: 1px solid #444; border-radius: 8px;">
    <p style="color: #888; font-family: sans-serif; margin-bottom: 10px;">Type to heal</p>
    <input type="text" id="questInput" value="{user_text}" 
           style="width: 100%; background: #222; color: #00FF00; border: 1px solid #00FF00; padding: 10px; font-family: monospace;">
</div>

<script>
    const input = document.getElementById('questInput');
    let timeout = null;

    // Keep cursor at the end
    input.focus();
    input.setSelectionRange(input.value.length, input.value.length);

    input.addEventListener('input', (e) => {{
        const val = e.target.value;
        
        // 1. Update the URL silently immediately (no reload)
        const url = new URL(window.top.location);
        url.searchParams.set('msg', val);
        window.top.history.replaceState({{}}, '', url);

        // 2. Debounce Logic: Clear the previous timer
        clearTimeout(timeout);

        // 3. Set a new timer to reload only after 300ms of silence
        timeout = setTimeout(() => {{
            window.top.location.reload();
        }}, 300); 
    }});
</script>
"""
components.html(input_html, height=150)

# 4. Python Feedback
if char_count >= 100:
    st.balloons()
    st.success("MAX LEVEL REACHED!")
elif char_count == 0:
    st.warning("Character is fainted! Type something to revive.")