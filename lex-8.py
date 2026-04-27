def infix_to_prefix(expr):
    def reverse_expr(s):
        s = s[::-1]
        s = s.replace('(', '#').replace(')', '(').replace('#', ')')
        return s

    rev = reverse_expr(expr)
    postfix = infix_to_postfix(rev)
    return " ".join(postfix.split()[::-1])

print(infix_to_prefix("price + discount * quantity"))