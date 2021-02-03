def string_index_deletion(word, index):
    word = [char for char in word]
    word.pop(index)
    word = "".join(word)  # list to string convertion
    # del word[index] # only for integers
    return word


print(string_index_deletion("pythonn", 5))




# def remove_char(str, n):
#     first_part = str[:n]
#     last_part = str[n+1:]
#     return first_part + last_part


# print(remove_char('Python', 0))
# print(remove_char('Python', 3))
# print(remove_char('Python', 5))
