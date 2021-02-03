
my_string = input("enter string: ")
# final_string = my_string.replace('r', '$')
my_list = []
my_list[:] = my_string
fch = my_list[0]
del my_list[0]



new_lists = []
for char in my_list:
    new_list = char.replace(fch, '$')
    new_lists.append(new_list)

new_string = ""
new_string = new_string.join(new_lists)

print(fch+new_string)
