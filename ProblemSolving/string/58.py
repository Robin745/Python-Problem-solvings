def move_spaces(string):
    only_letters = [char for char in string if char != " "]
    spaces = len(string) - len(only_letters)
    front_space = " " * spaces
    return front_space +  "".join(only_letters)

print(move_spaces(input()))