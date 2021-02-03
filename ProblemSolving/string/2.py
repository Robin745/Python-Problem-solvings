my_string = input("enter strings: ")

char_freq = {}

for i in my_string:
    if i in char_freq:
        char_freq[i] += 1
    else:
        char_freq[i] = 1

print(str(char_freq))
