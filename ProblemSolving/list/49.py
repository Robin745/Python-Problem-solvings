def list_to_list_of_dictionaries(color_name, color_code):
    my_list = []
    for x in range(len(color_name)):
        my_dict = {}
        my_dict['color_name'] = color_name[x]
        my_dict['color_code'] = color_code[x]
        my_list.append(my_dict)
    return my_list


color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]

print(list_to_list_of_dictionaries(color_name, color_code))


# def my_zip(*iterables):
#     # zip('ABCD', 'xy') --> Ax By
#     sentinel = object()
#     iterators = [iter(it) for it in iterables]
#     while iterators:
#         result = []
#         for it in iterators:
#             elem = next(it, sentinel)
#             if elem is sentinel:
#                 return
#             result.append(elem)
#         yield tuple(result)


# color_name = ["Black", "Red", "Maroon", "Yellow"]
# color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]

# print([{'color_name': f, 'color_code': c} for f, c in my_zip(color_name, color_code)])
