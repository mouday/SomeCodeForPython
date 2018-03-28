# 通过iccid查询订单

import os
import re
import time


def get_files(path, ext=None):
    """通过扩展名，在指定文件夹下过滤出符合条件的文件
    param:
        - path{string} 文件夹路径
        - extension{string} 文件扩展名
    return:
        - filenames{list} 符合条件的文件名
    """
    filenames = []
    for root, dirs, files in os.walk(path):
        for file in files:
            filename = os.path.normpath("%s\%s"%(root, file))
            shortname, extension = os.path.splitext(filename)
            if ext != None:  # 指定扩展名
                if extension.lower() == ext:
                    filenames.append(filename)
            else:            # 不指定扩展名
                filenames.append(filename)
            
            # print(filename)
    return filenames

def get_files_by_generator(path, ext=None):
    """通过扩展名，在指定文件夹下过滤出符合条件的文件
    param:
        - path{string} 文件夹路径
        - extension{string} 文件扩展名
    return:
        - filenames{list} 符合条件的文件名
    """
    for root, dirs, files in os.walk(path):
        for file in files:
            filename = os.path.normpath("%s\%s"%(root, file))
            shortname, extension = os.path.splitext(filename)
            if ext != None:  # 指定扩展名
                if extension.lower() == ext:
                    yield filename
            else:            # 不指定扩展名
                yield filename
            
def find_iccid_from_file(iccid_filename):
    """在文件中查找iccid
    param：
        - iccid_filename{tuple} 需要查找的iccid,文件路径filename
    return：
        - filename{string} 包含iccid的文件名
    """
    iccid, filename = iccid_filename
    # print(filename)
    try:
        with open(filename, "r") as f:
            data = f.read()
            if iccid in data:
                print("查找结果：", filename)
                return True  # 查找到结果就返回         
    except:
        return False

def find_iccid_from_files(iccid, filenames):
    """在文件中查找iccid
    param：
        - filenames{list} 文件地址列表
        - iccid{string} 需要查找的iccid
    return：
        - filename{string} 包含iccid的文件名
    """
    # total = len(filenames)
    count = 0
    
    for filename in filenames:
        count += 1
        print("正在查找第 %s 个文件"%(count, ))
        try:
            with open(filename, "r") as f:
                data = f.read()
                if iccid in data:
                    return filename  # 查找到结果就返回
        except:
            continue


def main(path, iccid):
    # 获取符合条件的文件名
    filename = None
    try:
        filenames = get_files_by_generator(path)  # 不指定扩展名
        filename = find_iccid_from_files(iccid, filenames)
    except Exception as e:
        return "查找异常"
    return filename

if __name__ == '__main__':
    path = r"新建文件夹"   # 文件夹路径
    iccid = "8986011777741000079"  # iccid
    ret = main(path,  iccid)
    print(ret)

