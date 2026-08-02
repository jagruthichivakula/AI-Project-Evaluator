# 📄 AI Project Proposal Evaluator

## 📌 Overview

The **AI Project Proposal Evaluator** is a Streamlit-based web application that helps evaluate Final Year Project proposals using Artificial Intelligence. Users can upload a proposal in PDF format, and the system extracts the text, analyzes it using an AI model, and generates a detailed evaluation report that can be downloaded as a PDF.

---

## 🚀 Features

- 📤 Upload Final Year Project Proposal PDF
- 📖 Extract text from PDF using PyMuPDF
- 🤖 AI-based proposal evaluation
- ⭐ Innovation and technical feasibility analysis
- 📊 Detailed evaluation report
- 📥 Download evaluation report as PDF
- 💻 Interactive Streamlit interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Ollama / OpenAI *(depending on your configuration)*
- PyMuPDF
- FPDF2
- python-dotenv

---

## 📂 Project Structure

```text
AI-Project-Evaluator/
│── app.py
│── evaluator.py
│── pdf_reader.py
│── report_generator.py
│── models.py
│── requirements.txt
│── README.md
│── .gitignore
│── uploads/
└── reports/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/jagruthichivakula/AI-Project-Evaluator.git
```

Move to the project folder

```bash
cd AI-Project-Evaluator
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. Upload a project proposal PDF.
2. Extract text from the PDF.
3. Send the extracted text to the AI model for evaluation.
4. Generate a detailed evaluation report.
5. Download the report as a PDF.

---

## 🎯 Future Enhancements

- Multi-language support
- Proposal comparison
- User authentication
- Evaluation history
- Cloud deployment

---

## 👩‍💻 Author

**Jagruthi Chivakula**

Aspiring Data Analyst | Python Developer | AI Enthusiast
