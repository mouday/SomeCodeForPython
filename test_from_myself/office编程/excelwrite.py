#新建excel并写入
#而xlwt生成excel文件
#是不能在已有的excel文件基础上进行修改的
#保存格式只能是xls
import xlwt
workbook=xlwt.Workbook()
sheet1=workbook.add_sheet('sheet1',cell_overwrite_ok=True)
sheet2=workbook.add_sheet('sheet2',cell_overwrite_ok=True)

sheet1.write(0,0,'this should overwrite')
sheet1.write(0,1,'aaaaaaaaaaaaaaaaaaaaaaa')
sheet2.write(0,0,'this should overwrite')
sheet2.write(1,2,'bbbbbbbbbbbbbbbbb')
#--------------设置样式------------------
style=xlwt.XFStyle()
font=xlwt.Font()
font.name="微软雅黑"
font.size=14
style.font=font
#使用样式
sheet1.write(1,1,'use style',style)
workbook.save('test2.xls')#同名会覆盖
print('创建excel完成')