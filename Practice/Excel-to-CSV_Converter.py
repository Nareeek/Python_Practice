# Using the openpyxl module, write a program that reads
# all the Excel files in the current working directory and outputs them as CSV
# files. A single Excel file might contain multiple sheets; you’ll have to
# create one CSV file per sheet.

# The filenames of the CSV files should be <excel filename>_<sheet title>.csv,
# where <excel filename> is the filename of the Excel file without the file
# extension (for example, 'spam_data', not 'spam_data.xlsx') and <sheet
# title> is the string from the Worksheet object’s title variable.

import os, openpyxl as xl
import sys, csv

path_for_excel_files = r'D:/Python/Python_practice/Practice/automate_online-materials'
path_for_main_program = r'D:/Python/Python_practice/Practice'

os.chdir(path_for_main_program)
os.makedirs('Excel_to_csv', exist_ok=True)

for excelFile in os.listdir(path_for_excel_files):
    # Skip non-xlsx files, load the workbook object.
    if not excelFile.endswith('.xlsx'):
        continue
    
    # Loop through every sheet in the workbook.
    print(excelFile)
    file_path = os.path.join(path_for_excel_files, excelFile)
    
    wb = xl.load_workbook(file_path)
    for sheetName in wb.sheetnames:    
        sheet = wb[sheetName]

        # Create the CSV filename from the Excel filename and sheet title.
        csvFileName = excelFile + '_' + sheetName + '.csv'
        path = os.path.join('Excel_to_csv', csvFileName)

        # Create the csv.writer object for this CSV file.
        csvFileObj = open(path, 'w', newline='')
        csvWriter = csv.writer(csvFileObj)

        # Loop through every row in the sheet.
        for rowNum in range(1, min(100, sheet.max_row) + 1):
            #print(rowNum, end=' ')
            rowData = [] # append each cell to this list

            # Loop through each cell in the row.
            for colNum in range(0, min(100, sheet.max_column)):
                # Append each cell's data to rowData.
                rowData.append(sheet[rowNum][colNum].value)
                
            # Write the rowData list to the CSV file.
            csvWriter.writerow(rowData)
            
        csvFileObj.close()
