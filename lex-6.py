def eval_postfix(expr):
    stack = []
    for token in expr.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a+b)
            elif token == '-': stack.append(a-b)
            elif token == '*': stack.append(a*b)
            elif token == '/': stack.append(a//b)
    return stack[0]

print(eval_postfix("2 3 + 5 *"))