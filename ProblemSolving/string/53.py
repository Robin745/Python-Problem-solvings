my_dict = {}
my_list = []


def check_repetations(string):
    for char in string:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
            my_list.append(char)
    if my_list == None:
        repeated_character = [char for char in my_list if my_dict[char] > 1]
        return repeated_character[0]
    else:
        return None


# solution
# def first_repeated_char(str1):
#   for index, c in enumerate(str1):
#     if str1[:index+1].count(c) > 1:
#       return c
#   return "None"


print(check_repetations('abcd'))
