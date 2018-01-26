import zipfile

#压缩
z=zipfile.ZipFile("test.zip","w")
z.write("test.txt")  #压缩包写入
z.write("text.json")  #压缩包写入
z.close()

#解压
z1=zipfile.ZipFile("预个人化HHSR09-2016-017-72.zip","r")
z1.extractall("1")
z1.close()

