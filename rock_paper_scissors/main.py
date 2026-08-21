# 石头剪刀布游戏
# 我是Python新手，今天写个经典小游戏来练手！
# 游戏规则：石头赢剪刀，剪刀赢布，布赢石头，一样的算平局

import random  # 导入随机数模块，让电脑随机出招

# 出招的三种选择，都放在一个列表里
choices = ["石头", "剪刀", "布"]

# 记录我和电脑的得分，一开始都是0分
my_score = 0
computer_score = 0

print("=" * 40)
print("  欢迎来到石头剪刀布游戏！")
print("  输入 石头 / 剪刀 / 布，和电脑一决高下")
print("  不想玩了就输入 '退出' 结束游戏")
print("=" * 40)

while True:  # 一直循环，直到玩家想退出为止
    # 电脑随机出一个（random.choice会从列表里随机挑一个）
    computer_choice = random.choice(choices)

    # 玩家出招
    my_choice = input("\n请输入你的选择(石头/剪刀/布/退出): ")

    # 先判断玩家是不是想退出
    if my_choice == "退出":
        print("👋 游戏结束，欢迎再来~")
        break  # 跳出循环，结束游戏

    # 再检查输入是不是合法的
    if my_choice not in choices:
        print("❌ 输入不对哦，只能输入 石头、剪刀 或 布")
        continue  # 跳过本次循环，让玩家重新输入

    # 双方都出招了，把结果打印出来
    print(f"🖐 你出了：{my_choice}")
    print(f"🤖 电脑出了：{computer_choice}")

    # 判断胜负
    if my_choice == computer_choice:
        # 出的都一样，就是平局
        print("🤝 平局！")
    elif (my_choice == "石头" and computer_choice == "剪刀") or \
         (my_choice == "剪刀" and computer_choice == "布") or \
         (my_choice == "布" and computer_choice == "石头"):
        # 这三种情况是我赢，用 or 把它们连起来判断
        print("🎉 你赢啦！")
        my_score += 1  # 我的得分加1（+= 就是 自己加1 的简写）
    else:
        # 剩下的情况就是我输了
        print("😢 你输了~")
        computer_score += 1  # 电脑得分加1

    # 每局结束都打印一下当前比分
    print(f"📊 当前比分：你 {my_score} : {computer_score} 电脑")

# 循环结束（玩家说退出）后，打印最终比分
print(f"\n最终比分：你 {my_score} : {computer_score} 电脑")
print("感谢游玩！")