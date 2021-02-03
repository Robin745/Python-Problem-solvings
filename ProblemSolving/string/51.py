my_dict = {}
my_list = []


def check_repetations(string):
    for char in string:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
            my_list.append(char)
    
    first_non_repeating_character = [char for char in my_list if my_dict[char] == 1]
    return first_non_repeating_character[0]



print(check_repetations('abcabcdef'))
