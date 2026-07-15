import json
import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS


def generate_cv():
    with open("data/main_cv.json", "r", encoding="utf-8") as file:
        cv_data = json.load(file)

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("cv_template.html")

    rendered_html = template.render(
        basic_data=cv_data["basic_data"],
        hobbies=cv_data["hobbies"],
        summary=cv_data["summary"],
        experiences=cv_data["experiences"],
        skills=cv_data["skills"],
    )

    base_url = os.path.dirname(os.path.abspath(__file__))

    HTML(string=rendered_html, base_url=base_url).write_pdf(
        "Mariusz_Malankiewicz_CV.pdf", stylesheets=[CSS("static/cv_style.css")]
    )


if __name__ == "__main__":
    generate_cv()
