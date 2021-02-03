my_list = []
def check_repetations(string):
    for value in string:
        if value in my_list:
            return value
        else:
            my_list.append(value)
    return None


print(check_repetations('ab ca bc ab ca ab bc'.split()))
