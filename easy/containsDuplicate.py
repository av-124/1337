nums = [1, 2, 3, 4, 2]

def containsDuplicate(nums) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    print(seen)
    return False
print(containsDuplicate(nums))