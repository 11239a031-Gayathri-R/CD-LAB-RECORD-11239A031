def infix_to_postfix(expr):
    prec = {'+':1, '-':1, '*':2, '/':2, '(':0}
    stack = []
    output = []

    for token in expr.split():
        if token.isalpha() or token.isdigit():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and prec[stack[-1]] >= prec[token]:
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return " ".join(output)

print(infix_to_postfix("price + discount * quantity"))