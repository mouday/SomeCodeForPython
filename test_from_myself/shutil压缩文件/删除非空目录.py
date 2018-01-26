
# 删除非空目录

import shutil
import os

dirname = r"C:\Users\PSY\Desktop\1"

print("start..")
try:
    # shutil.rmtree(dirname)  # 可能会报错
    
    os.system("rd /s/q %s"% dirname)   #调用系统命令
    
except Exception as e:
    print("Except:", e)

else:
    print("ok")

finally:
    input("press any key continue...")