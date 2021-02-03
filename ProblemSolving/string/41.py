my_list = []
def stripping(sentence, strip):
    for char in sentence:
        if char not in strip:
            my_list.append(char)
    return "".join(my_list)


print(stripping("The quick brown fox jumps over the lazy dog.", "aeiou"))



