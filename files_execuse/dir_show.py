import os
import matplotlib.pyplot as plt

def count_mid_files_deep_in_subfolders(parent_folder, output_file):
    subfolder_mid_counts = {}
    for entry in os.scandir(parent_folder):
        if entry.is_dir():
            mid_count = 0
            for root, dirs, files in os.walk(entry.path):
                mid_count += sum(1 for file in files if file.endswith('.mid'))
            subfolder_mid_counts[entry.name] = mid_count

    # 按.mid文件数量对子文件夹进行排序
    sorted_subfolders = sorted(subfolder_mid_counts.items(), key=lambda x: x[1], reverse=True)
    sorted_names = [k for k, v in sorted_subfolders]
    sorted_counts = [v for k, v in sorted_subfolders]

    plt.figure(figsize=(20, 10))  # 增加图表尺寸
    plt.bar(sorted_names, sorted_counts, color='skyblue')
    plt.title('Count of MIDI Files for Each Genre', fontsize=24)
    plt.xticks(rotation=90, fontsize=24)  # 将标签旋转90度
    plt.yticks(fontsize=24)
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

# 用实际的文件夹路径替换'path_to_your_folder'，并指定输出文件名（可选）
# count_mid_files_deep_in_subfolders('dataset_mid/Mysongbook', 'Figures/未命名.jpg')
count_mid_files_deep_in_subfolders('dataset_mid/Others', 'Figures/未命名.jpg')

