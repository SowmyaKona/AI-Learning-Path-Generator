from fpdf import FPDF
from io import BytesIO


class PDF(FPDF):

    def header(self):

        self.set_font(
            "Arial",
            "B",
            16
        )

        self.cell(
            200,
            10,
            "AI Learning Mentor Roadmap",
            ln=True,
            align="C"
        )


def generate_pdf(response):

    pdf = PDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        size=12
    )

    # Learning Stages

    pdf.cell(
        200,
        10,
        "Learning Stages",
        ln=True
    )

    for item in response.learning_stages:

        pdf.multi_cell(
            0,
            10,
            f"- {item}"
        )

    pdf.ln(5)

    # Key Topics

    pdf.cell(
        200,
        10,
        "Key Topics",
        ln=True
    )

    for item in response.key_topics:

        pdf.multi_cell(
            0,
            10,
            f"- {item}"
        )

    pdf.ln(5)

    # Summary

    pdf.cell(
        200,
        10,
        "Summary",
        ln=True
    )

    pdf.multi_cell(
        0,
        10,
        response.learning_goal_summary
    )

    pdf_output = pdf.output(dest="S").encode("latin-1")

    return pdf_output