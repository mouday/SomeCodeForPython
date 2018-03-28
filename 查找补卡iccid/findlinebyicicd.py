# 通过iccid查询数据行

import os
import re
import time


def getFiles(path, ext=None):
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

def getLinesFromFileByIccids(iccidfile, filename):
    """在文件中查找iccid,返回行
    param：
        - filenames{list} 文件地址列表
        - iccid{string} 需要查找的iccid
    return：
        - filename{string} 包含iccid的文件名
    """
    # total = len(filenames)
    

    # 读取iccid
    iccids = open(iccidfile, "r").readlines()
    iccids = [iccid.replace("\n", "") for iccid in iccids]
    print("iccids", iccids) 
    title_key = iccids[0]
    body_keys = iccids[1:]
    print("title_key", title_key)
    print("body_keys", body_keys)


    # 读取文件查找
    lines = open(filename, "r").readlines()
    lines = [line.replace("\n", "") for line in lines]
    # print("lines", lines) 
    title_lines = lines[0]
    body_lines = lines[1:]
    print("title_lines", title_lines)
    # print("body_lines", body_lines)

    index = title_lines.split(",").index(title_key)
    print(index)
    dct = {}
    for body_line in body_lines:
        dct[body_line.split(",")[index]] = body_line

    # print(dct)
    ok_lines=[]
    for body_key in body_keys:
        ok_line = dct.get(body_key)
        ok_lines.append(ok_line)
    print(len(ok_lines), ok_lines)
    data = "\n".join(ok_lines)
    print(data)
    fret =  open("findresult.mca" ,"w")
    fret.write(title_lines)
    fret.write("\n")
    fret.write("\n".join(ok_lines))
    fret.write("\n")
    fret.close()
    return len(ok_lines)

import os

def combineTxt(path:str)->bool:
    """合并txt文本
    """
    count = 0
    files = os.listdir(path)
    ret_path = "combine.txt"
    with open(ret_path, "w") as fwrite:
        for file in files:
            f = os.path.join(path, file)
            with open(f, "r") as fopen:
                data = fopen.read()
                fwrite.write(data)
            count += 1
    print("合并数量:", count)
    return ret_path

def checkFiles(filenames):
    # 先打开第一个文件，获取标题
    pass

def main(path, iccidfile):
    # 获取符合条件的文件名
    filename = None
    # try:
    combine = combineTxt(path) # 不指定扩展名

    ret = getLinesFromFileByIccids(iccidfile, combine)
    print(ret)
    # except Exception as e:
    #     return "查找异常"
    return ret

if __name__ == '__main__':
    path = r"新建文件夹"   # 文件夹路径
    iccidfile = "iccids.txt"  # iccid
    ret = main(path,  iccidfile)
    print(ret)

