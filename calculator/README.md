# 简易计算器 - 新手教程

## 🧮 程序介绍

一个简单的命令行计算器，支持加减乘除四种运算。这是学习函数和用户交互的好练习！

## 📚 学到的知识点

### 1. 基本数学运算
```python
a + b  # 加法
a - b  # 减法
a * b  # 乘法
a / b  # 除法（结果是浮点数）
```

### 2. try-except 异常处理
```python
try:
    num = float(user_input)
except ValueError:
    print("这不是数字")
```
- `try` 尝试执行代码
- `except` 如果出错了怎么办
- `ValueError` 是值错误的异常类型

### 3. 浮点数 float
```python
float("3.14")  # 把字符串转成小数
```
- `int` 是整数，`float` 是小数
- 除法的结果默认是 float

### 4. 字符串方法
```python
num1_str.lower() == 'q'
```
- `.lower()` 把字符串转成小写

## 💡 新手小贴士

1. **用 try-except 处理错误**：用户输入什么都有可能，要做好防御
2. **除法要判断0**：除以0会报错，记得检查
3. **`break` 退出循环**：在合适的地方跳出循环

## 🎯 进阶挑战

- [ ] 加上取余运算 (%)
- [ ] 加上乘方运算 (**)
- [ ] 支持连续计算（用上一次的结果继续算）
- [ ] 加上历史记录功能
- [ ] 做一个图形界面的计算器

## 🔗 相关资源

- [Python 运算符](https://www.runoob.com/python3/python3-basic-operators.html)
- [Python 异常处理](https://docs.python.org/zh-cn/3/tutorial/errors.html)
