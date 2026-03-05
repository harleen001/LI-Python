import time
import numpy as np
import pandas as pd
import streamlit as st

_LOREM_IPSUM = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""

def stream_data():
    # Stream the first block of text
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

    # Yield the DataFrame (st.write_stream will render this as a table)
    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=list("abcdefghij"),
    )

    # Stream the second block of text
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

st.title("Streamlit Data Streamer")

if st.button("Run Stream"):
    # This captures the generator and displays it dynamically
    st.write_stream(stream_data())