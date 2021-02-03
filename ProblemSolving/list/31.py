def count_from_range(my_list, min, max):
    count = 0  
    for item in my_list:
        if item <= max and item >= min:
            count += 1
    return count


print(count_from_range([10, 20, 30, 40, 40, 40, 70, 80, 99], 40, 100))
