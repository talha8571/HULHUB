import openpyxl
path= "/DataDriven/writedata.xlsx"

workbook=openpyxl.load_workbook(path)

sheet=workbook.active

for r in range(1,14):
    for c in range(1,4):
        sheet.cell(row=r,column=c).value="bingo"


    workbook.save(path)
