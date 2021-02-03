def replace_char(amount):
    return amount.translate({ord(x): y for (x, y) in zip(",.", ".,")})


print(replace_char("231,442.55"))
