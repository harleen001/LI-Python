import streamlit as st
import streamlit.components.v1 as components

# Sample data to display in flex items
items = ["Dashboard", "Analytics", "Reports", "Settings", "Profile", "Notifications"]

# Define the HTML with Flexbox CSS
flex_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        .flex-container {{
            display: flex;
            flex-wrap: wrap; /* Allows items to wrap to next line */
            gap: 15px;      /* Space between items */
            justify-content: center; /* Centers items horizontally */
            font-family: 'Segoe UI', sans-serif;
        }}

        .flex-item {{
            background-color: #262730; /* Streamlit-like dark grey */
            color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            flex: 1 1 150px; /* Grow, Shrink, Basis (min-width) */
            text-align: center;
            border: 1px solid #444;
            transition: transform 0.2s;
        }}

        .flex-item:hover {{
            transform: translateY(-5px);
            border-color: #ff4b4b; /* Streamlit Red */
        }}
    </style>
</head>
<body>
    <div class="flex-container">
        {"".join([f'<div class="flex-item">{item}</div>' for item in items])}
    </div>
</body>
</html>
"""

st.title("Streamlit Flexbox Layout")
# Render the flexbox container. Set height to ensure it's not cut off.
components.html(flex_html, height=300)