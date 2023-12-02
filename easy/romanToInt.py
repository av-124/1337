# AV (12/10/23)

# Read the string from right to left.
# If the value of the next Roman numeral in the string is larger than the 
# current numeral, perform addition of the two values and move on to the 
# next numeral.
# If it is not, add the first value and subtract the second value before moving
# on to the next pair.

# First, identify the characters in the input string

s = "DCXVI" # test string

# Make some sort of dictionary where you can store the values of the 7 Roman
# numerals
RN_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

num_array = [] # initialise array

# Create an equivalent numerical array from the input string
for i in list(range(len(s))):
    num = RN_dict[s[i]]
    num_array.append(num)
    
    if len(s) == 1:
        print(num) # end here and return

# if len(s) > 1:
#     rev_num_array = num_array[::-1] # reverse num array
#     sum = rev_num_array[0] # add first element to sum
#     for i in range(1, len(rev_num_array)):
#         if rev_num_array[i] >= rev_num_array[i-1]:
#             sum = sum + rev_num_array[i]
#         elif rev_num_array[i] < rev_num_array[i-1]:
#             sum = sum - rev_num_array[i]
#     print(sum)

if len(s) > 1:
    sum = 0
    for i in range(len(num_array)):
        if i < len(num_array)-1 and num_array[i] < num_array[i+1]:
            sum -= num_array[i]
        else:
            sum += num_array[i]
    print(sum)