import os

def add_suffix_to_filenames(folder_path, suffix='r'):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 构造旧文件名和新文件名的完整路径
        old_file_path = os.path.join(folder_path, filename)
        if os.path.isfile(old_file_path):  # 只处理文件，忽略文件夹
            # 获取文件名和扩展名
            name, ext = os.path.splitext(filename)
            # 构造新文件名
            new_filename = f"{name}{suffix}{ext}"
            new_file_path = os.path.join(folder_path, new_filename)
            # 重命名文件
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename} to {new_filename}")

# 使用示例
folder_path = r"C:\Users\14168\1\Python\pythonProject\yolov5\xmltxtred\txt"  # 替换为你的文件夹路径
add_suffix_to_filenames(folder_path)