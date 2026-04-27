def validate_op(expr):
    ops = ["<=", ">=", "==", "!="]
    return any(op in expr for op in ops)

print(validate_op("balance >= 5000"))

def check_speed(expr):
    return "++" in expr or "--" in expr

print(check_speed("speed++"))