import streamlit as st
from utils import extract_text_from_pdf, calculate_ats_score, analyze_resume

st.set_page_config(page_title="Resume Analyzer")

st.title("Resume Analyzer")
st.write("Upload your resume and get basic ATS feedback")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file:

    resume_text = extract_text_from_pdf(uploaded_file)

    # ATS score
    score, matched = calculate_ats_score(resume_text)

    st.subheader("ATS Score")
    st.progress(score)
    st.write(f"Score: {score}%")

    st.subheader("Matched Skills")
    st.write(matched)

    # Suggestions
    suggestions = analyze_resume(resume_text)

    st.subheader("Suggestions")
    for s in suggestions:
        st.warning(s)
# How silly of me to think that I can write code without bugs got a name error wow
# had to describe every part noww
