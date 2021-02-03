# def str_reverse(word):
#     print(word)
#     return "".join(reversed(word))  # reverse string

rearranged_list = []
def word_rearranged(sentence):
    for index in range(1, len(sentence)):
        # rearranged_list[index] = sentence[index] # IndexError: list assignment index out of range
        rearranged_list.append(sentence[-index])
    return " ".join(rearranged_list)


# def word_rearranged(sentence):
#     # rearranged_list = [rearranged_list.append(sentence[-index]) for index in range(1, len(sentence))] # need not no append because of autimatically appending inside the new list. no need to manually append
#     rearranged_list = [sentence[-index] for index in range(1, len(sentence)+1)] # +1 for one extra looping
#     return " ".join(rearranged_list)


print(word_rearranged(input().split()))


