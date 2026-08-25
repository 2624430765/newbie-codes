# 学生成绩统计器
# 我是Python新手，今天写个成绩统计小程序练练手！
# 功能：录入学生的名字和分数，然后自动算出平均分、最高分、最低分、及格率啥的

# 用一个列表来装所有学生
# 每个学生用一个小字典来存，字典里就两个信息：名字 和 分数
student_list = []  # 先建一个空列表，等会儿往里装学生

print("=" * 45)
print("  📊 学生成绩统计器")
print("=" * 45)
print("  输入学生的名字和分数，帮你统计全班成绩")
print("  都输入完之后，输入 '完成' 就能看结果啦")
print("=" * 45)

# 用 while 循环不停地录入学生，直到老师说"完成"才停
while True:
    name = input("\n请输入学生名字(输入'完成'结束录入): ")

    # 先看看是不是想结束录入
    if name == "完成":
        break  # break 就是跳出这个循环，不再录入了

    # 名字不能是空的（有的人会直接按回车）
    if name.strip() == "":
        print("❌ 名字不能是空的哦，重新输入")
        continue  # continue 就是跳过这次，从头再来一遍循环

    # 输入分数，这里用 try 保护一下
    # 因为万一有人手滑输入了字母（比如"九十"），程序会报错崩溃
    try:
        score = float(input(f"请输入 {name} 的分数(0-100): "))
    except ValueError:
        # 输入的不是数字，就提示一下，重新录这个学生
        print("❌ 分数必须是数字哦，请重新输入这个学生")
        continue

    # 分数范围检查，不能小于0，也不能大于100
    if score < 0 or score > 100:
        print("❌ 分数要在 0 到 100 之间哦，重新输入")
        continue

    # 都检查通过啦，把这个学生存进列表里
    # 一个字典就像一个小本本，可以同时记"名字"和"分数"两样东西
    student_list.append({"名字": name, "分数": score})
    print(f"✅ 已录入 {name}：{score} 分")

# 录入结束了，先看看有没有真的录到学生
if len(student_list) == 0:
    print("\n😅 一个学生都没录入，没法统计哦，下次记得输入~")
else:
    # 下面正式开始统计啦！
    # 1. 先算总人数（len() 能数出列表里有几个元素）
    total_count = len(student_list)

    # 2. 把所有分数单独拿出来，凑成一个新列表，方便后面计算
    #    这个写法叫"列表推导式"，就是循环 student_list，把每个人的分数取出来
    score_list = [student["分数"] for student in student_list]

    # 3. 算平均分、最高分、最低分
    #    sum() 求所有分数的总和，除以人数就是平均分啦
    average = sum(score_list) / total_count
    highest = max(score_list)  # max() 找出最大值
    lowest = min(score_list)   # min() 找出最小值

    # 4. 统计及格人数（60分及以上算及格）
    pass_count = 0  # 及格人数先归零
    for score in score_list:
        if score >= 60:
            pass_count += 1  # 每找到一个及格的，就加1（+= 就是"自己加1"的简写）

    pass_rate = pass_count / total_count * 100  # 及格率 = 及格人数 / 总人数 * 100%

    # 5. 给每个学生评级，顺便打印成绩明细
    #    90以上优秀，80-89良好，60-79及格，60以下不及格
    print("\n" + "=" * 45)
    print("  📋 成绩明细")
    print("=" * 45)
    for student in student_list:
        name = student["名字"]
        score = student["分数"]
        # 用 if-elif 一层一层判断等级
        if score >= 90:
            level = "优秀 🌟"
        elif score >= 80:
            level = "良好 👍"
        elif score >= 60:
            level = "及格 ✅"
        else:
            level = "不及格 ❌"
        print(f"  {name}：{score} 分 —— {level}")

    # 6. 打印统计结果
    print("\n" + "=" * 45)
    print("  📊 统计结果")
    print("=" * 45)
    print(f"  总人数：{total_count} 人")
    print(f"  平均分：{average:.2f} 分")   # :.2f 是保留两位小数的意思
    print(f"  最高分：{highest} 分")
    print(f"  最低分：{lowest} 分")
    print(f"  及格人数：{pass_count} 人")
    print(f"  及格率：{pass_rate:.2f}%")

    # 7. 按分数从高到低排个名次
    #    sorted() 用来排序，key= 告诉它"按什么排"，reverse=True 表示从高到低
    #    lambda 可以理解成一个"临时小函数"，这里就是取出每个学生的分数来排
    sorted_students = sorted(student_list, key=lambda s: s["分数"], reverse=True)
    print("\n  🏆 成绩排名（从高到低）:")
    # enumerate() 可以同时拿到"序号"和"学生"，start=1 表示序号从1开始
    for rank, student in enumerate(sorted_students, start=1):
        print(f"  第{rank}名：{student['名字']} ({student['分数']} 分)")

print("\n统计完成，再见~ 👋")