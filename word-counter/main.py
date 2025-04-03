import os
import re
import chardet
import argparse

def time_format(minutes) -> str:
    hours, minutes = divmod(minutes, 60)  # 直接转换为小时和分钟
    if hours and minutes:
        return f"{int(hours)}h{int(minutes)}m"
    elif hours:
        return f"{int(hours)}h"
    else:
        return f"{int(minutes)}m"

class Counter:
    def __init__(self, path):
        self.path = path
        self.files_list = self.files_info()  # 先获取文件列表，避免重复调用
        self.files = len(self.files_list)
        self.file_content = self.read_files()
        self.words = 0
        self.characters = 0
        self.read_time = ""
        self.paragraphs = 0
        self.run()

    def files_info(self) -> list:
        """ 获取文件信息, 返回文件路径列表 """
        if os.path.isfile(self.path):
            return [self.path]
        return [
            os.path.join(self.path, file)
            for file in os.listdir(self.path)
            if os.path.isfile(os.path.join(self.path, file)) and not file.startswith(".")
        ]

    def detect_encoding(self, file_path):
        """ 自动检测文件编码 """
        with open(file_path, "rb") as f:
            raw_data = f.read(1000)  # 读取部分数据进行编码检测
        result = chardet.detect(raw_data)
        return result["encoding"] or "utf-8"  # 默认回退 utf-8

    def read_files(self):
        """ 读取所有文件内容 """
        text_list = []
        for file in self.files_list:
            encoding = self.detect_encoding(file)  # 自动检测编码
            with open(file, "r", encoding=encoding, errors="replace") as f:
                text_list.append(f.read())
        return "\n".join(text_list)

    def count_characters(self):
        self.characters = len(self.file_content)

    def count_words(self):
        self.words = len(self.file_content.split())

    def count_paragraphs(self):
        """ 统计段落数：按空行分割 """
        self.paragraphs = len([p for p in re.split(r'\n\s*\n+', self.file_content) if p.strip()])

    def count_read_time(self):
        self.read_time = time_format(self.words / 200)  # 直接计算时间并转换格式

    def run(self):
        """ 执行所有统计 """
        self.count_characters()
        self.count_words()
        self.count_paragraphs()
        self.count_read_time()

    def __str__(self):
        return f"files: {self.files}, words: {self.words}, characters: {self.characters}, paragraphs: {self.paragraphs}, read time: {self.read_time}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str)
    args = parser.parse_args()
    counter = Counter(args.path)
    print(counter)


if __name__ == "__main__":
    main()