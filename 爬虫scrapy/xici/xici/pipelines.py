# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class XiciPipeline(object):
    def process_item(self, item, spider):
        # 连接数据库，创建游标
        DBKWARGS =  "xici.db"
        conn=sqlite3.connect(DBKWARGS)
        cursor=conn.cursor()

        # 创建数据库
        rows = cursor.execute("""create table if not exists xicidata (
                                    id integer primary key autoincrement, 
                                    ip text not null,
                                    port text not null,
                                    address text not null,
                                    typ text not null,
                                    speed text not null,
                                    check_time text not null
                                    )""")

        sql = ("insert into xicidata(ip, port, address, typ, speed, check_time)"
           "values(?,?,?,?,?,?)")
        lst = (item["ip"], item["port"], item["address"], 
            item["typ"],item["speed"],item["check_time"])

        try:
            cursor.execute(sql, lst)
        except Exception as e:
            print("insert error", e)
            conn.rollback()
        else:
            conn.commit()

        cursor.close()
        conn.close()
        return item