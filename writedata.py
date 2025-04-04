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
            file_path = os.path.join(logs_path, ti + ".wopd")
            file = open(file_path, "a")
            file.write(logs + "\n")
            file.close()
        else:
            os.makedirs(logs_path)
            file_path = os.path.join(logs_path, ti + ".wopd")
            file = open(file_path, "a")
            file.write(logs + "\n")
            file.close()
    else:
        os.makedirs(folder)
        folder_list = os.listdir(folder)
        if ".logs" in folder_list:
            file_path = os.path.join(logs_path, ti + ".wopd")
            file = open(file_path, "a")
            file.write(logs)
            file.close()
        else:
            os.makedirs(logs_path)
            file_path = os.path.join(logs_path, ti + ".wopd")
            file = open(file_path, "a")
            file.write(logs)
            file.close()
    return

def creative_wop():
    user_list = os.listdir(user)
    if ".wop" not in user_list:
        os.makedirs(folder)
        file_path = os.path.join(folder, "project.wopd")
        file = open(file_path, "a")
        file.close()
    log(logs="creative wop folder" + "\n")
    return

def write_project_list(data: str, path: str):
    user_list = os.listdir(user)
    if ".wop" in user_list:
        file_path = os.path.join(folder, "project.wopd")
        file = open(file_path, "a")
        file.write(data + "\n")
        file.close()
    else:
        os.makedirs(folder)
        file_path = os.path.join(folder, "project.wopd")
        file = open(file_path, "a")
        file.write(data + "\n")
        file.close()
    log(logs="write project list")
    user_list = os.listdir(user)
    if ".wop" in user_list:
        file_path = os.path.join(folder, "project_path.wopd")
        file = open(file_path, "a")
        file.write(path + "\n")
        file.close()
    else:
        os.makedirs(folder)
        file_path = os.path.join(folder, "project_path.wopd")
        file = open(file_path, "a")
        file.write(path + "\n")
        file.close()
    log(logs="write project path")
    return

def read_project_list():
    user_list = os.listdir(user)
    data = []
    if ".wop" in user_list:
        file_path = os.path.join(folder, "project.wopd")
        if os.path.exists(file_path):  # 新增文件存在检查
            with open(file_path, "r") as file:  # 使用with自动关闭文件
                raw_data = file.readlines()
                data = [line.strip() for line in raw_data]  # 关键修改：清理换行符
    else:
        os.makedirs(folder)
    log(logs="read project list")
    return data  # 现在返回的是清理后的列表

def read_project_path():
    user_list = os.listdir(user)
    data = []
    if ".wop" in user_list:
        file_path = os.path.join(folder, "project_path.wopd")
        if os.path.exists(file_path):  # 新增文件存在检查
            with open(file_path, "r") as file:
                raw_data = file.readlines()
                data = [line.strip() for line in raw_data]  # 关键修改：清理换行符
    else:
        os.makedirs(folder)
    log(logs="read project path")
    return data  # 现在返回的是清理后的列表

if __name__ == '__main__':
    print(write_project_list(data="beta", path = "E:\beta"))