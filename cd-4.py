def count_spaces_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    lines = text.split('\n')
    spaces = text.count(' ')
    return len(lines), spaces