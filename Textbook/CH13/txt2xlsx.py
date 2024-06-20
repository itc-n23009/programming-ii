import openpyxl

def read_files_to_spreadsheet(file_paths, output_file):
    wb = openpyxl.Workbook()
    ws = wb.active

    for col_index, file_path in enumerate(file_paths, start=1):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for row_index, line in enumerate(lines, start=1):
                ws.cell(row=row_index, column=col_index, value=line.strip())

    wb.save(output_file)

