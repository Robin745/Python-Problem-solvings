def check_common(first_list, second_list):
    result = 0
    for member in first_list:
        if member in second_list:
            result += 1
        else:
            result = 0
    return True if result == 1 else None


print(check_common([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))

