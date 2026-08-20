# 番茄钟计时器 - 新手教程

## 🍅 程序介绍

一个命令行版的番茄钟计时器，实现番茄工作法：25分钟专注 + 5分钟休息，每4个番茄后长休息15分钟。

## 📚 学到的知识点

### 1. time 模块 - 时间相关操作
```python
import time
time.sleep(1)  # 暂停1秒
```
- `time.sleep(秒数)` 让程序暂停指定秒数
- 这是制作计时器的核心函数

### 2. 自定义函数 def
```python
def format_time(seconds):
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes:02d}:{secs:02d}"
```
- `def` 定义函数，后面跟函数名和参数
- `return` 返回计算结果
- 把常用的代码封装成函数，调用方便

### 3. // 整除和 % 取余
```python
125 // 60  # = 2，整除，得到分钟
125 % 60   # = 5，取余，得到剩下的秒数
```
- `//` 地板除法，只保留整数部分
- `%` 取模/取余，得到相除后的余数

### 4. f-string 格式化 :02d
```python
f"{minutes:02d}:{secs:02d}"
# 如果 minutes=5, secs=3，显示成 "05:03"
```
- `:02d` 表示：两位数，不足2位前面补0
- 让时间显示更整齐好看

### 5. range 倒序
```python
for i in range(10, 0, -1):
    print(i)  # 输出 10, 9, 8, ... 1
```
- `range(起始, 结束, 步长)`
- 步长为负数就是倒着数
- 注意：结束值不包含，所以到0就停，不会显示0

### 6. \r 回车符（原地刷新）
```python
print(f"剩余: {time_left}", end='\r')
```
- `\r` 是回车，光标移到行首
- `end=''` 取消自动换行
- 组合起来：在同一行不断刷新，形成动画效果

### 7. try-except 捕获 Ctrl+C
```python
try:
    countdown(work_time, "工作中")
except KeyboardInterrupt:
    print("被打断了")
```
- `KeyboardInterrupt` 是用户按 Ctrl+C 产生的异常
- 捕获它可以优雅地处理中断，而不是程序崩掉

### 8. 取模判断循环周期
```python
if pomodoro_count % 4 == 0:
    long_break()  # 每4个番茄长休息
else:
    short_break() # 其他情况短休息
```
- `x % 4 == 0` 表示 x 是 4 的倍数
- 用来实现"每N次就..."的逻辑

## 💡 新手小贴士

1. **用 \r 做原地刷新比逐行打印酷多了**：试试把 `\r` 去掉看看效果对比
2. **time.sleep 是阻塞的**：sleep期间程序什么都不做，就是等
3. **函数要"一个函数只做一件事"**：`format_time` 只管格式化，`countdown` 只管倒计时
4. **Ctrl+C 打断程序**：Python 里叫 KeyboardInterrupt 异常

## 🎯 进阶挑战

- [ ] 加上提示音（播放beep声音）
- [ ] 保存每天的番茄数到文件，做统计
- [ ] 做一个图形界面版本（用 tkinter）
- [ ] 加上任务名称功能，给每个番茄打标签
- [ ] 做成番茄钟桌面小组件
- [ ] 支持暂停和继续（按空格暂停）

## 🔗 相关资源

- [Python time 模块](https://docs.python.org/zh-cn/3/library/time.html)
- [Python 函数定义](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#defining-functions)
- [番茄工作法 - 维基百科](https://zh.wikipedia.org/wiki/番茄工作法)
