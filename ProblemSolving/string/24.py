def check_str(word, str):
    return "True" if word[:len(str)] == str else "False"

print(check_str("w3resources", "w3r"))