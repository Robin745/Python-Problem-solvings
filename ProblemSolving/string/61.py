def remove_duplicate(word):
    word = set(word)
    print("".join(word))

remove_duplicate(input())






# def remove_duplicate(word):
#     new_word = ""
#     for char in word:
#         if char in new_word:
#             pass
#         else:
#             new_word += char
#     print("".join(new_word))

# remove_duplicate(input())







# # for repeated characters
# my_dict = {}
# my_list = []
# def remove_repeated_word(word):
#     for char in word:
#         if char in my_dict:
#             my_dict[char] += 1
#         else:
#             my_dict[char] = 1
#             my_list.append(char)
    
#     repeating_character = [char for char in my_list if my_dict[char] == 1]
#     print(my_dict)
#     print("".join(repeating_character))

# remove_repeated_word('python exercises practice solution')






