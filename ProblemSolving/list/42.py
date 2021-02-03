def comparing_lists(list1, list2):
    new_sting1 = ""
    for item in list1:
        if item not in list2:
            new_sting1 += item
    new_sting2 = ""
    for item in list2:
        if item not in list1:
            new_sting2 += item
    print(f"Missing values in second list: ", ",".join(new_sting1))
    print(f"Missing values in second list: ", ",".join(new_sting2))
list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = ['d', 'e', 'f', 'g', 'h']
comparing_lists(list1, list2)