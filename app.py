import streamlit as st
from utils import extract_text
from summarizer import abstractive_summary
from rouge import Rouge

st.set_page_config(page_title="AutoDoc AI", layout="wide")

st.title("📄 AutoDoc AI - Intelligent Document Summarizer")

uploaded_file = st.file_uploader("Upload a document (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

if uploaded_file:
    with st.spinner("🔍 Extracting text..."):
        raw_text = extract_text(uploaded_file)
        st.subheader("📜 Extracted Text")
        st.text_area("Text", raw_text, height=400, key="extracted_text")

    if st.button("✨ Generate Summary"):
        with st.spinner("🧠 Summarizing..."):
            try:
                summary = abstractive_summary(raw_text)
                st.subheader("📝 Summary")
                st.success(summary)

                # ROUGE scores
                rouge = Rouge()
                scores = rouge.get_scores(summary, raw_text, avg=True)
                st.subheader("📊 Summary Quality (ROUGE Scores)")
                st.write("ROUGE scores evaluate how well the summary captures the content of the original text.")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("ROUGE-1 (F1)", f"{scores['rouge-1']['f']:.3f}")
                with col2:
                    st.metric("ROUGE-2 (F1)", f"{scores['rouge-2']['f']:.3f}")
                with col3:
                    st.metric("ROUGE-L (F1)", f"{scores['rouge-l']['f']:.3f}")
            except Exception as e:
                st.error(f"Error generating summary: {str(e)}")