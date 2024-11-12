import openpyxl
import pandas as pd

# Create a new Excel workbook
workbook = openpyxl.Workbook()

# Select the default sheet
sheet = workbook.active

# Add data to the Excel sheet
data = [
    ['Country', 'Capital', 'Other City'],
    ['United Kingdom', 'London', 'Liverpool'],
    ['Canada', 'Ottawa', 'Montreal'],
    ['United States', 'Washington DC', 'California'],
    ['Australia', 'Canberra', 'Sydney'],
]

for row in data:
    sheet.append(row)

# Save the workbook as a file
workbook.save('For_Loop_File.xlsx')

# Print a success message
print('Your Excel file has been successfully created')
