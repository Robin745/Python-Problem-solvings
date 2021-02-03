def vowel_check(word):
    vowels = 'aeiou'
    print(len([char for char in word if char in vowels]))

    my_list = [char for char in word if char in vowels]
    print(list(dict.fromkeys(my_list))) # convert duplicate element of list

vowel_check("w3resource")
