def check(strings):
    count = 0
    for string in strings:
        if len(string) > 1 and string[0] == string[-1]:
            count += 1
    return count


print(check(['abc', 'xyz', 'aba', '1221']))
