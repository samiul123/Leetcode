class Solution:
    def minOperations(self, s: str) -> int:
        start0_count = 0
        start1_count = 0

        # assume s starts with 0
        for i in range(len(s)):
            if i%2 == 0 and s[i] != "0":
                start0_count += 1
            elif i%2 == 1 and s[i] != "1":
                start0_count += 1

        # assume s starts with 1
        for i in range(len(s)):
            if i%2 == 0 and s[i] != "1":
                start1_count += 1
            elif i%2 == 1 and s[i] != "0":
                start1_count += 1

        return min(start0_count, start1_count)


