def sorting(items):
    sorted_list = sorted(items, key=lambda item: item[1])
    return sorted_list


print(sorting([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
