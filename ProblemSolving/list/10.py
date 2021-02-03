def check_words(word_list, n):
    result = []
    for word in word_list.split(" "):
        if len(word) > n:
            result.append(word)
    return " ".join(result)

print(check_words(input(), 3))
