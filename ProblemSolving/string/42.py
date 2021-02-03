my_dict = {}
my_list = []
def check_repeated_char(string):
    for char in string:
        if string.count(char) > 1:
            my_dict[char] = string.count(char)
            # print(f"{char} {string.count(char)}")
    for key, value in my_dict.items():
        print(key, value)
    #     temp = [key, value]
    #     my_list.append(temp)
    # print(my_list)

check_repeated_char("thequickbrownfoxjumpsoverthelazydog")
