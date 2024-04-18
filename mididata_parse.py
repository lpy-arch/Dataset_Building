from music21 import *
import pretty_midi
from collections import Counter
import os
import matplotlib.pyplot as plt
from tqdm import tqdm



def Tutorial_stream_structure():
    score = stream.Score()

    part = stream.Part()
    bass_line = stream.Part()

    voice1 = stream.Voice()
    voice2 = stream.Voice()

    notes = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]

    for notename in notes:
        melody_note = note.Note(notename)
        voice1.append(melody_note)

        harmony_note = melody_note.transpose(-8)
        voice2.append(harmony_note)

        bass_note = note.Note(notename)
        bass_note.octave -= 2
        bass_line.append(bass_note)
        
    part.append([voice1, voice2])

    score.insert(0, part)
    score.insert(0, bass_line)

    score.write('midi', fp='output.mid')


def plot_instruments(counter, save_path):
     # 对后缀名计数器按照计数值从大到小排序
    counter = sorted(counter.items(), key=lambda x: x[1], reverse=False)    
    # 准备数据用于绘图
    labels = [item[0] for item in counter]
    values = [item[1] for item in counter]
    # 创建柱状图
    plt.figure(figsize=(30, 24))
    plt.barh(labels, values, color='skyblue')
    plt.xlabel('Frequency')
    plt.ylabel('Instruments')
    plt.title('Frequency of Instruments')
    plt.tight_layout()
    # 保存图表到本地文件
    plt.savefig(save_path)
    print(f"Image saved to {save_path}")


if __name__ == "__main__":
    # 处理的文件夹
    directory = "dataset_mid/Mysongbook"

    # 获取所有的mid文件列表
    all_file_path = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mid"):
                file_path = os.path.join(root, file)
                all_file_path.append(file_path)

    # 数据集再小一点，只截取[0:500]
    all_file_path = all_file_path[0:500]

    # 对文件列表中的参数进行统计
    instrument_conut = Counter()
    for file in tqdm(all_file_path, desc='Processing', unit='file'):
        try:
            # 用pretty_midi解析mid文件时是要"try"的，因为可能会有不符合规范的mid文件
            midi_file = pretty_midi.PrettyMIDI(file)
            # 获取mid文件中所有的乐器，是所有乐器组成的列表
            instruments = midi_file.instruments

            # 遍历每一个乐器
            for item in instruments:
                # 先把lable设定成others，后面如果发现是想要的乐器类型的话，就改过来了
                instrument_lable = "others"
                # 判断是否是鼓，因为鼓的编号不在标准音色表里
                if item.is_drum:
                    instrument_lable = "Drum"
                else:
                    # 标准音色编号到乐器类别的映射
                    instrument_map = {
                        "vocal": [56, 57, 58, 59, 60, 61, 62, 63, 80, 81, 82, 83, 84, 85, 86, 87, 73, 71, 66, 65, 40],
                        "piano": [0, 1, 2, 3, 4, 5, 6, 7],
                        "clean_guitar": [26, 27, 24, 25, 31],
                        "electric_guitar": [28, 29, 30],
                        "bass": [32, 33, 34, 35, 36, 37, 38, 39]
                        }
                    # 如果编号在映射里，就更新lable
                    for lable, numbers in instrument_map.items():
                        if item.program in numbers:
                            instrument_lable = lable

                instrument_conut[instrument_lable] += 1
        except Exception as e:
            print(f"Error processing item {item}: {e}")
            continue

    plot_instruments(instrument_conut, "未命名.jpg")
