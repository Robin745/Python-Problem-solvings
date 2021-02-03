def making_sorted_list(original_list):
    my_list = []
    for item in original_list:
        for each in item:
            my_list.append(each)

    return list(set(my_list))


print("Original List: ", [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
                          (7, 8), (9, 10)])
print(making_sorted_list([(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
                          (7, 8), (9, 10)]))

