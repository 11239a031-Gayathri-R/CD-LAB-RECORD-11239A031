def is_keyword(word, keywords):
    return word.upper() in keywords

print(is_keyword("TRACK", {"ORDER", "CANCEL", "TRACK"}))
print(is_keyword("RETURN", {"ISSUE", "RETURN", "SEARCH"}))