def get_char(word):
    # return word[:3] if len(word) > 3 else word
    if len(word) < 3:
        return word
    else:
        return word[0:3]

print(get_char("python"))
