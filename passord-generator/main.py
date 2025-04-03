import random
import re
from colorama import Fore, Style

MAX_LENGTH = 36  # 设置最大长度为常量

# 可选的字符集提前定义
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_LETTERS = LETTERS.upper()
NUMBERS = '0123456789'
SYMBOLS = '!@#$%^&*()'


def generate_password(length=16, include_upper=True, include_numbers=True, include_symbols=True):
    """生成一个随机密码，支持大写字母、数字和符号"""
    chars = LETTERS  # 默认使用小写字母
    if include_upper:
        chars += UPPER_LETTERS
    if include_numbers:
        chars += NUMBERS
    if include_symbols:
        chars += SYMBOLS
    
    # 使用 random.choices 生成密码，允许字符重复
    return ''.join(random.choices(chars, k=length))


def get_len_percent(password):
    """根据密码长度返回强度百分比"""
    password_length = len(password)
    
    if password_length < 4:
        return 0
    elif password_length > MAX_LENGTH:
        return 100  # 超过最大长度的密码被视为最大强度
    return min((password_length / MAX_LENGTH) * 100, 100)  # 对应长度的百分比


def check_password(password):
    """检查密码安全性"""
    # 使用一行代码检查各个要求
    conditions = [
        bool(re.search(r'\d', password)),  # 数字
        bool(re.search(r'[A-Z]', password)),  # 大写字母
        bool(re.search(r'[a-z]', password)),  # 小写字母
        bool(re.search(r'[!@#$%^&*()]', password))  # 符号
    ]
    
    # 满足的条件数目
    valid_conditions = sum(conditions)
    
    # 计算密码的安全性百分比
    length_percent = get_len_percent(password)
    percent = (length_percent + valid_conditions * 25) / 200

    # 确保基本密码长度要求
    if len(password) < 8:
        return 'Very Weak', 'red'
    elif len(password) < 12:
        return 'Weak', 'yellow'

    # 返回安全性评价
    if percent < 0.25:
        return 'Weak', 'yellow'
    elif percent < 0.5:
        return 'Normal', 'white'
    elif percent < 0.75:
        return 'Strong', 'cyan'
    else:
        return 'Very Strong', 'green'
    
def print_password_strength(password):
    strength, color = check_password(password)
    print(f"{getattr(Fore,color.upper()) + Style.BRIGHT}Password Strength: {strength}{Style.RESET_ALL}")

if __name__ == '__main__':
    password = generate_password(length=16)
    print("Generated Password:", password)
    print_password_strength(password)