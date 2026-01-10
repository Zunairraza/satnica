# Dental Clinic Timesheet Generator

This project is a small automation tool that generates yearly timesheet spreadsheets for a dental clinic based on a given year.

It takes pre-defined ODS spreadsheet templates (for a dentist and a dental assistant), calculates the monthly working hours for each month of the selected year, and produces new ready-to-use timesheets.

The goal is to eliminate manual recalculation of monthly hour funds every year and prevent errors in payroll and work-time tracking.

---

## What it does

For a given year (for example 2026), the tool:

- Calculates the number of working days (Monday–Friday) for each month
- Computes the monthly hour fund (working days × 8 hours)
- Updates all 12 monthly sheets in each template
- Writes the selected year into the sheets
- Generates new ODS files ready for use

---

## Folder structure
```
satnica/
│
├── satnica.py
├── requirements.txt
├── templates/
│ ├── timesheet_dentist.ods
│ └── timesheet_assistant.ods
├── output/
```

Generated files will be written to an `output` folder.

## Installation

Create a virtual environment and install dependencies:
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Run the generator by providing a year:
```
python satnica.py 2026
```

If no year is provided, the current year will be used automatically.

The generated files will be created in the `output` folder:
```
output/
timesheet_dentist_2026.ods
timesheet_assistant_2026.ods
```

## Why this exists

This tool was created to automate a real-world administrative workflow in a dental clinic, where timesheet templates need to be recreated every year with correct monthly hour funds.

It is a simple example of how Python can be used to automate repetitive office work and reduce human error.
