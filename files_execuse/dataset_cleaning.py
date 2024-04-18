import os
import hashlib
from collections import Counter
import matplotlib.pyplot as plt

def delete_other_files(allowed_extensions, folder_path):
    def filter_files(root_dir, allowed_extensions):
        for root, dirs, files in os.walk(root_dir):
            for filename in files:
                # 获取文件的完整路径
                file_path = os.path.join(root, filename)
                # 获取文件的后缀名并转换为小写
                _, file_extension = os.path.splitext(filename)
                file_extension = file_extension.lower()
                # 检查文件后缀是否在允许的列表中
                if file_extension in allowed_extensions:
                    yield file_path
                else:
                    # 如果文件后缀不在允许的列表中，则删除文件
                    os.remove(file_path)
    # 执行文件过滤
    for file_path in filter_files(folder_path, allowed_extensions):
        print("保留文件:", file_path)

def transform_filename_capital2lower(folder_path):
    def rename_files_to_lowercase_extension(folder_path, target_extensions):
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                # 获取文件的完整路径
                file_path = os.path.join(root, filename)
                # 获取文件的后缀名并转换为小写
                base_name, ext = os.path.splitext(filename)
                if ext.upper() in target_extensions:
                    new_extension = ext.lower()
                    new_file_path = os.path.join(root, base_name + new_extension)
                    os.rename(file_path, new_file_path)
                    print(f"文件 '{filename}' 的后缀名已改为 '{new_extension}'")
    # 指定目标后缀名列表
    target_extensions = {'.GP3', '.GTP', '.GP5', '.GP4'}
    # 执行将后缀名改为小写的操作
    rename_files_to_lowercase_extension(folder_path, target_extensions)

def delete_blank_folders(folder_path):
    def remove_empty_folders(root_dir):
        for root, dirs, files in os.walk(root_dir, topdown=False):
            for folder in dirs:
                folder_path = os.path.join(root, folder)
                # 检查文件夹是否为空
                if not os.listdir(folder_path):
                    # 如果文件夹为空，则删除它
                    os.rmdir(folder_path)
                    print("已删除空文件夹:", folder_path)
    # 执行删除空文件夹操作
    for _ in range(10):
        remove_empty_folders(folder_path)

def delete_duplicate_files(folder_path):
    def find_duplicate_files(folder_path):
        # 找到文件夹中的重复文件，并返回一个包含重复文件路径的列表
        # 用于存储文件内容的哈希值和对应的文件路径
        hash_map = {}
        # 用于存储重复文件的路径
        duplicate_files = []
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                # 获取文件的完整路径
                file_path = os.path.join(root, filename)
                # 使用 MD5 哈希算法计算文件内容的哈希值
                with open(file_path, 'rb') as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
                # 如果哈希值已经存在于字典中，则说明是重复文件
                if file_hash in hash_map:
                    duplicate_files.append(file_path)
                else:
                    # 否则将哈希值和文件路径存储到字典中
                    hash_map[file_hash] = file_path
        return duplicate_files

    def remove_duplicate_files(folder_path):
        # 删除文件夹中的重复文件
        duplicate_files = find_duplicate_files(folder_path)
        for file_path in duplicate_files:
            os.remove(file_path)
            print(f"已删除重复文件: {file_path}")
    # 执行删除重复文件的操作
    remove_duplicate_files(folder_path)

def file_distribution_visualize(folder_path, save_path):
    def count_file_extensions(directory):
        # 用于存储文件后缀名的计数器
        extensions_counter = Counter()
        # 遍历指定目录及其所有子目录的所有文件
        for root, dirs, files in os.walk(directory):
            for file in files:
                # 分离文件名和后缀
                _, extension = os.path.splitext(file)
                # 统计后缀名
                extensions_counter[extension] += 1
        return extensions_counter

    def plot_extensions(extensions_counter, save_path):
        # 准备数据用于绘图
        labels = list(extensions_counter.keys())
        values = list(extensions_counter.values())
        # 创建柱状图
        plt.figure(figsize=(10, 8))
        plt.bar(labels, values, color='skyblue')
        plt.xlabel('File Extension')
        plt.ylabel('Frequency')
        plt.title('Frequency of File Extensions')
        plt.xticks(rotation=45)
        plt.tight_layout()
        # 保存图表到本地文件
        plt.savefig(save_path)
        print(f"Chart saved to {save_path}")

    # 执行上面两个函数
    extensions_counter = count_file_extensions(folder_path)
    plot_extensions(extensions_counter, save_path)


if __name__ == "__main__":
    # 指定数据集文件夹路径
    folder_path = './dataset_mid/Mysongbook'
    save_path = "./Figures/未命名.jpg"

    # 指定允许的文件后缀名
    # allowed_extensions = {'.gp4', '.gp3', '.gp5'}
    # allowed_extensions = {'.mid'}
    # 只保留特定后缀名的文件
    # delete_other_files(allowed_extensions, folder_path)

    # 将文件后缀名从大写变到小写
    # transform_filename_capital2lower(folder_path)

    # 删除文件夹内什么都没有的空文件夹
    # delete_blank_folders(folder_path)

    # 删除重复文件
    # delete_duplicate_files(folder_path)

    # 输出基于文件后缀名的文件分布柱状图
    file_distribution_visualize(folder_path, save_path)