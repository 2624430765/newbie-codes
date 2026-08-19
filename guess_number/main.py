# 猜数字游戏
# 我是一个Python新手，这是我写的第一个小游戏！
# 游戏规则：电脑随机生成一个1-100的数字，你来猜，我会告诉你大了还是小了

import random  # 导入随机数模块

# 生成一个1到100之间的随机数
secret_number = random.randint(1, 100)

print("=" * 40)
print("  欢迎来到猜数字游戏！")
print("  我想了一个1到100之间的数字")
print("  你来猜猜看吧~")
print("=" * 40)

guess_count = 0  # 记录猜了几次

while True:  # 无限循环，直到猜对
    # 获取用户输入
    user_input = input("\n请输入你猜的数字: ")
    
    # 判断用户输入是不是数字
    if not user_input.isdigit():
        print("❌ 请输入数字哦！")
        continue  # 跳过这次循环，重新输入
    
    guess = int(user_input)  # 把字符串转成整数
    guess_count += 1  # 次数加1
    
    # 判断猜的对不对
    if guess < secret_number:
        print("📈 太小啦！再大一点~")
    elif guess > secret_number:
        print("📉 太大啦！再小一点~")
    else:
        print(f"\n🎉 恭喜你猜对了！答案就是 {secret_number}")
        print(f"🏆 你一共猜了 {guess_count} 次")
        
        # 给点评价
        if guess_count <= 5:
            print("🌟 太厉害了！你是猜数字大师！")
        elif guess_count <= 10:
            print("👍 不错哦，继续加油！")
        else:
            print("💪 下次一定能更快猜对！")
        
        break  # 跳出循环，游戏结束

print("\n游戏结束，欢迎再来玩！")
