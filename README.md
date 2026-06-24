# Python Automation Scripts

A collection of practical Python automation scripts built to solve real business problems.

---

## 📁 File Organiser

Automatically sorts a messy folder into subfolders by file type.

### What it does
- Scans any folder you point it at
- Sorts files into categories: Images, Documents, Videos, Audio, Archives, Scripts
- Moves unrecognised files into an "Other" folder
- Prints a log of every file moved

### How to use
1. Open `file_organiser.py`
2. Change the `FOLDER_TO_ORGANISE` path to your target folder
3. Run the script

### Requirements
- Python 3.x
- No external libraries needed

---
## 📊 Excel Report Generator

Converts raw CSV data into a clean, formatted Excel report automatically.

### What it does
- Reads any CSV file
- Generates a styled Excel report with colour coded headers
- Auto fits column widths
- Adds alternating row colours for readability
- Calculates totals automatically at the bottom

### How to use
1. Place your CSV file in the same folder
2. Open `excel_report_generator.py`
3. Change `INPUT_CSV` to your file name
4. Run the script

### Requirements
- Python 3.x
- openpyxl (`pip install openpyxl`)

## 🚀 More scripts coming soon
- Web Scraper

---

Built by [Patrik Milić](https://py-patrik.pages.dev)
