new_list = []

def swap_position(my_list):
    # new_list = [x for x in my_list]

    for i in range(len(new_list)-1):
        if i % 2 == 0:
            my_list[i] = new_list[i+1]
            my_list[i+1] = new_list[i]
    return my_list


print(swap_position([0, 1, 2, 3, 4, 5]))
