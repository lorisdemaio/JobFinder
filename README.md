# 📌 Introduction

This Python script allows you to search for remote job offers on Remotive.com.  
It sends a request to the Remotive API, filters the results based on selected criteria
(keyword and location), and either saves the job offers to a CSV file or prints them to the console.

---
<br>

# 🧰 Usage
Once you've downloaded the file or cloned the repository, unpack it and move it to a directory convenient for you. 
Open the terminal and navigate to the directory, when you are in the "JobFinder" directory you can navigate 
to the "data" directory to see the jobs.csv file or navigate to "src" directory and use the command

```bash
python main.py --keyword <your_keyword> --location <location> --limit <number> --csv
```
to search job offers.

### Arguments

* -k OR --keyword (**REQUIRED**): Filter job offers by keyword.
* -l OR --location (**OPTIONAL**): Filter job offers by location.
* -lt OR --limit: (**OPTIONAL**): Limit the number of job offers returned (default: 10).
* --csv (**OPTIONAL**): Export job offers to a CSV file.

---
<br>

# 📥 Installation

1. Clone the repository:
```bash
git clone https://github.com/lorisdemaio/JobFinder.git
```
2. (Optional but recommended) Create and activate a virtual environment:
```bash
python -m venv venv
```
Windows
```bash
venv\Scripts\activate
```
MacOS/Linux
```bash
source venv/bin/activate
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

---
<br>

# ⚙️ Requirements

To use this project you need:
* Python 3.11.9 or higher

If you dont't have python installed on your computer, you can install it 
from this link: https://www.python.org/downloads/

---
<br>

# 🙏 Credits

This project uses the public API provided by **Remotive** to retrieve remote job listings.

- Website: https://remotive.com
- API documentation: https://remotive.com/api-documentation

All job data belongs to Remotive and the respective companies.
This project is intended for educational and personal use.

<br><br>
