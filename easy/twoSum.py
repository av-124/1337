# AV (08/10/23)

'''
There are three potential cases depending on the input list:
- All numbers are +ve -> target must be +ve
- All numbers are -ve -> target must be -ve
- +ve and -ve numbers -> target can be +ve or -ve

Case 1
1) Check if all numbers in the list are >= 0, elseif Case 2
2) Store the indices of the original list
3) Sort the elements in ascending order
4) Filter the list so that all elements greater than the target are
removed in the new list
5) Starting with the first element, subtract this from the target and
store its value
6) Use the difference to scan the rest of the array for the same value
7) If there are no matches, move on to the second element and repeat the
above process
8) Return indices corresponding to the numbers

Case 2
1) Elseif statement should check if all numbers are strictly < 0, else Case 3
2) Similar to Case 1, except, the numbers filtered will be less than the
target

Case 3
1) The hardest case, which will likely require some form of brute force
checking by addition and comparison
'''

nums = [1, 2, 3, 5, 0]
target = 5 # Test with 0, -2, 3
indices = list(range(len(nums)))

for i in indices[:-1]:
    for j in indices[i+1:]:
        test_sum = nums[i] + nums[j]
        if target == test_sum:
            print(i, j)