# word_list = []
def longest_word(words):
    words = words.split() # each word in a list by space # split converts strings into a list

    # word_list[:] = words 
    words.sort(key=len)
    return words[-1]


print(longest_word("write something new"))



