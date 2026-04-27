class SymbolTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def lookup(self, key):
        return self.table.get(key, "Not Found")

sym = SymbolTable()
sym.insert("Cake", {"price": 50, "stock": 20})
print(sym.lookup("Cake"))