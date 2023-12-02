from collections import defaultdict

nums = [1,1,1,2,2,2,2]

def majorityElement(nums) -> int:
    # nums.sort()
    # i = len(nums) // 2
    # return nums[i]

    n = len(nums)
    d = defaultdict(int) ### New tool
    
    for num in nums:
        d[num] += 1
    
    n = n // 2
    for key, value in d.items():
        if value > n:
            return key
    
    return 0

print(majorityElement(nums))