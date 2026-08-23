# -*- coding: utf-8 -*-
# 我是 Python 新手，这是我自己敲的"待办清单"小程序
# 代码写得很啰嗦，注释超多，就是方便自己以后回来看得懂

# 导入 os 模块，用来操作文件（比如判断文件存不存在）
import os

# 定义一个空列表，用来装所有的待办事项
# 列表 list 就像一个大"收纳盒"，可以往里不停地放东西
todo_list = []

# 保存待办事项的文件名，待办会存到这个文件里
file_name = "todo.txt"


def load_todos():
    """程序一启动，就把之前保存的待办读出来，这样重启也不丢"""
    # os.path.exists(文件名) 用来判断这个文件到底存不存在
    # 文件不存在就跳过下面的读取代码，不然打开不存在的文件会报错
    if os.path.exists(file_name):
        # with open 是打开文件的标准写法，用完会自动关闭文件
        # "r" 表示 read 只读模式，encoding 指定中文编码，防止乱码
        with open(file_name, "r", encoding="utf-8") as wenjian:
            # for 循环会一行一行地读文件
            for hang in wenjian:
                # strip() 去掉每行两边的空格和换行符
                hang = hang.strip()
                # 如果这一行不是空的，就加到列表里
                if hang != "":
                    todo_list.append(hang)
        print("📂 已加载之前保存的待办")


def save_todos():
    """把列表里的待办全部写回文件，实现"保存"功能"""
    # "w" 表示 write 写入模式，会直接覆盖文件原来的内容
    with open(file_name, "w", encoding="utf-8") as wenjian:
        # 遍历列表，把每一条待办写进文件
        for item in todo_list:
            # 每写一条，末尾加个换行符 \n，这样文件里一行就是一条
            wenjian.write(item + "\n")


def show_menu():
    """打印菜单，让用户知道现在能干什么"""
    print("")
    print("=" * 30)
    print("        📝 我的待办清单")
    print("=" * 30)
    print("  1. 添加待办")
    print("  2. 查看所有待办")
    print("  3. 标记完成（删掉一项）")
    print("  4. 退出程序")
    print("=" * 30)


def add_todo():
    """往列表里加一条待办"""
    # input() 会暂停程序等你输入，返回的内容是字符串
    shi_xiang = input("请输入要添加的待办：")
    # 判断一下，防止添加空内容
    if shi_xiang.strip() == "":
        print("内容不能为空哦！")
        return  # return 直接结束这个函数，回到主循环
    # append() 把新内容加到列表末尾
    todo_list.append(shi_xiang)
    print(f"✅ 已添加：{shi_xiang}")


def list_todos():
    """把所有待办一项一项打印出来"""
    # len(列表) 返回列表里有多少个元素
    if len(todo_list) == 0:
        print("📭 暂时没有待办，先去添加一条吧！")
        return
    print("")
    print("----- 我的待办 -----")
    # enumerate 可以在循环时同时拿到"序号"和"内容"
    # 序号默认从 0 开始，我们 +1 让它从 1 开始显示，更符合习惯
    for xuhao, item in enumerate(todo_list):
        print(f"{xuhao + 1}. {item}")
    print("--------------------")
    print(f"共 {len(todo_list)} 条待办")


def complete_todo():
    """标记完成：从列表里删掉一条"""
    # 先让用户看看现在有哪些待办，才知道删哪条
    list_todos()
    if len(todo_list) == 0:
        return
    # 让用户输入要完成第几条
    bianhao = input("输入要完成的序号（直接回车返回）：")
    if bianhao.strip() == "":
        return
    # 用户输入的是字符串，要转成整数才能当列表下标用
    # 用 try 来抓异常，万一用户乱输入字母，程序也不会崩溃
    try:
        index = int(bianhao) - 1  # 显示序号从1开始，列表下标从0开始，所以减1
        wancheng = todo_list.pop(index)  # pop(下标) 弹出并删除那一个元素
        print(f"🎉 完成！「{wancheng}」已被划掉")
    except (ValueError, IndexError):
        # ValueError 是输入了字母，IndexError 是序号超出范围
        print("序号不对，请输入一个正确的数字")


# ===== 程序真正开始执行的地方 =====

# 启动时先加载之前保存的待办
load_todos()

# 主循环：让程序一直运行，直到用户选择退出
while True:
    show_menu()
    choice = input("请输入 1-4 选择操作：")

    # 根据用户输入，调用对应的函数
    if choice == "1":
        add_todo()
    elif choice == "2":
        list_todos()
    elif choice == "3":
        complete_todo()
    elif choice == "4":
        # 退出前一定要保存，不然刚才添加的全丢了
        save_todos()
        print("已保存，下次打开还能看到。再见！👋")
        break  # break 跳出 while 循环，结束整个程序
    else:
        print("输入不对，请输入 1-4 的数字")