# LazyApply

A project that automates the creation of tailored PDF resumes based on collected data.

## 🛠 Built With (Technologies)

*   **Python** - Main application engine and logic
*   **Jinja2** - Template system for injecting data into HTML files
*   **WeasyPrint** - Advanced library for converting HTML and CSS to PDF while preserving print dimensions and proportions (A4)
*   **HTML5 & CSS3** - Resume templates and structure styling
*   **Git & GitHub** - Version control and documentation
*   **VS Code** - Main development environment
*   **Sqlite** - Data container

## File Directory
```text
LazyApply/
├── database/
│   └── main.sqlite     #main candidate data
├── static/
│   ├── modern.css
│   ├── icons/
│   └── imgs/
├─── templates/
│   └── modern.html     #inject html from database jinja2
├─── generators/
│   ├── html_injector.py        #jinja2
│   └── pdf_generator.py        #weasyprint
├── main.py     #core logic
├── venv
├── .gitignore.py
└── README.md
```

## 🏗 System Architecture (Flowchart)
![Schemat architektury projektu](architecture.drawio.svg)

## 🚀 Getting Started

Follow these steps to set up the development environment and run the resume generator locally.

### 1. Clone the repository
```bash
git clone https://github.com/mariuszmalankiewicz97/LazyApply.git
cd LazyApply
```

### 2. Create and activate a virtual environment
It is strictly recommended to use a virtual environment to isolate project dependencies.
Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```
macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install dependencies
Once the virtual environment is active, install the required packages (including WeasyPrint and Jinja2):
```bash
pip install -r requirements.txt
```

### 4. Run the Generator
To generate your resume, simply run the main script:
```bash
python cv_generator.py
```

### 🔍 Code Standards
To maintain high code quality, readability, and adherence to backend development best practices (e.g., SOLID principles), this project utilizes the following tools:

* **Black** - The uncompromising Python code formatter.
* **Flake8** - For linting and real-time error checking.

If you are using **VS Code**, please ensure you have the official `Black Formatter` and `Flake8` extensions installed, and enable the `Format On Save` option in your editor settings before committing any new code.

