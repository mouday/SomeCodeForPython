#email_helper.py
'''
参考：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432005226355aadb8d4b2f3f42f6b1d6f2c5bd8d5263000

封装成简单邮件发送模块
'''
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

debug = True  # debug开关

def debug_info(text):
    if debug == True:
        print(text)

class EmailClient(object):
    '邮件发送端初始化类'

    def __init__(self, smtp_server):
        '初始化服务器地址'
        self._smtp_server = smtp_server  
        self.addrs = []  # 邮件地址列表, 格式(addr, name)

    def login(self,  from_addr, password, from_name="admin"):
        '登录'
        self._from_addr = from_addr
        self._password = password
        self._from_name = from_name

        try:
            self.server = smtplib.SMTP(self._smtp_server, 25)
            #server.set_debuglevel(1)
            self.server.login(self._from_addr, self._password)
        except Exception as e:
            return -1  # 登录失败
            debug_info("登录失败")
        else:
            return 0  # 登录成功
            debug_info("登录成功")

    def send(self, title, text,  to_addr, to_name=None):
        '发送邮件'
        if to_name == None: to_name=to_addr

        try:
            # 接受方信息
            msg = MIMEText(text, 'plain', 'utf-8')
            msg['From'] = self._format_addr('%s<%s>' % (self._from_name,self._from_addr))
            msg['To'] = self._format_addr('%s <%s>' % (to_name,to_addr))
            msg['Subject'] = Header(title, 'utf-8').encode()

             # 发送内容
            self.server.sendmail(self._from_addr, to_addr, msg.as_string())
            
            return 0

        except Exception as e:
            debug_info(e)
            return -1

    def add_address(self, addr, name=None):
        '增加地址到地址列表'
        if name==None: name = addr
        self.addrs.append((addr, name))

    def send_all(self, title, text):
        '发送所有人'
        success = 0
        fail = 0
        for addr, name in self.addrs:
            ret = self.send(title, text, addr, name)
            if ret == 0: 
                success += 1
            else:
                fail += 1
        return success, fail

    def __del__(self):
        '析构'
        self.server.quit()

    def _format_addr(self, s):
        '格式化地址'
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

if __name__ == '__main__':
    email_client=EmailClient("smtp.163.com")  # 邮箱服务器地址
    email_client.login("username", "password", "name")  # 登陆

    email_client.add_address("email") # 增加收件人
    email_client.add_address("email")
    email_client.add_address("email")

    # 发送 
    success, fail = email_client.send_all("邮件标题", "邮件内容，试试看能不能发送出去")
    print("success:", success, "fail:", fail)  # 返回发送结果
