def capitalized_word(string):
    for word in string.split():
        print(word[0].upper() + word[1:-1] + word[-1].upper(), end =" ")
    return ""


print(capitalized_word("python exercises practice solution"))
