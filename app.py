
import streamlit as st

paginas = [
    st.Page("src/ativ1.py", title="Atv 1"),
    st.Page("src/ativ2.py", title="Atv 2"),
    st.Page("src/ativ3.py", title="Atv 3"),
    st.Page("src/ativ4.py", title="Atv 4"),
    st.Page("src/ativ5.py", title="Atv 5"),
    st.Page("src/trabalho.py", title="Trabalho Final"),
]

st.navigation(paginas).run()
