import openpyxl
import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: python multiplicationTable.py <N>')
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print('Please provide a valid integer for N.')
        sys.exit(1)
    
    wb = openpyxl.Workbook()
    ws = wb.active

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            ws.cell(row=i, column=j, value=i * j)
    
    filename = f'multiplicationtable{N}x{N}.xlsx'
    wb.save(filename)
    
    print(f'Multiplication table {N}x{N}')

if __name__ == '__main__':
    main()

