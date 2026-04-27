def count_chars(s):
    letters = digits = spaces = others = 0
    for ch in s:
        if ch.isalpha(): letters += 1
        elif ch.isdigit(): digits += 1
        elif ch.isspace(): spaces += 1
        else: others += 1
    return letters, digits, spaces, others

print(count_chars("Pizza 123! #1"))