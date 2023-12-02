x =-313

# Compare terms within the square brackets [x(0), x(n)], [x(1), x(n-1)], ... and so forth
# Do this for half the length of the input number's digits
# Make a hash table that remembers all of the terms that it comes across from the left hand side
# Search the table to see if the terms in the RHS are the same
# If not, return false
# Else, return true

# x_str = str(x)
# n = len(x_str)-1
# n_by_2 = len(x_str) // 2

# if x < 0:
#     print('false')
# elif len(x_str) == 1 and x >= 0:
#     print('true')
# elif len(x_str) > 1:
#     for i in list(range(n_by_2)):
#         if x_str[i] != x_str[n-i]:
#             print('false')
#     print('true') # return true

# Without converting into a string

def isPalindrome(x: int) -> bool:
    reverse_x = []
    result = x

    if x >= 0 and x < 10:
        return True
    elif x < 0 or x % 10 == 0:
        return False
    else:
        while result != 0:
            reverse_x.append(result % 10)
            # print(reverse_x)
            result //= 10
            # print(result)
            if result < 10:
                reverse_x.append(result)
                # print(reverse_x)
                break
        x_list = reverse_x[::-1]
        return reverse_x == x_list
    
        # x_list = reverse_x[::-1]
        # if x_list == reverse_x:
        #     return True
        # else:
        #     return False
        
print(isPalindrome(x))