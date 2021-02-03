def string_insertion(list, string):
    my_list = []
    for item in list:
        my_list.append(string + str(item))
    return my_list


print(string_insertion([1,2,3,4], "emp"))