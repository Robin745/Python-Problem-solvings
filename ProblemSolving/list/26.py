def check_identical(list1, list2):
    identical = False
    for item in list1:
        if item in list2:
            identical = True
        else:
            identical = False
            break
    for item in list2:
        if item in list1:
            identical = True
        else:
            identical = False
            break
    
    return identical


print(check_identical([10, 10, 0, 0, 10], [10, 10, 10, 0, 0]))
