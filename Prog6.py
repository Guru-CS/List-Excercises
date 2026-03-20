def larger_than_n(nums, n):
    new_list = []
    for i in nums:
        if i > n:
            new_list.append(i)
    return new_list


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input("Enter a number: "))
print(larger_than_n(nums, n))
