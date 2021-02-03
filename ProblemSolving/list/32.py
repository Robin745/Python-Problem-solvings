def check_sublist(list1, list2):
    count = 0
    if list1 == list2:
        return True
    elif len(list2) > len(list1):
        return False

    elif len(list1) > len(list2):
        temp_index = 0
        for value in list1:
            if value in list2:
                if value == list2[temp_index]:
                    count += 1
                    temp_index += 1

    if count == len(list2):
        return True
    else:
        return False
            

print(check_sublist([2, 4, 3, 5, 7], [4, 3]))
