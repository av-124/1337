nums = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums) -> int:
    k = 0
    seen = set() ### New tool
    for num in nums:
        if num not in seen:
            seen.add(num)
            nums[k] = num
            k += 1
    return k, nums

print(removeDuplicates(nums))