def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in nums:
        a = target - i
        if a in nums:
            # print(i,a)
            print([nums.index(i), (nums[nums.index(i):].index(a))+nums.index(i)+1])
            return [nums.index(i), (nums[nums.index(i)+1:].index(a))+nums.index(i)+1]

print(twoSum([3,3,4,8,65,1,4],8))