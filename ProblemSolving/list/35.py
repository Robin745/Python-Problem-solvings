def concatenating(my_list, n):
    new_list = []
    for i in range(1, n+1):
        for item in my_list:
            # new_item = item + str(i)
            new_list.append(item+str(i))
    return new_list


print(concatenating(['p', 'q'], 5))
        
