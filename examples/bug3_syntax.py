# Bug: Off-by-one error, last element not included
# Expected: print all elements of nums
# Actual: prints only first 4 elements

nums = [1, 2, 3, 4, 5]
for i in range(len(nums) - 1):
    print(nums[i])
