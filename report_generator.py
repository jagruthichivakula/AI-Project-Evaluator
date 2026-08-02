from fpdf import FPDF

def create_pdf(report):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    for line in report.split("\n"):
        pdf.multi_cell(0, 10, line)

    pdf.output("reports/Project_Report.pdf")