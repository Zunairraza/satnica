import sys
import ezodf
import calendar
import datetime

docs = ["templates/timesheet_assistant.ods", "templates/timesheet_dentist.ods"]

if len(sys.argv) == 2:
    YEAR = int(sys.argv[1])
else:
    YEAR = datetime.date.today().year

MONTH_NAMES = [
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
]

def open_document(doc_name: str):
    return ezodf.opendoc(doc_name)

def set_output_name(doc_name: str):
    file_name = doc_name.split("/")[1]
    name = file_name.split(".")[0]
    return f"output/{name}_{YEAR}.ods"

def get_month_layout(year: int, month: int):
    days_in_month = calendar.monthrange(year, month)[1]
    if days_in_month == 31:
        last_column = "AG"
    else:
        last_column = "AF" if days_in_month == 30 else "AE"
    workdays = 0
    for day in range(1, days_in_month + 1):
        date = datetime.date(year, month, day)
        is_weekend = date.weekday() >= 5
        if not is_weekend:
            workdays += 1
    return (days_in_month, last_column, workdays * 8)

for doc_name in docs:
    document = open_document(doc_name)

    for month in range(1, 13):
        days_in_month, last_column, total_hours = get_month_layout(YEAR, month)
        hours_cell = f"{last_column}19"
        hours_value = f"={last_column}18-{total_hours}"
        sheet_name = MONTH_NAMES[month - 1]
        sheet = document.sheets[sheet_name]
        sheet["D5"].set_value(YEAR)
        sheet[hours_cell].formula = hours_value
        
    output_name = set_output_name(doc_name)
    document.saveas(output_name)