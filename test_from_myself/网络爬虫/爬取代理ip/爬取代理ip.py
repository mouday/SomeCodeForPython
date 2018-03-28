
"""
搭建一个爬虫代理池
参考：
《小白动手搭建一个简单爬虫代理池》
http://mp.weixin.qq.com/s/_lzWZPVc-OvPEx-wQH4qOg
《学会最简单的数据库|看完这7招就够了》
http://mp.weixin.qq.com/s?__biz=MzIxNjM4NDE2MA==&mid=2247484554&idx=1&sn=d57beb3552d89413cb834a1940db698a&chksm=97889345a0ff1a532ce06d354a42324429ff611ea1b103e2de3b87eb3e13334baa37ac2342b0&scene=21#wechat_redirect
"""
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import sqlite3
import time

def get_html_text(url):
    """获取网页，返回文本格式"""
    try:
        headers = {
            "User-Agent":"""Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 
            (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"""
            }
        r = requests.get(url, headers=headers)
        r.raise_for_status()  # 状态不是200，抛出异常
        r.encoding = r.apparent_encoding  # 编码
        return r.text
    except:
        return "产生异常"

def get_proxies():
    """获取代理ip，以[{},{}]形式返回"""
    url = "http://www.xicidaili.com/"
    html = get_html_text(url)
    soup = BeautifulSoup(html, "html.parser")
    ip_list = soup.find(id="ip_list")
    proxies = []
    for tr in ip_list.find_all("tr"):
        try:
            proxy = {}
            # ["代理IP地址", "端口", "服务器地址", "是否匿名", "类型", "存活时间", "验证时间"]
            tds = tr.find_all("td")
            ip = tds[1].string
            port = tds[2].string
            addr = tds[3].string
            anonymous = tds[4].string
            typ = tds[5].string
            alive = tds[6].string
            check = tds[7].string

            proxy["ip"] = ip
            proxy["prot"] = port
            proxy["addr"] = addr
            proxy["anonymous"] = anonymous
            proxy["type"] = typ
            proxy["alive"] = alive
            proxy["check"] = check

            proxies.append(proxy)

        except:
            continue
    return proxies
        

def save_list_to_xlsx(lst):
    # 表头
    titles = ["代理IP地址", "端口", "服务器地址", "是否匿名", "类型", "存活时间", "验证时间"]

    # 新建工作薄
    book = xlsxwriter.Workbook("ip_list.xlsx")
    sheet = book.add_worksheet("sheet1")
    row = 0  # 行号
    col = 0  # 列号

    # 表头写入excel
    for title in titles:
        sheet.write(row, col, title)
        col += 1
    row += 1

    # 写入每条记录
    for dct in lst:
        print(dct)
        sheet.write(row, 0, dct.get("ip"))
        sheet.write(row, 1, dct.get("prot"))
        sheet.write(row, 2, dct.get("addr"))
        sheet.write(row, 3, dct.get("anonymous"))
        sheet.write(row, 4, dct.get("type"))
        sheet.write(row, 5, dct.get("alive"))
        sheet.write(row, 6, dct.get("check"))
        row += 1

    book.close()
    return row


class Database(object):
    """连接数据库"""
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect(self.name)
        self.cursor = self.conn.cursor()

    def create_table(self, tablename):
        """创建工作表"""
        self.tablename = tablename
        sql = """create table if not exists %s(
            "id" integer primary key autoincrement,
            "ip" text,
            "port" integer,
            "addr" text,
            "anonymous" text,
            "type" text,
            "alive" text,
            "check" text,
            "status" integer default 1
            )"""%self.tablename
        self.cursor.execute(sql)

    def insert(self, data):
        """插入数据"""
        self.cursor.execute("""insert into ip_list("ip", "port", "addr", "anonymous", 
            "type", "alive", "check")values(?,?,?,?,?,?,?)""", data)
        self.conn.commit()

    def get_random_ip(self):
        """随机获取一个ip"""
        sql = "select ip, port from %s where state!=0 order by random() limit 1"%(self.tablename)
        self.cursor.execute(sql)
        for ip, port in self.cursor.fetchall():
            # print("ip:", ip, "port:", port)
            if self.verify_ip(ip, port): # 验证ip
                return (ip, port)
            else:
                return get_random_ip()

    def verify_ip(self, ip, port):
        """验证ip有效性"""
        http_url = "http://www.baidu.com"
        proxy_url = "https://{}:{}".format(ip, port)
        proxies = {
            "https": proxy_url
        }
        try:
            r = requests.get(http_url, proxies=proxies)
        except:
            self.delete_ip(ip)
            return False
        else:
            # code [200,300)之间则为有效的
            if r.status_code >=200 or r.status_code<300:
                return True
            else:
                self.delete_ip(ip)
                return False


    def delete_ip(self, ip):
        """删除ip记录"""
        # sql = "delete from %s where ip = %s"% (self.tablename, ip)
        sql = "update %s set status=0 where ip =%s"%(self.tablename, ip)
        self.cursor.execute(sql)
        self.conn.commit()

    def __del__(self):
        """释放数据库连接"""
        self.cursor.close()
        self.conn.close()

def add_list_to_database(lst):
    """插入到数据库"""
    database = Database("ip_pool.db")
    count = 0  # 计数
    database.create_table("ip_list")
    for dct in lst:
        data = (dct.get("ip"), dct.get("prot"), dct.get("addr"), dct.get("anonymous"), 
            dct.get("type"), dct.get("alive"), dct.get("check"))
        database.insert(data)
        count += 1

    return count


if __name__ == '__main__':
    # proxies = get_proxies()
    # ret = add_list_to_database(proxies)
    # print(ret)

    database = Database("ip_pool.db")
    database.create_table("ip_list")
    for i in range(100):
        ip, port = database.get_random_ip()
        print(ip, port)
    

