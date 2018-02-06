try:
    1/0
except Exception as e:
    print(e)
else:
    print("程序没错误")
finally:
    print("执行完毕")

"""
division by zero
执行完毕
"""