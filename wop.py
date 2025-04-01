import tkinter as tk
from tkinter import messagebox
import os
import writedata

ve = "Beta V0.1"
def main():

    # 窗口设置
    root = tk.Tk()
    root.geometry("800x500-200-100")
    root.title(f"Wop {ve}")

    # 添加页面Frame
    page = tk.Frame(root)

    # 添加HomeFrame
    home_frame = tk.Frame()

    #添加chFrame
    ch_frame = tk.Frame(root)

    # 添加projectFrame
    project_frame = tk.Frame(root)

    # 默认显示
    home_frame.pack()

    # 创建homeFrame组件
    writedata.creative_wop()
    title_home = tk.Label(home_frame, text=f"Welcome ! {os.getlogin()}", font=10, padx=20, pady=20)
    title_home.pack()

    go_home = tk.Button(home_frame, text="Let go!", font=10, padx=10, pady=10)
    go_home.pack(padx=20, pady=20)

    # 设置go_home按钮的点击效果
    def show_menu():
        home_frame.pack_forget()
        ch_frame.pack()

    go_home.config(command=show_menu)

    # 创建chFrame组件
    home_button = tk.Button(ch_frame, text="Home", font=10, padx=10, pady=10)
    home_button.pack(padx=20, pady=20)

    project_button = tk.Button(ch_frame, text="Project", font=10, padx=10, pady=10)
    project_button.pack(padx=20, pady=20)

    new_project_button = tk.Button(ch_frame, text="New project", font=10, padx=10, pady=10)
    new_project_button.pack(padx=20, pady=20)

    # 创建projectFrame组件

    project_title = tk.Label(project_frame, text="Your project: ")

    project_list = writedata.read_project_list()



    def show_home():
        ch_frame.pack_forget()
        home_frame.pack()

    home_button.config(command=show_home)

    # 添加Menu
    main_menu = tk.Menu(page, tearoff=False)
    home_menu = tk.Menu(main_menu, tearoff=False)

    # 添加Home二级菜单
    home_menu.add_command(label="Home")
    home_menu.add_command(label="Project")
    home_menu.add_command(label="New Project")

    # 添加Home栏
    main_menu.add_cascade(label="Home", menu=home_menu)

    # 显示Menu
    root.config(menu=main_menu)

    # 程序主循环
    root.mainloop()

if __name__ == '__main__':
    main()