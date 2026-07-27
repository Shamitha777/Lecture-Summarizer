import streamlit as st
from summarizer import summarize_text

st.title("📄 Lecture Notes Summarizer")

text = st.text_area("Paste your lecture text:")

if st.button("Summarize"):
    if text:
        result = summarize_text(text)
        st.subheader("Summary")
        st.write(result)
    else:
        st.warning("Please enter text")