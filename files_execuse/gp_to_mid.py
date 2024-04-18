import os
import subprocess

def process_files(folder_path):
    """
    遍历文件夹中的所有文件，并将每个文件的完整文件名传递给 convert_guitarpro_to_midi() 进行处理
    """
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件扩展名是否为 .gp4、.gp5 或 .gtp
            if file.lower().endswith(('.gp4', '.gp5', '.gtp')):
                file_path = os.path.join(root, file)
                convert_guitarpro_to_midi(file_path)

def convert_guitarpro_to_midi(file_path):
    """
    使用 GuitarProToMidi 工具将 Guitar Pro 文件转换为 MIDI 格式
    """
    # 构造命令行命令
    command = ["./GuitarProToMidi", file_path]
    
    try:
        # 执行命令
        subprocess.run(command, check=True)
        print("转换完成！")
    except subprocess.CalledProcessError as e:
        # 处理执行命令时出现的错误
        print("转换失败:", e)

# 指定要处理的文件夹路径
folder_path = "dataset_mid"  # 替换为你的文件夹路径

# 调用 process_files 函数，传递文件夹路径
process_files(folder_path)
