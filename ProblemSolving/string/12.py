def words_occurrence(sentence):
    my_dict = {}
    list_item = sentence.split()

    for word in list_item:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict

print(words_occurrence('the quick brown fox jumps over the lazy dog'))
