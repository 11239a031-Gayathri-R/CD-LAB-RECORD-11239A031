import re

def validate_discount(expr):
    pattern = r'^[A-Za-z]+(\s*[\+\-]\s*[A-Za-z]+)*$'
    return bool(re.match(pattern, expr))

expr = "A + B - (C + D)"
print(validate_discount(expr))


import re

def validate_ticket(ticket):
    pattern = r'^PARK\-[A-Z0-9]{2,}\-\d{4}$'
    return bool(re.match(pattern, ticket))

ticket = "PARK-AB12-0045"
print(validate_ticket(ticket))