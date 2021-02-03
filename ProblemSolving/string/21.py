def str_upp(word):
    temp = word[0:4]
    temp = temp.upper()
    count = 0
    for i in range(4):
        if word[i].upper() == word[i]:
        # if word[i] == temp[0] or temp[1] or temp[2] or temp[3]: # not works
            count += 1
    if count >= 2:
        return word.upper()
    else:
        return word

print(str_upp("cONtinuous"))
