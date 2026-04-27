def is_balanced(expr):
    stack = []
    for ch in expr:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

print(is_balanced("(deposit + withdraw - transfer))"))
print(is_balanced("((math + science) + (english + social))"))