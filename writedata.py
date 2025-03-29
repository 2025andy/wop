import os
from datetime import datetime


# 本文件进行文件读取和写入

# 获取
user = os.path.expanduser("~")
folder = os.path.join(user, ".wop")
logs_path = os.path.join(folder, ".logs")
ti = str(datetime.now())[0:10]

# 日志
def log(logs: str):
    user_list = os.listdir(user)
    if ".wop" in user_list:
        folder_list = os.listdir(folder)
        if ".logs" in folder_list:
            file_path = os.path.join(logs_path, ti + ".xwd")
            file = open(file_path, "a")
            file.write(logs)
            file.close()
        else:
            os.makedirs(logs_path)
            file_path = os.path.join(logs_path, ti + ".xwd")
            file = open(file_path, "a")
            file.write(logs)
            file.close()
    else:
        os.makedirs(folder)
        folder_list = os.listdir(folder)
        if ".logs" in folder_list:
            file_path = os.path.join(logs_path, ti + ".xwd")
            file = open(file_path, "a")
            file.write(logs)
            file.close()
        else:
            os.makedirs(logs_path)
            file_path = os.path.join(logs_path, ti + ".xwd")
            file = open(file_path, "a")
            file.write(logs)
            file.close()
    return

def creative_wop():
    user_list = os.listdir(user)
    if ".wop" not in user_list:
        os.makedirs(folder)
    log(logs="creative wop folder")
    return