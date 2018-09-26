def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i
    return -7

print(pivotIndex(
    # [-1,-1,-1,-1,-1,0]
    # [1, 7, 3, 6, 5, 6]
[1, 2, 3]
))
