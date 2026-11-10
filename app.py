import streamlit as st
from utils.pdf_reader import extract_pdf_text
from utils.doc_reader import extract_docx_text
from utils.text_cleaner import clean_text
from utils.resume_parser import parse_resume
from utils.skill_matcher import match_skills
from utils.ats_score import calculate_ats_score
# Page Configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Header
st.title("📄 AI Resume Analyzer")
st.write("Boost your resume with AI-powered ATS analysis.")

# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Home", "Resume Analyzer", "Reports", "About"]
)

st.divider()

# Two Columns
left, right = st.columns(2)

# LEFT COLUMN
with left:

    st.subheader("📄 Upload Resume")

    resume = st.file_uploader(
        "Choose your Resume",
        type=["pdf", "docx"],
        key="resume_upload"
    )

    if resume is not None:

        st.success("Resume uploaded successfully!")

        st.write("### File Details")

        st.write("**File Name:**", resume.name)
        st.write("**File Type:**", resume.type)
        st.write("**File Size:**", round(resume.size / 1024, 2), "KB")

        with open(f"uploads/{resume.name}", "wb") as f:
            f.write(resume.getbuffer())

        st.info("Resume saved in the uploads folder.")

# RIGHT COLUMN
with right:

    st.subheader("Job Description")

    job_description = st.text_area(
        "Paste Job Description",
        height=250
    )

    analyze = st.button(
        "Analyze Resume",
        use_container_width=True
    )

    if analyze:
        st.success("Analysis will start in the next phase.")
        result = match_skills(
    resume_skills,
    job_skills
)
        score = calculate_ats_score(
    result["matched_skills"],
    job_skills
)
st.divider()
st.caption("AI Resume Analyzer © 2026")