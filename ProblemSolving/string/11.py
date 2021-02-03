def str_odd_index_remove(word):
    new = ""
    word = [char for char in word]
    new = [word[char] for char in range(len(word)) if char % 2 == 0] # getting even index value
    return "".join(new)

print(str_odd_index_remove("python"))