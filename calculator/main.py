# 简易计算器
# 我是Python新手，这是我写的计算器小程序
# 支持加减乘除四种运算

print("=" * 40)
print("   🧮 我的简易计算器")
print("=" * 40)
print("  支持的运算:")
print("  1. 加法 (+)")
print("  2. 减法 (-)")
print("  3. 乘法 (*)")
print("  4. 除法 (/)")
print("=" * 40)

while True:
    # 获取第一个数字
    num1_str = input("\n请输入第一个数字 (输入q退出): ")
    if num1_str.lower() == 'q':
        print("👋 再见！")
        break
    
    # 判断是不是数字（允许小数）
    try:
        num1 = float(num1_str)
    except ValueError:
        print("❌ 这不是有效的数字，请重新输入")
        continue
    
    # 获取运算符
    op = input("请输入运算符 (+, -, *, /): ")
    
    # 获取第二个数字
    try:
        num2 = float(input("请输入第二个数字: "))
    except ValueError:
        print("❌ 这不是有效的数字")
        continue
    
    # 计算结果
    if op == '+':
        result = num1 + num2
        print(f"\n✅ {num1} + {num2} = {result}")
    elif op == '-':
        result = num1 - num2
        print(f"\n✅ {num1} - {num2} = {result}")
    elif op == '*':
        result = num1 * num2
        print(f"\n✅ {num1} × {num2} = {result}")
    elif op == '/':
        if num2 == 0:
            print("❌ 除数不能为0！数学老师会生气的")
        else:
            result = num1 / num2
            print(f"\n✅ {num1} ÷ {num2} = {result}")
    else:
        print("❌ 不认识这个运算符，只支持 + - * /")

print("\n计算结束~")
