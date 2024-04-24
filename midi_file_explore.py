import os
import pypianoroll
import pretty_midi

# 指定处理的文件夹
directory = "lpd_5_cleansed"

# 获取所有的mid文件列表
all_file_path = []
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".npz"):
            file_path = os.path.join(root, file)
            all_file_path.append(file_path)

# 数据集再小一点，只截取[0:500]
all_file_path = all_file_path[0:5]
test_file = all_file_path[0]

multitrack = pypianoroll.load(test_file)

pretty = multitrack.to_pretty_midi()
print(pretty)


# # 设置解析对象
# object_parse = multitrack
# # 获取对象类型的名称
# object_type_name = type(object_parse).__name__
# # 构建文件名，包含对象类型
# filename = f"json_file/pianoroll_file_parse/{object_type_name}_Structure.json"
# # 解析对象并存为json文件
# save_object_to_json(object_parse,filename)