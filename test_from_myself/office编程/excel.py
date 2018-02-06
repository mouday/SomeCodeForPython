
import xlrd, xlwt

def read_excel(path):
    workbook = xlrd.open_workbook(path)
    print(workbook.sheet_names())
    
    sheet = workbook.sheet_by_index(0)
    
    for row in range(sheet.nrows):
        print()
        for col in range(sheet.ncols):
            #print("%5s"%sheet.row(row)[col].value,"\t",end=" ")
            print("%5s"%sheet.cell(row,col).value,"\t",end=" ")

def main():
    path  =r"C:\Users\PSY\Desktop\中电数据.xlsx"
    read_excel(path)

if __name__ == "__main__":
    main()
