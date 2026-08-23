# 待办清单 - 新手教程

## 📝 功能介绍

这是一个很实用的小工具，帮你管理每天要做的事。支持：

- ➕ **添加待办**：输入要做的事情，存进列表
- 👀 **查看待办**：把所有待办按序号列出来
- ✅ **标记完成**：输入序号，完成的事就从列表里划掉
- 💾 **自动保存**：退出时把待办写进 `todo.txt` 文件，下次打开还能接着看

## 🚀 怎么运行

1. 确认电脑装了 Python 3
2. 打开终端，进入这个文件夹
3. 输入命令运行：
   ```bash
   python main.py
   ```
4. 按提示输入 1-4 的数字选择操作就行

## 📚 学到的知识点

### 1. 列表 list
```python
todo_list = []
todo_list.append("买牛奶")   # 往末尾添加
todo_list.pop(0)            # 删除指定位置的元素
len(todo_list)              # 看有多少个元素
```
- 列表是最常用的数据结构，可以看成一个大"收纳盒"
- `append` 加东西，`pop` 删东西，`len` 数数量

### 2. 自定义函数 def
```python
def add_todo():
    ...
```
- `def` 用来定义一个函数，函数是一段能重复用的代码
- 把功能拆成一个个函数，主流程就变得很清爽

### 3. 文件读写 open
```python
with open("todo.txt", "w", encoding="utf-8") as f:
    f.write("内容" + "\n")
```
- `"r"` 只读、`"w"` 写入、`"a"` 追加
- `with` 语法会自动关闭文件，不用担心忘关
- `encoding="utf-8"` 指定中文编码，不然容易乱码

### 4. os.path.exists 判断文件在不在
```python
import os
if os.path.exists("todo.txt"):
    ...
```
- 打开不存在的文件会报错，所以先判断一下更安全

### 5. enumerate 同时拿序号和内容
```python
for xuhao, item in enumerate(todo_list):
    print(f"{xuhao + 1}. {item}")
```
- `enumerate` 会返回「序号, 内容」两个值
- 序号默认从 0 开始，习惯上 +1 让它从 1 开始显示

### 6. try-except 捕获异常
```python
try:
    index = int(bianhao) - 1
except (ValueError, IndexError):
    print("序号不对")
```
- 用户可能乱输入字母，或者序号超出范围
- 用 try-except 兜底，程序就不会崩溃

### 7. while True + break
```python
while True:
    ...
    if choice == "4":
        break
```
- `while True` 是无限循环，让程序一直问你
- 满足条件就 `break` 跳出循环，结束程序

### 8. strip 清理字符串
```python
hang = hang.strip()
```
- 去掉字符串两边的空格和换行符
- 读文件时特别常用，因为每行末尾都带个 `\n`

### 9. f-string 格式化
```python
print(f"已添加：{shi_xiang}")
```
- `f` 开头的字符串，花括号 `{}` 里可以直接写变量
- 会自动把变量值替换进去

## 💡 新手小贴士

1. **分函数写**：每个函数只干一件事，好读也好改
2. **先跑通再加功能**：先把最简版本写对，再慢慢复杂
3. **多 print 调试**：不确定程序跑到哪了，就多打印看看
4. **别怕报错**：报错信息会告诉你第几行错了，仔细看就行

## 🎯 进阶挑战

- [ ] 给待办加"优先级"（高/中/低），查看时按优先级排序
- [ ] 加"已完成清单"，完成的待办不删掉而是挪过去
- [ ] 支持设置截止日期，快到期的自动提醒
- [ ] 把待办存成 CSV 或 JSON 格式，方便别的程序读取
- [ ] 加个命令行参数，直接 `python main.py add 买东西` 添加

## 🔗 相关资源

- [Python 官方教程](https://docs.python.org/zh-cn/3/tutorial/)
- [菜鸟教程 - Python3](https://www.runoob.com/python3/python3-tutorial.html)
- [Python 文件读写](https://docs.python.org/zh-cn/3/tutorial/inputoutput.html)