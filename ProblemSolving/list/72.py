lists = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

print([v for item in lists for v in (item if not str(item).isdigit() else [item])])








# new = [item for item in lists if type(item) is not list]

# new = []
# for item in lists:
#     if str(item).isdigit() != True:
#         for v in item:
#             new.append(v)
#     else:
#         new.append(item)
# print(new)











# # from stackoverflow
# from collections import Iterable

# def flatten(items):
#     """Yield items from any nested iterable; see Reference."""
#     for x in items:
#         if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
#             for sub_x in flatten(x):
#                 yield sub_x
#         else:
#             yield x
    

# lists = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# print(list(flatten(lists)))
