import os

# 打包文件
file = "main.py"

# icon图标
icon = "icons/Limewire.ico"

os.system("pyinstaller -F -w {} -i {}".format(file, icon))