import guitarpro
import json

def serialize_obj(obj, max_depth=4, current_depth=0):
    """递归序列化对象到JSON兼容的结构。

    Args:
        obj (any): 要序列化的对象。
        max_depth (int): 最大递归深度，防止无限递归。
        current_depth (int): 当前递归的深度。
    Returns:
        dict: JSON兼容的字典。
    """
    if current_depth >= max_depth:
        return "Maximum depth reached"
    
    if isinstance(obj, (str, int, float, bool, type(None))):
        return obj
    
    if isinstance(obj, (list, tuple, set)):
        return [serialize_obj(item, max_depth, current_depth + 1) for item in obj]
    
    if isinstance(obj, dict):
        # 确保所有键都是字符串
        return {str(k): serialize_obj(v, max_depth, current_depth + 1) for k, v in obj.items()}
    
    result = {}
    if hasattr(obj, '__dict__'):
        for key, value in obj.__dict__.items():
            result[str(key)] = serialize_obj(value, max_depth, current_depth + 1)
    else:
        attributes = dir(obj)
        for attr in attributes:
            if not attr.startswith("__"):
                try:
                    value = getattr(obj, attr)
                    if callable(value) or attr.startswith("_"):
                        continue
                    result[str(attr)] = serialize_obj(value, max_depth, current_depth + 1)
                except AttributeError:
                    continue
    return result

def save_object_to_json(obj, filename):
    """将对象的结构保存到JSON文件。

    Args:
        obj (any): 要保存的对象。
        filename (str): 输出文件名。
    """
    with open(filename, 'w') as f:
        json.dump(serialize_obj(obj), f, indent=4)


if __name__ == "__main__":
    # 读取gpx文件
    song = guitarpro.parse('X Japan - Endless Rain.gp4')
    track = song.tracks[5]
    measure = track.measures[6]
    voice = measure.voices[0]
    beat = voice.beats[0]
    note = beat.notes[0]
    object_list = [song, track, measure, voice, beat, note]

    for i, objects in enumerate(object_list):
        # 设置解析对象
        object_parse = objects
        # 获取对象类型的名称
        object_type_name = type(object_parse).__name__
        # 构建文件名，包含对象类型
        filename = f"json_file/gpx_file_parse/{i}-{object_type_name}_Structure.json"
        # 解析对象并存为json文件
        save_object_to_json(object_parse,filename)



