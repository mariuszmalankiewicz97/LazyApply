from jinja2 import Environment, FileSystemLoader


class HTMLInjector:
    def __init__(self, directory_templates="templates"):
        self.directory_templates = directory_templates

        loader_templates = FileSystemLoader(self.directory_templates)

        self.environment = Environment(loader=loader_templates)

    def inject_data(
        self,
        fetch_template,
        user,
        education,
        hobbies,
        experiences,
        skills,
        injection_filename="injectionfile",
    ):
        template = self.environment.get_template(fetch_template)
        self.user = user
        self.education = education
        self.hobbies = hobbies
        self.experiences = experiences
        self.skills = skills

        html = template.render(
            name=self.user[0],
            lastname=self.user[1],
            city=self.user[2],
            phone=self.user[3],
            email=self.user[4],
            summary=self.user[5],
            github=self.user[6],
            linkedin=self.user[7],
            name_school=self.education[0],
            time_school=self.education[1],
            specialization=self.education[2],
            hobbies=self.hobbies,
            experiences=self.experiences,
            skills=self.skills,
        )

        with open(f"{injection_filename}.html", "w", encoding="utf-8") as f:
            f.write(html)
