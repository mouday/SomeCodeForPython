import xlrd
path="test.xlsx"
excel=xlrd.open_workbook(path)
table=excel.sheets()[0]
#按照行取
for i in range(table.nrows):
	print(table.row_values(i))

#按照列取
for j in range(table.ncols):
	print(table.col_values(j))

#遍历所有单元格
for i in range(table.nrows):
	for j in range(table.ncols):
		print(table.cell_value(i,j))