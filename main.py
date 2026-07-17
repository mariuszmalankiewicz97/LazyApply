# from generators.html_injector import HTMLInjector
# from generators.pdf_generator import PDFGenerator
from data.database import DataManager

# injector = HTMLInjector()
# injector.inject_data("test.html")
# printer = PDFGenerator()
# printer.create_pdf("injectionfile.html", "example.pdf")
database = DataManager("data/database.db")
