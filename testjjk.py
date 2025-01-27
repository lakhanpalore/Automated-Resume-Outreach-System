import pandas as pd

file_path = 'D:\python\Portals.xlsx'
excel_file = pd.ExcelFile(file_path)
print(excel_file.sheet_names)
