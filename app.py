
import streamlit as st

paginas = [
    st.Page("src/ativ1.py", title="Atv 1"),
    st.Page("src/ativ2.py", title="Atv 2"),
    st.Page("src/ativ3.py", title="Atv 3"),
]

st.navigation(paginas).run()
