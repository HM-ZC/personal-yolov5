import os


def modify_first_digit(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)

            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # 修改每行第一个数字为1的行
            modified_lines = []
            for line in lines:
                stripped_line = line.lstrip()
                if stripped_line and stripped_line[0] == '1':
                    modified_lines.append('2' + stripped_line[1:])
                else:
                    modified_lines.append(line)

            # 将修改后的内容写回文件
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(modified_lines)


# 使用示例
folder_path = r"C:\Users\14168\1\Python\pythonProject\yolov5\ballwooden\temp"  # 替换为你的文件夹路径
modify_first_digit(folder_path)