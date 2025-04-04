import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os
import writedata
from tkinter import filedialog

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

    # 添加newprojectFrame
    new_project_frame = tk.Frame(root)

    # 默认显示
    home_frame.pack()

    # 创建homeFrame组件
    writedata.creative_wop()
    title_home = ttk.Label(home_frame, text=f"Welcome ! {os.getlogin()}", font=10)
    title_home.pack()

    go_home = ttk.Button(home_frame, text="Let go!")
    go_home.pack(padx=20, pady=20)

    # 设置go_home按钮的点击效果
    def show_menu():
        home_frame.pack_forget()
        ch_frame.pack()

    go_home.config(command=show_menu)

    # 创建chFrame组件
    home_button = ttk.Button(ch_frame, text="Back")
    home_button.pack(padx=20, pady=20)

    project_button = ttk.Button(ch_frame, text="Project")
    project_button.pack(padx=20, pady=20)

    new_project_button = ttk.Button(ch_frame, text="New project")
    new_project_button.pack(padx=20, pady=20)

    # 创建projectFrame组件

    project_title = ttk.Label(project_frame, text="Your project: ", font=10)
    project_title.pack(padx=10, pady=10)

    project_list = writedata.read_project_list()

    project_listbox = tk.Listbox(project_frame, width=80, height=15)

    project_back = ttk.Button(project_frame, text="Back")
    project_back.pack(padx=10, pady=10)

    project_listbox.delete(0, tk.END)

    if len(project_list) == 0:
        project_listbox.insert(tk.END, "Not have project")
    else:
        for project_name in project_list:
            project_listbox.insert(tk.END, project_name)

    project_listbox.pack(padx=10, pady=10)

    re_listbox = ttk.Button(project_frame, text="Update")
    re_listbox.pack(padx=10, pady=10)

    def update_listbox():
        project_list = writedata.read_project_list()
        project_frame.pack_forget()
        project_frame.pack()
        project_listbox.delete(0, tk.END)
        if len(project_list) == 0:
            project_listbox.insert(tk.END, "Not have project")
        else:
            for project_name in project_list:
                project_listbox.insert(tk.END, project_name)

    re_listbox.config(command=update_listbox)

    # 添加newprojectFrame组件

    new_project_title = ttk.Label(new_project_frame, text="Creative new project", font=10)
    new_project_title.pack(padx=10, pady=10)

    choice_project_folder = ttk.Label(new_project_frame, text="Choice root directory : ", font=5)
    choice_project_folder.pack(padx=10, pady=10)

    new_project_path = ttk.Entry(new_project_frame, width=50)
    new_project_path.pack(padx=10, pady=10)

    # 新增文件夹选择函数
    def choose_directory():
        selected_path = filedialog.askdirectory(
            title="Choice project path",
            initialdir=os.path.expanduser("~")
        )
        if selected_path:  # 仅当用户选择有效路径时更新
            new_project_path.delete(0, tk.END)
            new_project_path.insert(0, selected_path)

    choice_button = ttk.Button(
        new_project_frame,
        text="Choice",
        command=choose_directory  # 绑定事件
    )
    choice_button.pack(padx=10, pady=10)

    new_project_name = ttk.Label(new_project_frame, text="New project name : ", font=5)
    new_project_name.pack(padx=10, pady=10)

    new_project_name_entry = ttk.Entry(new_project_frame, width=30)
    new_project_name_entry.pack(padx=10, pady=10)

    creative_new_project = ttk.Button(new_project_frame, text="Creative")
    creative_new_project.pack(padx=10, pady=10)

    back_new_project = ttk.Button(new_project_frame, text="Back")
    back_new_project.pack(padx=10, pady=10)

    def creative_project():
        # 获取并清理输入
        cre_project_name = new_project_name_entry.get().strip()
        cre_project_path = new_project_path.get().strip()

        # 路径标准化（关键修改）
        cre_project_path = os.path.normpath(cre_project_path).replace("\\", "/")

        # 动态获取最新数据（关键修改）
        user_all_name = writedata.read_project_list()  # 实时读取项目名
        user_all_path = writedata.read_project_path()  # 实时读取路径

        # === 英文提示修改开始 ===
        # 项目名长度校验
        if len(cre_project_name) > 20:
            messagebox.showerror("Error", "Project name cannot exceed 20 characters")
            return

        # 检查项目名重复（不区分大小写）
        existing_names = [name.strip().lower() for name in user_all_name]
        if cre_project_name.lower() in existing_names:
            messagebox.showerror("Error", "Project name already exists")
            return

        # 检查路径重复（标准化后对比）
        existing_paths = [
            os.path.normpath(path.strip()).replace("\\", "/").lower()
            for path in user_all_path
        ]
        if cre_project_path.lower() in existing_paths:
            messagebox.showerror("Error", "Project path already exists")
            return

        # 空输入校验
        if not cre_project_name:
            messagebox.showerror("Error", "Please enter project name")
            return
        if not cre_project_path:
            messagebox.showerror("Error", "Please select project path")
            return
        # === 英文提示修改结束 ===

        # 写入数据
        writedata.write_project_list(data=cre_project_name, path=cre_project_path)
        messagebox.showinfo("Success", f"Project {cre_project_name} created!\nPath: {cre_project_path}")

        # 清空输入框并返回主页
        new_project_name_entry.delete(0, tk.END)
        new_project_path.delete(0, tk.END)
        show_home()

    # 为"创建"按钮设置点击效果
    creative_new_project.config(command=creative_project)

    def show_new_project():
        ch_frame.pack_forget()
        project_frame.pack_forget()
        home_frame.pack_forget()
        new_project_frame.pack()

    def show_home():
        ch_frame.pack_forget()
        project_frame.pack_forget()
        new_project_frame.pack_forget()
        home_frame.pack()

    def show_project_list():
        home_frame.pack_forget()
        new_project_frame.pack_forget()
        ch_frame.pack_forget()
        project_frame.pack()

    project_back.config(command=show_home)

    back_new_project.config(command=show_home)

    home_button.config(command=show_home)

    project_button.config(command=show_project_list)

    new_project_button.config(command=show_new_project)

    # 添加Menu
    main_menu = tk.Menu(page, tearoff=False)
    home_menu = tk.Menu(main_menu, tearoff=False)

    # 添加Home二级菜单
    home_menu.add_command(label="Home", command=show_home)
    home_menu.add_command(label="Project", command=show_project_list)
    home_menu.add_command(label="New Project", command=show_new_project)

    # 添加Home栏
    main_menu.add_cascade(label="Home", menu=home_menu)

    # 显示Menu
    root.config(menu=main_menu)

    # 程序主循环
    root.mainloop()

if __name__ == '__main__':
    main()