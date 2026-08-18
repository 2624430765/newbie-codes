# 密码生成器 - 新手教程

## 🔐 程序介绍

一个可以自定义长度和字符类型的密码生成器，还能评估密码强度。

## 📚 学到的知识点

### 1. 函数 def
```python
def generate_password(length, use_upper):
    # 函数体
    return password
```
- `def` 定义函数
- 参数是输入，`return` 返回输出
- 函数可以复用代码

### 2. string 模块
```python
import string
string.ascii_uppercase  # 大写字母
string.ascii_lowercase  # 小写字母
string.digits           # 数字
```

### 3. random.choice
```python
random.choice(chars)  # 从序列中随机选一个
```

### 4. for 循环
```python
for i in range(10):
    print(i)  # 打印0到9
```
- `range(n)` 生成0到n-1的序列
- `for` 循环遍历序列

### 5. 字符串拼接
```python
chars += "abc"
password += random_char
```
- `+=` 也可以用在字符串上

## 💡 新手小贴士

1. **函数命名要有意义**：一看就知道是干什么的
2. **参数设置默认值**：让用户可以直接回车使用默认
3. **None 表示空**：函数出错时可以返回 None

## 🎯 进阶挑战

- [ ] 确保密码每种字符至少包含一个
- [ ] 排除容易混淆的字符（如 0 和 O, l 和 1）
- [ ] 生成易记密码（单词+数字+符号）
- [ ] 批量生成多个密码
- [ ] 保存密码到加密文件

## 🔗 相关资源

- [Python 函数](https://www.runoob.com/python3/python3-function.html)
- [Python string 模块](https://docs.python.org/zh-cn/3/library/string.html)
