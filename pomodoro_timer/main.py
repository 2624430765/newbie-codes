# 番茄钟计时器
# 我是Python新手，这是我写的番茄钟小程序
# 番茄工作法：25分钟专注 + 5分钟休息，循环4次后长休息15分钟

import time  # 时间模块，用来计时和暂停

print("=" * 40)
print("   🍅 我的番茄钟计时器")
print("=" * 40)
print("  番茄工作法:")
print("  🍅 工作 25 分钟")
print("  ☕ 短休息 5 分钟")
print("  🌴 每4个番茄后长休息 15 分钟")
print("=" * 40)

# 定义时间长度（单位：秒，演示时可以改小一点测试）
# 正式版：25分钟 = 25*60 = 1500秒
# 测试版：可以改成 10 秒试试效果
work_time = 25 * 60      # 工作时间 25分钟
short_break = 5 * 60     # 短休息 5分钟
long_break = 15 * 60     # 长休息 15分钟
pomodoro_count = 0       # 已经完成的番茄数

# 把秒数转成 "分:秒" 格式，方便显示
def format_time(seconds):
    # // 是整除，得到分钟数
    minutes = seconds // 60
    # % 是取余，得到剩下的秒数
    secs = seconds % 60
    # :02d 表示两位数，不够就补0，比如 5秒显示成 05
    return f"{minutes:02d}:{secs:02d}"

# 倒计时函数，传入总秒数和提示文字
def countdown(total_seconds, message):
    print(f"\n⏰ {message}")
    print("  按 Ctrl+C 可以提前结束当前阶段")
    # range 从大到小数：从 total_seconds 开始，到 0 结束（不包含），每次减1
    for i in range(total_seconds, 0, -1):
        # \r 是回车，不换行，让数字在原地变化
        # end='' 表示不换行
        print(f"  剩余时间: {format_time(i)}", end='\r')
        # 暂停1秒
        time.sleep(1)
    # 倒计时结束后换行，再提示一下
    print(f"\n🎉 {message} 结束！")

# 主循环
while True:
    print(f"\n📊 当前已完成番茄数: {pomodoro_count}")
    choice = input("\n开始一个新番茄？(y开始 / q退出 / s设置时间): ")

    if choice.lower() == 'q':
        print(f"\n👋 今天完成了 {pomodoro_count} 个番茄，明天继续加油！")
        break

    elif choice.lower() == 's':
        # 让用户自定义时间（方便测试用）
        try:
            new_work = int(input("请输入工作分钟数: "))
            work_time = new_work * 60
            new_short = int(input("请输入短休息分钟数: "))
            short_break = new_short * 60
            new_long = int(input("请输入长休息分钟数: "))
            long_break = new_long * 60
            print(f"✅ 设置成功！工作{new_work}分钟 / 短休{new_short}分钟 / 长休{new_long}分钟")
        except ValueError:
            print("❌ 请输入数字哦")
        continue

    elif choice.lower() == 'y':
        # 开始番茄钟
        try:
            # 1. 工作时间
            countdown(work_time, "🍅 专注工作中")
            pomodoro_count += 1  # 完成一个番茄，数量+1
            print(f"🎯 太棒了！已完成第 {pomodoro_count} 个番茄")

            # 2. 判断休息类型
            # 每4个番茄后长休息
            if pomodoro_count % 4 == 0:
                countdown(long_break, "🌴 长休息时间，好好放松")
            else:
                countdown(short_break, "☕ 短休息时间，喝杯水吧")

        except KeyboardInterrupt:
            # 用户按了 Ctrl+C 提前结束
            print("\n\n⏸️  番茄被打断了，休息一下再来吧！")

    else:
        print("❌ 看不懂，输入 y 开始、q 退出、s 设置")

print("\n程序结束~")
