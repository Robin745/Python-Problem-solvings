alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
            'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

string = "['Red', 'Green', 'White']"
my_list = []
temp = ''
for char in string:
    if char in alphabets:
        temp += char
    else:
        if len(temp) > 0:
            my_list.append(temp)
            temp = ''

print((my_list))


#my_list = ['', '', 'Red', '', '', '', 'Green', '', '', '', 'White', '']
#for index, value in enumerate(my_list):
    #if len(value) == 0:
        #my_list.pop(index)
#for index, value in enumerate(my_list):
    #if len(value) == 0:
        #my_list.pop(index)
#print((my_list))
