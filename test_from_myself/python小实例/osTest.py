import os

p=os.path.abspath(__file__)
print(p)
# D:\CODE\python\python小实例\osTest.py

p=os.path.dirname(os.path.abspath(__file__))
print(p)
# D:\CODE\python\python小实例

p=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(p)
# D:\CODE\python