
import traceback

try:
    1/0
except:
    traceback.print_exc(file=open("tb.txt","w+"))  # except的缩写
else:
    print("success!")
finally:
    print("ok")

# print(dir(traceback))
# print(help(traceback))

"""tb.txt
Traceback (most recent call last):
  File "D:\GitHub\SomeCodeForPython\test_from_myself\Python17个常用内置模块总结\16.traceback模块.py", line 4, in <module>
    1/0
ZeroDivisionError: division by zero
"""