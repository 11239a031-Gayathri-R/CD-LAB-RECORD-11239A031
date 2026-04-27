import re

def is_valid_vin(vin):
    pattern = r'^[A-Za-z][A-Za-z0-9]{16}$'
    return bool(re.match(pattern, vin))

print(is_valid_vin("1HGCM82633A004352"))
print(is_valid_vin("HGCM82633A004352"))

pattern = r'^[A-Za-z][A-Za-z0-9_]*$'
print(bool(re.match(pattern, "Cake_01")))
print(bool(re.match(pattern, "_Cake")))