def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    from functools import reduce
    nums = sorted(nums)

    new_list = [tuple([nums[a], nums[b], nums[c]]) for a in range(len(nums) - 2) for b in range(a + 1, len(nums)) for c
                in range(b + 1, len(nums)) if sum([nums[a], nums[b], nums[c]]) == 0]
    print(new_list)
    final_list = [list(i) for i in set(new_list)]

    print(final_list)
    # new_list = [list(i) for i in e ]
    # nums = sorted(nums)
    # print(nums)
    # d = []
    # for a in range(len(nums)-2):
    #     for b in range(a+1,len(nums)):
    #         for c in range(b+1,len(nums)):
    #             if sum([nums[a],nums[b],nums[c]]) == 0 :
    #
    #                 d.append([nums[a],nums[b],nums[c]])
    # print(d)
    # d = [reduce(lambda x,y:set(x)-set(y),d) for i in d]
    # print(d)
    # for a in nums[:-2]:
    #     for b in nums[nums.index(a)+1:]:
    #         for c in nums[nums.index(b)+1:]:
    #             d.append([a,b,c])
    # c = sorted([i for i in e],key=lambda x:c.count(x))
    # print(c)
    # for i in e:
    #     for q in e[e.index(i)+1:]:
    #         if len(set(i)-set(q)) == 0:
    #             e.remove(q)
            # print(q)
            # print(len(set(i)-set(q)))

    # print(len(e))
    # print(e)


threeSum([-1, 0, 1, 2, -1, -4])