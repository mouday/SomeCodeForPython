import hashlib

'''
函数名称：MD5加密
Paramenters:
    string - 需要加密的字符串
Return:
    String - md5加密后的字符串
'''
def md5(s):
    if isinstance(s,str):
        m = hashlib.md5()   
        m.update(s.encode("utf-8"))#py3需要先编码
        return m.hexdigest()
    else:
        return ''

def main():
    print(md5("1234567890"))
    # e807f1fcf82d132f9bb018ca6738a19f

if __name__ == '__main__':
    main()

