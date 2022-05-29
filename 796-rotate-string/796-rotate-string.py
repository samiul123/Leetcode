class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if len(s) == 0:
            return True

        for rotation in range(len(s)):
            if all(s[(rotation+i) % len(s)] == goal[i] for i in range(len(s))):
                return True
        return False