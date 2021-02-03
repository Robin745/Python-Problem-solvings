my_dict = {}
my_list = []

def check_second_most_repetations(string):
    for word in string:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    my_list = list({key: value for key, value in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}) # using dictonary comprehension
    return my_list[1], my_dict[my_list[1]]    

print(check_second_most_repetations(input().split()))






# # solution
# def word_count(str):
#     counts = dict()
#     print(type(counts))
#     words = str.split()

#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1

#     counts_x = sorted(counts.items(), key=lambda kv: kv[1])
#     #print(counts_x)
#     print(type(counts))
#     return counts_x[-2], counts_x

# print(word_count("Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster."))
