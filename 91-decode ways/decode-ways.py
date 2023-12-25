class Solution:
    def numDecodings(self, s: str) -> int:
        decodingSet = {str(i) for i in range(1, 27)}

        # count = 0

        def recurse(s, memo=None, count=0):
            # nonlocal count

            if memo is None:
                memo = {}
            if s in memo:
                count += memo[s]
                return count

            if len(s) == 0:
                count += 1
                return count

            for i in range(len(s)):
                if s[:i + 1] not in decodingSet:
                    continue
                count = recurse(s[i + 1:], memo, count)
            memo[s] = count
            return memo[s]

        return recurse(s)
        # return count
