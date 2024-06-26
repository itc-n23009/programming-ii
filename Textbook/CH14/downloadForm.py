import ezsheets

SPREADSHEET_ID = '1Vq-h-kKZAMKLVpRdNsbc8t0GrH3yy4it2kxKjbrkrsg'

ss = ezsheets.Spreadsheet(SPREADSHEET_ID)

sheet = ss[0]

data = sheet.getRows()

for row in data[1:]:
    print(f"名前: {row[0]}, メールアドレス: {row[1]}")

