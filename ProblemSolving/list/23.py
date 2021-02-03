shallow_list = []
def flatten_shallow(my_list):
    for sub_list in my_list:
        for item in sub_list:
            shallow_list.append(item)
    return shallow_list

original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
print(flatten_shallow(original_list))
