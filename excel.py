import xlrd

def excel():
    file_location ="C:/Users/Atul/Downloads/TestData.xlsx"
    workbook = xlrd.open_workbook(file_location)
    sheet = workbook.sheet_by_name("data")
    print(sheet.cell_value(0,0))
    print(sheet.nrows)
    for col in range(sheet.ncols):
        for row in range(sheet.nrows):
            print(sheet.cell_value(row,col))
        

if __name__ == '__main__':
    excel()