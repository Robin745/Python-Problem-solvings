def check_empty(lists):
    empty = True
    for dict in lists:
        if dict:
            empty = False
            break
    return empty


print(check_empty([{}, {}, {}]))

