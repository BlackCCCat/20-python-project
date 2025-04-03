import random
import re
import sys
import pyperclip  # 用于复制文本到剪贴板
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLineEdit, QSlider, QLabel, QCheckBox, QMessageBox
)
from PyQt6.QtCore import Qt


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


class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.password_length_label = QLabel("Password Length (4-36): 16")
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(4)
        self.slider.setMaximum(MAX_LENGTH)
        self.slider.setValue(16)
        self.slider.valueChanged.connect(self.update_length_label)

        self.include_upper = QCheckBox("Include Uppercase Letters")
        self.include_upper.setChecked(True)
        self.include_numbers = QCheckBox("Include Numbers")
        self.include_numbers.setChecked(True)
        self.include_symbols = QCheckBox("Include Symbols")
        self.include_symbols.setChecked(True)

        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.generate_password)

        self.copy_button = QPushButton("Copy Password")
        self.copy_button.clicked.connect(self.copy_password)  # 复制密码的功能

        self.password_output = QLineEdit()
        self.password_output.setReadOnly(True)

        self.password_strength_label = QLabel("Password Security: ")

        layout.addWidget(self.password_length_label)
        layout.addWidget(self.slider)
        layout.addWidget(self.include_upper)
        layout.addWidget(self.include_numbers)
        layout.addWidget(self.include_symbols)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.copy_button)  # 添加复制按钮
        layout.addWidget(self.password_output)
        layout.addWidget(self.password_strength_label)

        self.setLayout(layout)

    def update_length_label(self, value):
        self.password_length_label.setText(f"Password Length (4-36): {value}")
        self.generate_password()  # 直接生成密码

    def generate_password(self):
        length = self.slider.value()
        include_upper = self.include_upper.isChecked()
        include_numbers = self.include_numbers.isChecked()
        include_symbols = self.include_symbols.isChecked()

        password = generate_password(length, include_upper, include_numbers, include_symbols)
        self.password_output.setText(password)

        strength_label, color = check_password(password)
        self.password_strength_label.setText(f"Password Security: {strength_label}")

        # 设置背景色
        self.password_output.setStyleSheet(f"background-color: {color}; color: black;")

    def copy_password(self):
        password = self.password_output.text()
        if password:
            pyperclip.copy(password)  # 使用pyperclip模块复制密码
            QMessageBox.information(self, "Copied", "Password copied to clipboard!")  # 复制成功提示


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec())
