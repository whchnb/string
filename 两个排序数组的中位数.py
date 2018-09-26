def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    nums = nums1 + nums2
    nums.sort()
    a = len(nums)//2
    return nums[a] if len(nums)%2 != 0 else (nums[a-1]+nums[a])/2


print(findMedianSortedArrays([1,2,3,4],[2,2,5,6]))