# Change 'nodes' when the sum of all elements preceding are less than that node
# i.e., only move to the next node if nums[i] is > total
# Make a dict where each key = current index in nums & each value = total sum from the last node to the present element
# Get the index of the starting node and the element that corresponds to the highest sum
# subArraySum = sum of all elements between these two indices (inclusive)

# General cases
# if entire array is positive, return whole array
# if entire array is negative, return max(array)
# if len(array) == 1, return the element

# Test cases
a = [8,-19,5,-4,20] # return sum of [5, -4, 20] = 21
b = [1, -2, 0, 0, 2] # 2
c = [1, -2, 0] # 1
e = [-1, -2, -4, 5] # 5
f = [1, 1, -2] # 2
g = [3,2,-3,-1,1,-3,1,-1] # 5
h = [1, 2, 3, 4, 5] # 15
i = [3,9,-9,-3,4,7,5,0,-4,-4,1,-6,-3,6,0,5,1,-2] # 16

nums = a

def maxSubArray(nums) -> int:
    # if len(nums) == 1:
    #     return nums[0]

    d = {}
    startingElementIndex = 0
    total = 0

    for i in list(range(0, len(nums))):
        if nums[i] >= (total + nums[i]): # condition to change nodes
            startingElementIndex = i # change nodes
            total = nums[i] # reset total to only include current node
        else:
            total += nums[i] # else, continue adding to the total from the previous node
        d[i] = total
    return max(d.values()) ### New tool

    # finalElementIndex = max(d, key=lambda k: d[k])
    # subArraySum = 0

    # print(startingElementIndex)
    # print(finalElementIndex) ### error if it occurs before starting element
    # print(total)
    # print(d)

    # if all(element <= 0 for element in nums):
    #     return max(nums) ### for what cases would you just return max(nums)?
    # # else:
    # elif total <= max(nums) or startingElementIndex >= finalElementIndex:
    #     return max(d.values())

    # for i in list(range(startingElementIndex, finalElementIndex+1)):
    #     subArraySum += nums[i]
    #     # print('in loop')

    # # print(subArraySum)
    # return subArraySum

print(maxSubArray(nums))