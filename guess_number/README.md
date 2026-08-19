# 猜数字游戏 - 新手教程

## 🎮 游戏介绍

这是一个经典的入门编程项目。电脑随机生成一个1-100的数字，玩家来猜，电脑会提示"大了"还是"小了"，直到猜对为止。

## 📚 学到的知识点

### 1. 导入模块
```python
import random
```
- `random` 是Python自带的随机数模块
- `random.randint(1, 100)` 可以生成1到100之间的随机整数

### 2. 变量
```python
secret_number = random.randint(1, 100)
guess_count = 0
```
- 变量就是用来存数据的"盒子"
- `=` 是赋值符号，把右边的值存到左边的变量里

### 3. while 循环
```python
while True:
    # 循环体
    if 猜对了:
        break
```
- `while True` 是无限循环，会一直执行
- `break` 可以跳出循环

### 4. 用户输入
```python
user_input = input("请输入你猜的数字: ")
```
- `input()` 函数会等待用户输入
- 用户输入的内容是字符串类型

### 5. 条件判断 if / elif / else
```python
if guess < secret_number:
    print("太小啦")
elif guess > secret_number:
    print("太大啦")
else:
    print("猜对了")
```
- `if` 如果...
- `elif` 否则如果...
- `else` 否则...

### 6. 类型转换
```python
guess = int(user_input)
```
- `int()` 把字符串转成整数
- `str()` 把整数转成字符串

### 7. 字符串方法
```python
user_input.isdigit()
```
- `.isdigit()` 判断字符串是不是全是数字

## 💡 新手小贴士

1. **多打印变量**：不确定的时候，用 `print()` 把变量打印出来看看
2. **注释很重要**：用 `#` 写注释，过几天再看就懂了
3. **别怕报错**：报错是正常的，仔细看错误信息
4. **从小处开始**：先写能跑的最简单版本，再慢慢加功能

## 🎯 进阶挑战

- [ ] 加上猜的次数限制（比如最多猜7次）
- [ ] 加上难度选择（简单=1-50，困难=1-200）
- [ ] 加上排行榜，记录最好成绩
- [ ] 让电脑来猜，你来提示大了小了

## 🔗 相关资源

- [Python官方教程](https://docs.python.org/zh-cn/3/tutorial/)
- [菜鸟教程 - Python](https://www.runoob.com/python3/python3-tutorial.html)
