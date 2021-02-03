def get_commons(list1, list2):
    my_list = []
    for item in list1:
        if item in list2:
            my_list.append(item)
    return my_list

print(get_commons([1,3,5,7,9,0, 20,40,60], [2,4,6,8,0,20,40,80]))
    