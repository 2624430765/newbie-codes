# 密码生成器
# 帮你生成安全的随机密码
# 可以选择长度和包含的字符类型

import random
import string  # 字符串常量模块

print("=" * 40)
print("  🔐 我的密码生成器")
print("=" * 40)

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """生成随机密码的函数"""
    
    # 准备字符池
    chars = ""
    if use_upper:
        chars += string.ascii_uppercase  # 大写字母 ABCDEFG...
    if use_lower:
        chars += string.ascii_lowercase  # 小写字母 abcdefg...
    if use_digits:
        chars += string.digits  # 数字 0123456789
    if use_symbols:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"  # 特殊符号
    
    if not chars:
        return None  # 什么字符都不选，生成不了
    
    # 随机选字符拼成密码
    password = ""
    for i in range(length):
        # 从chars里随机选一个字符
        random_char = random.choice(chars)
        password += random_char
    
    return password


while True:
    print("\n--- 生成新密码 ---")
    
    # 问用户要多长的密码
    length_str = input("密码长度 (默认12位，回车用默认): ")
    if length_str == "":
        length = 12
    else:
        try:
            length = int(length_str)
            if length < 4:
                print("❌ 密码太短啦，至少4位")
                continue
        except ValueError:
            print("❌ 请输入数字")
            continue
    
    # 问包含什么字符
    use_upper = input("包含大写字母? (y/n，默认y): ").lower() != 'n'
    use_lower = input("包含小写字母? (y/n，默认y): ").lower() != 'n'
    use_digits = input("包含数字? (y/n，默认y): ").lower() != 'n'
    use_symbols = input("包含特殊符号? (y/n，默认n): ").lower() == 'y'
    
    # 生成密码
    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    
    if password:
        print(f"\n✅ 你的随机密码是:")
        print(f"   {password}")
        
        # 评估强度
        strength = "弱"
        if length >= 12 and use_upper and use_lower and use_digits and use_symbols:
            strength = "非常强"
        elif length >= 10 and (use_upper or use_symbols):
            strength = "强"
        elif length >= 8:
            strength = "中等"
        
        print(f"   密码强度: {strength}")
    else:
        print("❌ 你一种字符都没选，生成不了密码呀")
    
    # 问要不要再来一个
    again = input("\n再来一个? (y/n): ")
    if again.lower() != 'y':
        break

print("\n👋 再见！记得保管好密码哦~")
