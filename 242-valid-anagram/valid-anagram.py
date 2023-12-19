from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counter = Counter(s)
        t_counter = Counter(t)

        for item, count in s_counter.items():
            if not t_counter[item] or t_counter[item] > count:
                return False

        for item, count in t_counter.items():
            if not s_counter[item] or s_counter[item] < count:
                return False

        return True
