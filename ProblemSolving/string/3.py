
my_string = input('enter strings: ')

w1 = ""
w2 = ""

if len(my_string) > 1:
    w1 = my_string[0:2]
    w2 = my_string[-2:]
    my_string = w1 + w2
else:
    my_string = "Empty String"

print(my_string)