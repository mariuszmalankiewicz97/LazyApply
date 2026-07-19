from data.database import DataManager
from data.repositories.user_repository import UserRepository
from data.repositories.skill_repository import SkillRepository
from data.repositories.hobby_repository import HobbyRepository
from data.repositories.experience_repository import ExperienceRepository
from data.repositories.education_repository import EducationRepository
from models.user_model import User
from models.skill_model import Skill
from models.hobby_model import Hobby
from models.experience_model import Experience
from models.education_model import Education
from generators.html_injector import HTMLInjector
from generators.pdf_generator import PDFGenerator

db_manager = DataManager("data/database.db")
db_manager.connect()

# init repository
user_repository = UserRepository(db_manager)
skill_repository = SkillRepository(db_manager)
hobby_repository = HobbyRepository(db_manager)
experience_repository = ExperienceRepository(db_manager)
education_repository = EducationRepository(db_manager)

# models
new_user = User(
    "Mariusz",
    "Kowalski",
    "Rzeszów",
    "123 456 789",
    "test@test.com",
    "lorem lorem lorem lorem",
    "github test",
    "linkedin test",
)
new_skill = Skill(1, "HTML5")
new_skill2 = Skill(1, "CSS3")
new_hobby = Hobby(1, "Nowe Technologie")
new_hobby2 = Hobby(1, "Automatyzacja")
new_experience = Experience(
    1, "Asseco Poland", "Python Developer", "2020 - 2025", "lorem lorem lorem"
)
new_education = Education(1, "WSIiZ", "2025-currently", "Informatyka, Programowanie")

# repository methods
# user_repository.insert_user(new_user)
# skill_repository.insert_skill(new_skill)
# skill_repository.insert_skill(new_skill2)
# hobby_repository.insert_hobby(new_hobby)
# hobby_repository.insert_hobby(new_hobby2)
# experience_repository.insert_experience(new_experience)
# education_repository.insert_education(new_education)

user = user_repository.select_user()
education = education_repository.select_education()
hobbies = hobby_repository.select_hobby()
skills = skill_repository.select_skill()
experiences = experience_repository.select_experience()
db_manager.close()


injector = HTMLInjector()
injector.inject_data("modern.html", user, education, hobbies, experiences, skills)

printer = PDFGenerator()
printer.create_pdf("injectionfile.html")
