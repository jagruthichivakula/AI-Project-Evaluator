import streamlit as st
import os

from pdf_reader import extract_text_from_pdf
from evaluator import evaluate_project
from report_generator import create_pdf

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="AI Project Proposal Evaluator",
    page_icon="📄",
    layout="wide"
)

# ---------------- Sidebar ----------------
st.sidebar.title("Project Information")

st.sidebar.info("""
AI Project Proposal Evaluator

Technology Used:
- Python
- Streamlit
- Gemini AI
- PyMuPDF
- FPDF
""")

# ---------------- Main Page ----------------
st.title("📄 AI Project Proposal Evaluator")

st.write("Upload your Final Year Project Proposal PDF")

uploaded_file = st.file_uploader(
    "Choose a PDF",
    type=["pdf"]
)

# ---------------- PDF Upload ----------------
if uploaded_file is not None:

    os.makedirs("uploads", exist_ok=True)
    os.makedirs("reports", exist_ok=True)

    file_path = os.path.join("uploads", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ PDF Uploaded Successfully!")

    # Extract text
    text = extract_text_from_pdf(file_path)

    st.subheader("📑 Extracted Proposal")

    st.text_area(
        "Proposal Text",
        text,
        height=300
    )

    # Evaluate Button
    if st.button("🚀 Evaluate Proposal"):

        with st.spinner("AI is evaluating your proposal..."):

            result = evaluate_project(text)

        st.subheader("📊 AI Evaluation Report")

        st.markdown(result)

        # Generate PDF
        create_pdf(result)

        # Download Button
        with open("reports/Project_Report.pdf", "rb") as pdf_file:

            st.download_button(
                label="📥 Download Evaluation Report",
                data=pdf_file,
                file_name="Project_Report.pdf",
                mime="application/pdf"
            )