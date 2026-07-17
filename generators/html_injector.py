from jinja2 import Environment, FileSystemLoader


class HTMLInjector:
    def __init__(self, directory_templates="templates"):
        self.directory_templates = directory_templates

        loader_templates = FileSystemLoader(self.directory_templates)

        self.environment = Environment(loader=loader_templates)

    def inject_data(self, fetch_template, injection_filename="injectionfile"):
        template = self.environment.get_template(fetch_template)

        html = template.render(name="MARIUSZ")

        with open(f"{injection_filename}.html", "w", encoding="utf-8") as f:
            f.write(html)
