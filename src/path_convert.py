def format_path_string(path):
    # 添加引号
    # path = '"' + path + '"'
    # 反斜杠转换为双反斜杠
    path = path.replace('/', '\\')
    return path