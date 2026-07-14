# LazyApply

A project that automates the creation of tailored PDF resumes based on collected data.

## 🛠 Built With (Technologies)

*   **Python** - Core logic and PDF generation (WeasyPrint, Jinja2)
*   **HTML5 & CSS3** - Resume templates and structure styling
*   **Git & GitHub** - Version control and documentation
*   **VS Code** - Main development environment

## 🏗 System Architecture (Flowchart)

```mermaid
graph TD
    %% Version 1.0: Static CV Generator
    Data[data/<br>main_cv.py<br>]
    Generator[cv_generator.py<br>PDF Generator]
    HTML[templates/<br>cv_template.html]
    CSS[static/<br>cv_style.css]
    PDF[ready_CV.pdf]

    Data -->|Data Transfer| Generator
    HTML -.->|Structure| Generator
    CSS -.->|Appearance| Generator
    Generator -->|WeasyPrint| PDF
