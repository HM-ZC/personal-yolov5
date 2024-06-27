import os


def remove_lines_with_first_digit_one(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)

            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # 过滤掉第一个数字为1的行
            lines = [line for line in lines if not (line.strip() and line.strip()[0] == '1')]

            # 将修改后的内容写回文件
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(lines)


# 使用示例
folder_path = r"C:\Users\14168\1\Python\pythonProject\yolov5\xmltxtred\txt"  # 替换为你的文件夹路径
remove_lines_with_first_digit_one(folder_path)