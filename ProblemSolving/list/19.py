def list_defference(list1, list2):
    my_list = []
    for item in list1: # checking list 1
        if item not in list2:
            my_list.append(item)
    for item in list2: # checking list 2
        if item not in list1:
            my_list.append(item)
    return my_list


print(list_defference([1, 3, 5, 7, 9], [1, 2, 4, 6, 7, 8]))
