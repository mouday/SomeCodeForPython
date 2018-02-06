
#SQLite测试.py

import sqlite3
from collections import namedtuple

# 连接数据库，创建游标
conn=sqlite3.connect("test.db")
cursor=conn.cursor()

# 创建数据库
rows = cursor.execute("""create table if not exists user (
                            id integer primary key autoincrement, 
                            name text not null)""")
print(rows)  # <sqlite3.Cursor object at 0x0000000000AE6570>

data = [
("Tom",),
("Jack",),
("Jimi",)
]

# 删除数据
# cursor.execute("delete from user where id > 3")

# 插入多个数据
rows = cursor.executemany("insert into user(name) values(?)", data)

conn.commit()  # 提交事务

# 查询数据
cursor.execute("select * from user")

result = cursor.fetchall() # 获取所有查询结果
print(result)
# [(1, 'Tom'), (2, 'Jack'), (3, 'Jimi')]

# 使用具名元组可以很好的使用数据库中拿到的数据
user = namedtuple("user", ["id", "name"])
for u in map(user._make, result):
    print(u)  
    print(u.id, u.name)
"""
user(id=1, name='Tom')
1 Tom
user(id=2, name='Jack')
2 Jack
user(id=3, name='Jimi')
3 Jimi
"""

# 关闭游标和连接
cursor.close()
conn.close()

