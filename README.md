# Coding Katas with TDD 🏋️‍♂️

This repository contains simple coding katas to practice problem-solving and Test-Driven Development (TDD) using Python.

## 📂 Project Structure

```markdown
📁 Coding_Katas/
│
├── 📁 katas/
│   ├── init.py
│   ├── string_manipulations.py
│   ├── other_kata_files.py
│   ├── etc
│
├── 📁 tests/
│   ├── init.py
│   ├── test_string_manipulations.py
│   ├── test_other_kata_files.py
│   ├── etc
│
├── .gitignore                
├── requirements.txt          
├── README.md                 👋 You are reading me right now! 👋
```

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Coding_Katas.git
cd Coding_Katas
```
### 2️⃣ Set Up a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Running the Tests 🧪
The repository follows TDD, meaning each kata has corresponding unit tests.

To run all tests:

```bash
pytest tests/
```

To run a specific test:
```bash
pytest tests/test_string_manipulations.py
```