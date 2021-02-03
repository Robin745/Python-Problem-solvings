def caesar_encryption(strings, step):
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    my_list = []

    for str in strings:
        if str in uppercase:
            # index = uppercase.index(str) # doing shortcut below
            my_list.append(uppercase[uppercase.index(str)+step])
        elif str in lowercase:
            # index = lowercase.index(str) # doing shortcut below
            my_list.append(lowercase[lowercase.index(str)+step])
    return my_list


print(caesar_encryption("abc", 2))


