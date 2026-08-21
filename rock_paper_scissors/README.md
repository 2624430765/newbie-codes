# 石头剪刀布 - 新手教程

## 🎮 游戏介绍

这是一个经典的小游戏。你和电脑各出「石头、剪刀、布」中的一种，规则是：
- 石头 ✊ 赢 剪刀 ✌️
- 剪刀 ✌️ 赢 布 ✋
- 布 ✋ 赢 石头 ✊
- 一样的算平局

可以一直玩，还能看到实时比分，直到你主动说「退出」。

## 📚 学到的知识点

### 1. 导入模块
```python
import random
```
- `random` 是 Python 自带的随机数模块
- 导入后才能用它里面的函数

### 2. 列表 list
```python
choices = ["石头", "剪刀", "布"]
```
- 列表用方括号 `[]` 包起来，里面可以放多个数据
- 每个数据用逗号 `,` 隔开
- 列表就像一个"盒子"，能装很多东西

### 3. random.choice 随机选择
```python
computer_choice = random.choice(choices)
```
- `random.choice(列表)` 会从列表里随机挑一个元素返回
- 用这个方法就能让电脑"随机出招"

### 4. 用户输入 input
```python
my_choice = input("请输入你的选择: ")
```
- `input()` 会暂停程序，等待你输入
- 括号里的文字是提示语
- 你输入的内容会以**字符串**形式返回

### 5. 条件判断 if / elif / else
```python
if my_choice == "退出":
    print("再见")
elif 我赢了的情况:
    print("你赢啦")
else:
    print("你输了")
```
- `if` 如果...
- `elif` 否则如果...（可以有多个）
- `else` 否则...（最后兜底）

### 6. 成员判断 in / not in
```python
if my_choice not in choices:
    print("输入不对")
```
- `in` 判断一个东西在不在列表里
- `not in` 判断一个东西**不在**列表里
- 用来检查玩家输入是不是合法的

### 7. while 循环 + break + continue
```python
while True:
    if 玩家想退出:
        break     # 跳出整个循环
    if 输入不对:
        continue  # 跳过本次，进入下一轮
```
- `while True` 是无限循环
- `break` 直接结束循环
- `continue` 跳过本次循环剩下的代码，直接开始下一次

### 8. 得分累加 +=
```python
my_score += 1
```
- `+=` 是简写，等于 `my_score = my_score + 1`
- 意思是"把自己加1，再存回自己"

### 9. f-string 格式化
```python
print(f"当前比分：你 {my_score} : {computer_score} 电脑")
```
- 字母 `f` 开头的字符串叫 f-string
- 花括号 `{}` 里可以直接放变量，会自动替换成变量的值

## 💡 新手小贴士

1. **多 print 调试**：不确定程序跑到哪了，就多打印几个 `print()` 看看
2. **注释是给自己看的**：过几天再看代码，注释能帮你快速回忆
3. **别怕报错**：报错信息会告诉你哪一行错了，仔细看就行
4. **先跑通再加功能**：先把最简单的版本写对，再慢慢变复杂

## 🎯 进阶挑战

- [ ] 改成三局两胜制，最后宣布总冠军
- [ ] 加入「蜥蜴 🦎」和「史波克 🖖」变成"石头剪刀布蜥蜴史波克"
- [ ] 记录连胜次数，连赢三局有特殊奖励提示
- [ ] 把比分保存到文件里，下次打开还能接着看

## 🔗 相关资源

- [Python 官方教程](https://docs.python.org/zh-cn/3/tutorial/)
- [菜鸟教程 - Python](https://www.runoob.com/python3/python3-tutorial.html)