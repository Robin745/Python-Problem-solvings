def get_max_sublist(nums):
    mx = 0
    mx_list = []
    for sub in nums:
        temp = 0
        for num in sub:
            temp += num
        if temp > mx:
            mx = temp
            mx_list = sub
    return mx_list


nums = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
print(get_max_sublist(nums))



# # solution
# num = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# print(max(num, key=sum))
