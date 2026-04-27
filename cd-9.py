def wc(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    lines = text.count('\n') + 1 if text else 0
    words = len(text.split())
    chars = len(text)
    return lines, words, chars