# def newline_removal(word):
#     # reversed_word = "".join(reversed(word))
#     # new_word = [char for char in reversed_word]
#     new_word = reversed_word(word)
#     for index in range(len(new_word)):
#         # if new_word[index] != " ":
#         #     break
#         if new_word[index] ==  " ":
#             new_word.pop(index)
#         else:
#             break
#     print(new_word)
#     final_word = reversed_word(new_word)
#     return "".join(final_word)

# def reversed_word(word):
#     print(len(word))
#     reversed_word = "".join(reversed(word))
#     new_word = [char for char in reversed_word]
#     return new_word

# print(newline_removal("python exercises       "))

z = 'Python Exercises\n'
print(z.rstrip())

