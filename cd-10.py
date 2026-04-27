def tokenize(expr):
    tokens = []
    for t in expr.split():
        if t.isalpha():
            tokens.append(("ID", t))
        else:
            tokens.append(("OP", t))
    return tokens

print(tokenize("ITEM + ITEM - DISCOUNT"))