from weasyprint import HTML, CSS


class PDFGenerator:
    def __init__(self, css_path="static/style.css", output_dir="output"):
        self.css_path = css_path
        self.output_dir = output_dir

    def create_pdf(self, inject_html, output_filename):
        final_path = f"{self.output_dir}/{output_filename}"

        HTML(string=inject_html, base_url=self.output_dir).write_pdf(
            output_filename, stylesheets=[CSS(self.css_path)]
        )

        return final_path
