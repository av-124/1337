from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    group_anagrams = defaultdict(list) ### New tool
    for string in strs:
        sorted_string = ''.join(sorted(string)) ### New tool
        group_anagrams[sorted_string].append(string)
    return list(group_anagrams.values())

print(groupAnagrams(strs))