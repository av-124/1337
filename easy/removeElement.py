nums = [0,1,2,2,3,0,4,2]
val = 2

def removeElement(nums, val) -> int:
    k = 0
    for num in nums: ### New tool
        if num != val:
            nums[k] = num
            k += 1
    return k, nums

print(removeElement(nums, val))