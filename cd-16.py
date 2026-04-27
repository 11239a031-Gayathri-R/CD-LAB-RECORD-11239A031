def generate_code(tac):
    code = []
    for op, a, b, res in tac:
        if op == '=':
            code.append(f"{res} = {a}")
        else:
            code.append(f"{res} = {a} {op} {b}")
    return code

tac = [('+','b','c','t1'), ('*','a','t1','t2'), ('=','t2','','total')]
print(generate_code(tac))