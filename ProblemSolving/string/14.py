def sorting_alphanumerically(sentence):
    listed_sentence = sentence.split(",")
    listed_sentence.sort()
    return ", ".join(listed_sentence)


print(sorting_alphanumerically("red,black,pink,green"))
