def str_position_exchange(word):
    return word[-1:] + word[1:-1] + word[0:1]

print(str_position_exchange("Hello, world!"))