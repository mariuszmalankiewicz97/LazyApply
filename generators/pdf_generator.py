from pathlib import Path
from weasyprint import HTML, CSS


class PDFGenerator:
    def __init__(self, css_path="static/modern.css", output_dir=""):
        self.css_path = Path(css_path)
        self.output_dir = Path(output_dir)

    def create_pdf(self, html_filepath, output_filename="example.pdf"):
        final_path = self.output_dir / output_filename

        HTML(filename=html_filepath).write_pdf(
            final_path, stylesheets=[CSS(self.css_path)]
        )

        return final_path
