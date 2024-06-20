import openpyxl

def spreadsheet_to_files(spreadsheet_file, output_files):
    wb = openpyxl.load_workbook(spreadsheet_file)
    ws = wb.active

    for col_index, output_file in enumerate(output_files, start=1):
        with open(output_file, 'w', encoding='utf-8') as file:
            for row in ws.iter_rows(min_col=col_index, max_col=col_index, values_only=True):
                if row[0] is not None:
                    file.write(f"{row[0]}\n")
