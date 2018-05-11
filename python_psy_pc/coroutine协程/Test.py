#协程测试
"""文档说明"""
def gen(data):
    print("before yield",data)
    backData=yield data
    print("after resume",backData)

def main():
    print("hello world")

if __name__ == '__main__':
    main()
