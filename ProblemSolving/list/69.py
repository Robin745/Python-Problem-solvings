def remove_duplicate(nums):
    new_nums = []
    for item in nums:
        if item in new_nums:
            pass
        else:
            new_nums.append(item)
    return sorted(new_nums)

print(remove_duplicate([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]))
