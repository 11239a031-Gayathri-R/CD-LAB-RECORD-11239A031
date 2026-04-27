def shift_reduce(expr):
    stack = []
    tokens = expr.split()

    while tokens:
        stack.append(tokens.pop(0))
        print("Shift:", stack)

        while len(stack) >= 3 and stack[-2] == '*':
            stack[-3:] = ['E']
            print("Reduce:", stack)

    return stack

print(shift_reduce("price + discount * quantity"))