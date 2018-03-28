"""
将中电设备生成的日志转为银证设备日志格式
"""

import time
import os
import shutil
import random

def get_field_dict(titles, fields):
    obj_zip =  zip(titles,fields)
    dct = dict([item for item in obj_zip])
    return dct

def change_date_format(datestr):
    """改变日期格式：月/日/年 -> 月-日
    例如：01/10/2018  ->  01-06
    """
    date = time.strptime(datestr, "%m/%d/%Y")  # 转时间
    new_date = time.strftime("%m-%d",date)  # 格式化
    return new_date

def change_filename(path):
    (name, ext) = os.path.splitext(path)
    new_name= name + "_new" + ext
    return  new_name

def change_card_state(card_state):
    """改变“写卡成功”显示"""
    if card_state =="PASSED":
        return "写卡成功"
    else:
        return ""

def change_printdate(printdata, feedback):
    if feedback == "NULL":
        return printdata
    else:
        return printdata + " " + feedback

def convert_log_format(path, itemname, single_time):
    """日志转换
    path{str}:日志路径
    itemname{str}:批次号
    single_time{int}:单张时间
    """
    save_path = change_filename(path)
    new_f = open(save_path, "w")  # 打开新文件

    titles = []  # 标题字段
    reader_id = 0  # 写头id
    line_count = 0  # 行号
    with open(path, "r") as f:
        for line in f:
            line_count += 1  
            if line_count == 1:
                titles = line.replace("\n", "").split()
            else:
                if " "in line:  # 去除“----------”
                    fields = line.replace("\n", "").split()
                    dct = get_field_dict(titles, fields)
                    # print(dct)
                    date = change_date_format(dct["Date"])
                    card_state = change_card_state(dct["CardState"])
                    printdata = change_printdate(dct["PrintData"], dct["Feedback1"])
                    
                    if reader_id >= 20:
                        reader_id = 0

                    reader_id += 1
                    write_time = random.randint(single_time-2, single_time+2)

                    #输出格式： [01-06 10:55:25] [HHSR09_2016_031_165][4420,6090,009 HNB,][2][18 秒] 写卡成功
                    new_line = "[" + date +" "+ dct["Time"] + "] [" +itemname +\
                                "][" +  printdata +"]" +\
                                "["+ str(reader_id) +"]["+ str(write_time) +" 秒]" + card_state +"\n"
                    
                    new_f.write(new_line)# 写入
    new_f.close()  # 关闭新文件
    shutil.copystat(path, save_path)
    return save_path
        

def main(item_name, single_time=18, dirname = "写卡日志"):
    """
    :param item_name{str} 批次号
    :param single_time{int} # 平均写卡时间
    :param dirname{str} # 日志目录

    """
    # 配置相关信息
    try:
        save_dir = os.path.join(os.path.dirname(dirname), "转完的日志")  # 保存新日志目录
        print(save_dir)
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)

        files = os.listdir(dirname)
        count = 0  # 计数

        for file in files:
            count += 1
            path = convert_log_format(os.path.join(dirname, file), item_name, single_time)
            shutil.copy2(path, os.path.join(save_dir, os.path.basename(path)))
            os.remove(path)
    except Exception as e:
        return False
    return True

if __name__ == '__main__':
    main()
