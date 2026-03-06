import streamlit as st
import ollama

st.set_page_config(page_title="Yoga Guide AI", page_icon="🧘")

st.title("Custom Badminton Assistant")
st.caption("Direct, non-generic yoga coaching powered by Ollama")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask a yoga question..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response from your custom Ollama model
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ollama.chat(
                model='badminton-model', # Use your exact custom model name
                messages=[{'role': 'user', 'content': prompt}]
            )
            answer = response['message']['content']
            st.markdown(answer)
    
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": answer})