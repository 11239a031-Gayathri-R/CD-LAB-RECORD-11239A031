def generate_quadruples(expr):
    temp = 1
    quads = []
    stack = []
    tokens = expr.split()

    for token in tokens:
        if token.isalpha() or token.isdigit():
            stack.append(token)
        elif token in ['+', '*']:
            op2 = stack.pop()
            op1 = stack.pop()
            temp_var = f"T{temp}"
            temp += 1
            quads.append((token, op1, op2, temp_var))
            stack.append(temp_var)

    return quads

print(generate_quadruples("burger + fries * 2"))