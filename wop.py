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

    # 添加Menu
    main_menu = tk.Menu(page)

    # 添加HomeFrame
    home_frame = tk.Frame()
    # 默认显示
    home_frame.pack()

    # 标题
    writedata.creative_wop()
    title_home = tk.Label(home_frame, text=f"Welcome ! {os.getlogin()}", font=10)
    title_home.pack()

    # 添加Home栏
    main_menu.add_command(label="Home")

    # 显示Menu
    root.config(menu=main_menu)

    # 程序主循环
    root.mainloop()

if __name__ == '__main__':
    main()