from collections import defaultdict

s = 'anagram'
t = 'nagaram'

def isAnagram(s: str, t: str) -> bool:
    s_letters = defaultdict(int)
    t_letters = defaultdict(int)

    for l1 in s:
        s_letters[l1] += 1

    for l2 in t:
        t_letters[l2] += 1

    return s_letters == t_letters

print(isAnagram(s, t))