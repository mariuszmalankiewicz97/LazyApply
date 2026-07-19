# from generators.html_injector import HTMLInjector
# from generators.pdf_generator import PDFGenerator
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
skill = Skill(1, "HTML5")
hobby = Hobby(1, "Nowe Technologie")
experience = Experience(
    1, "Asseco Poland", "Python Developer", "2020 - 2025", "lorem lorem lorem"
)
education = Education(1, "WSIiZ", "2025-currently", "Informatyka, Programowanie")

# repository methods
# user_repository.insert_user(new_user)
# skill_repository.insert_skill(skill)
# hobby_repository.insert_hobby(hobby)
# experience_repository.insert_experience(experience)
# education_repository.insert_education(education)

user_repository.select_user()
hobby_repository.select_hobby()
skill_repository.select_skill()
experience_repository.select_experience()
education_repository.select_education()

# injector = HTMLInjector()
# injector.inject_data("test.html")
# printer = PDFGenerator()
# printer.create_pdf("injectionfile.html", "example.pdf")
db_manager.close()
