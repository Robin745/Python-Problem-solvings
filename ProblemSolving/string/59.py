my_dict = {}
my_list = []
def repeated_str(strings):
    for char in strings:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    my_list = list({key: value for key, value in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)})
    return my_list[0]


print(repeated_str(input(())))
