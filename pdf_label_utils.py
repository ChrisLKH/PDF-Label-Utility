import os
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


def rotate_pdf(input_file: str, output_file: str, degrees: int = 180):
    """Rotate the first page of a PDF by the specified degrees."""
    reader = PdfReader(input_file)
    writer = PdfWriter()

    page = reader.pages[0]
    page.rotate(degrees)
    writer.add_page(page)

    with open(output_file, "wb") as f_out:
        writer.write(f_out)


def add_text_to_label(input_file: str, output_file: str, text: str, x: float, y: float):
    """Add text to a PDF label at a specified (x, y) position."""
    page_width, page_height = 4 * inch, 6 * inch

    # Create a canvas overlay
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(page_width, page_height))
    c.setFont("Helvetica", 10)
    c.drawString(x, y, text)
    c.save()

    # Merge overlay with the original PDF
    packet.seek(0)
    overlay_reader = PdfReader(packet)
    overlay_page = overlay_reader.pages[0]

    reader = PdfReader(input_file)
    original_page = reader.pages[0]
    original_page.merge_page(overlay_page)

    writer = PdfWriter()
    writer.add_page(original_page)

    with open(output_file, "wb") as f_out:
        writer.write(f_out)


def merge_labels(pdf_list: list[str], output_file: str):
    """Merge multiple PDF labels into one file."""
    merger = PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    with open(output_file, "wb") as f_out:
        merger.write(f_out)

    merger.close()
