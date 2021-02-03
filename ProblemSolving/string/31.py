# def formatted_float(num):
#     num = f"{num:,.2f}"
#     return num


# num = input('floating number: ')
# # print(formatted_float(num)) # getting error like 'ValueError: Unknown format code 'f' for object of type 'str'' # In this case num is a unicode string, which does not support the f format modifier
# print(formatted_float(float(num)))


# usagable for make it floating num inside f string rather than direct use of input funcion
def formatted_float(num):
    num = f"{+float(num):,.2f}"
    return num

print(formatted_float(input("number: ")))
