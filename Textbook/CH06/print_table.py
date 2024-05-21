def print_table(table_data):
    col_widths = [max(len(row[i]) for row in table_data) for i in range(len(table_data[0]))]
    
    for row in table_data:
        print('　'.join(cell.rjust(width) for cell, width in zip(row, col_widths)))

table_data = [['apples', 'Alice', 'dogs'],
              ['oranges', 'Bob', 'cats'],
              ['cherries', 'Carol', 'moose'],
              ['banana', 'David', 'goose']]

print_table(table_data)
