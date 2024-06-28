import ezsheets

ID = '1xHE1fXKhzZogK1WwDdg_gboeDi10z9kIAyMq_81n7dQ'

ss = ezsheets.Spreadsheet(ID)
sheet = ss[0]
for row in range(sheet.rowCount):
    data = sheet.getRow(row + 1)
    print(data)
