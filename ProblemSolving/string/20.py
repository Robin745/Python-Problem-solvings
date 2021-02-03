def str_reverse(word):
    if len(word) % 4 == 0:
        return "".join(reversed(word))  # reverse string
    return word


print(str_reverse('BD'))
print(str_reverse('BANGLADESH'))
