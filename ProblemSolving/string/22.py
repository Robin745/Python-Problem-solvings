def lexicographical_order(word):
    word = [char for char in word] # getting every char as a list element
    word.sort()
    return word


print(lexicographical_order(input()))
